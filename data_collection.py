import requests
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pulp import *
import osmnx as ox
import census


from constants import CENSUS_API_KEY, CITY, MIN_DISTANCE_BETWEEN_STATIONS, NREL_API_KEY, NUM_CANDIDATE_LOCATIONS, POPULATION_POINTS
from fallback import generate_synthetic_population_data, generate_synthetic_charging_stations

# =============================================================================
# STEP 1: DATA COLLECTION
# =============================================================================

def get_city_boundary(city_name):
    """Get the boundary of the city using OSMnx"""
    try:
        # Get the city boundary as a GeoDataFrame
        city_gdf = ox.geocode_to_gdf(city_name)
        return city_gdf
    except Exception as e:
        print(f"Error getting city boundary: {e}")
        # Fallback to a simple bounding box if geocoding fails
        city_point = ox.geocode(city_name)
        lng, lat = city_point
        bbox = (lng - 0.1, lat - 0.1, lng + 0.1, lat + 0.1)  # Simple bounding box
        return bbox

def get_road_network(city_gdf):
    """Get the road network using OSMnx"""
    try:
        # Get the road network within the city boundary
        G = ox.graph_from_polygon(city_gdf.iloc[0].geometry, network_type='drive')
        # Convert to GeoDataFrame
        nodes, edges = ox.graph_to_gdfs(G)
        print(f"Retrieved {len(nodes)} road network nodes and {len(edges)} edges")
        return nodes, edges
    except Exception as e:
        print(f"Error getting road network: {e}")
        # Fallback to smaller area if the city is too large
        city_point = ox.geocoder.geocode(CITY)
        G = ox.graph_from_point(city_point, dist=5000, network_type='drive')
        nodes, edges = ox.graph_to_gdfs(G)
        print(f"Retrieved {len(nodes)} road network nodes and {len(edges)} edges")
        return nodes, edges

def get_population_data(city_gdf):
    """Get population density data from US Census API"""
    if not CENSUS_API_KEY:
        print("Census API key not provided. Using synthetic population data.")
        return generate_synthetic_population_data(city_gdf)
    
    try:
        # Initialize Census API client
        c = census.Census(CENSUS_API_KEY)
        
        # Get city boundary for filtering
        city_geom = city_gdf.iloc[0].geometry
        minx, miny, maxx, maxy = city_geom.bounds
        
        # Get the state code and try to determine county
        state_name = CITY.split(',')[1].strip()
        city_name = CITY.split(',')[0].strip()
        
        state_fips = {
            'WA': '53', 'OR': '41', 'CA': '06', 'TX': '48', 'NY': '36', 'FL': '12', 'IL': '17'
        }.get(state_name, '53')  # default to WA
        
        # Try to get data for specific counties first
        county_fips = get_county_fips_for_city(city_name, state_name, state_fips)
        
        if county_fips:
            print(f"Getting census data for specific counties: {county_fips}")
            census_data = []
            for county in county_fips:
                try:
                    county_data = c.acs5.state_county_tract(
                        fields=('NAME', 'B01003_001E'),  # Population
                        state_fips=state_fips,
                        county_fips=county,
                        tract='*',
                        year=2019
                    )
                    census_data.extend(county_data)
                except:
                    continue
        else:
            # Fallback: get limited data for the state
            print("County not found, getting limited state data")
            census_data = c.acs5.state_county_tract(
                fields=('NAME', 'B01003_001E'),
                state_fips=state_fips,
                county_fips='*',
                tract='*',
                year=2019
            )
            # Take only first POPULATION_POINTS tracts to avoid processing entire state
            census_data = census_data[:POPULATION_POINTS]
        
        # Convert to DataFrame
        census_df = pd.DataFrame(census_data)
        print(f"Retrieved census data for {len(census_df)} tracts")
        
        # Process the census data to create population points
        return process_census_data_to_geodataframe(city_gdf, census_df)
        
    except Exception as e:
        print(f"Error getting census data: {e}")
        return generate_synthetic_population_data(city_gdf)

def get_county_fips_for_city(city_name, state_name, state_fips):
    """Get county FIPS codes for major cities"""
    # Dictionary of major cities and their county FIPS codes
    city_county_mapping = {
        'seattle': {'WA': ['033']},  # King County
        'portland': {'OR': ['051']},  # Multnomah County
        'los angeles': {'CA': ['037']},  # Los Angeles County
        'san francisco': {'CA': ['075']},  # San Francisco County
        'houston': {'TX': ['201']},  # Harris County
        'dallas': {'TX': ['113']},  # Dallas County
        'austin': {'TX': ['453']},  # Travis County
        'new york': {'NY': ['061', '047', '081', '005', '085']},  # NYC boroughs
        'chicago': {'IL': ['031']},  # Cook County
        'miami': {'FL': ['086']},  # Miami-Dade County
    }
    
    city_lower = city_name.lower()
    if city_lower in city_county_mapping:
        return city_county_mapping[city_lower].get(state_name, None)
    
    return None

def filter_census_data_by_city(census_df, city_gdf):
    """Filter census data to tracts that are likely within or near the city"""
    # Get city boundary
    city_geom = city_gdf.iloc[0].geometry
    minx, miny, maxx, maxy = city_geom.bounds
    
    # Method 1: Try to filter by county name if it's in the city string
    city_parts = CITY.split(',')
    if len(city_parts) > 1:
        # Try to find county name in census tract names
        # Many cities are named after their county or vice versa
        city_name = city_parts[0].strip().lower()
        
        # Look for city name or common county variations
        county_patterns = [
            city_name,
            f"{city_name} county",
            f"{city_name} co",
        ]
        
        for pattern in county_patterns:
            city_tracts = census_df[census_df['NAME'].str.lower().str.contains(pattern, na=False)]
            if len(city_tracts) > 0:
                print(f"Found {len(city_tracts)} census tracts containing '{pattern}' in name")
                return city_tracts
    
    # Method 2: If no county match, filter by geographic proximity (rough approximation)
    # Create a buffer around the city to catch nearby tracts
    buffer_size = 0.1  # degrees (roughly 11km)
    extended_bounds = (minx - buffer_size, miny - buffer_size, 
                      maxx + buffer_size, maxy + buffer_size)
    
    # This is a very rough approximation since we don't have tract coordinates
    # We'll just take a reasonable sample of tracts from the state
    print(f"No tracts found by county name matching city '{city_parts[0]}', using geographic sampling")
    
    # Take tracts from middle portion of the sorted list (by tract number)
    # This often corresponds to more central/urban areas
    census_df_sorted = census_df.sort_values('tract')
    start_idx = len(census_df_sorted) // 4
    end_idx = 3 * len(census_df_sorted) // 4
    sample_size = min(100, end_idx - start_idx)  # Limit to 100 tracts max
    
    sampled_tracts = census_df_sorted.iloc[start_idx:start_idx + sample_size]
    print(f"Using sample of {len(sampled_tracts)} tracts from central portion of state")
    return sampled_tracts

def process_census_data_to_geodataframe(city_gdf, census_df):
    """Process census tract data into a GeoDataFrame with population points (excluding water areas)"""
    # Clean and prepare census data
    census_df['population'] = pd.to_numeric(census_df['B01003_001E'], errors='coerce').fillna(0)
    census_df = census_df[census_df['population'] > 0]  # Remove tracts with no population
    total_population = census_df['population'].sum()
    return generate_population_from_road_network(city_gdf, total_population)

def generate_population_from_road_network(city_gdf, total_population):
    """Fallback method: Generate population points based on road network density"""
    try:
        # Get road network
        city_geom = city_gdf.iloc[0].geometry
        G = ox.graph_from_polygon(city_geom, network_type='drive')
        nodes, edges = ox.graph_to_gdfs(G)
        
        # Sample nodes for population points
        num_points = min(POPULATION_POINTS, len(nodes))  # Reasonable number of points
        sampled_nodes = nodes.sample(num_points)
        
        # Distribute population among the points
        pop_per_point = int(total_population / num_points)
        
        pop_gdf = gpd.GeoDataFrame({
            'geometry': sampled_nodes.geometry,
            'population': [pop_per_point] * len(sampled_nodes)
        }, crs='EPSG:4326')
        
        print(f"Generated {len(pop_gdf)} population points from road network as fallback")
        return pop_gdf
        
    except Exception as e:
        print(f"Error generating population from road network: {e}")
        return generate_synthetic_population_data(city_gdf)

def get_existing_charging_stations(city_gdf):
    """Get existing EV charging stations from the NREL API for the specific city"""
    try:
        # Get the city geometry and its bounds
        city_geom = city_gdf.iloc[0].geometry
        minx, miny, maxx, maxy = city_geom.bounds
        
        print(f"City bounds: {minx:.6f}, {miny:.6f}, {maxx:.6f}, {maxy:.6f}")
        
        # Check if bounds are reasonable (not too large)
        lat_span = maxy - miny
        lon_span = maxx - minx
        
        if lat_span > 5 or lon_span > 5:  # If city spans more than 5 degrees, something's wrong
            print(f"Warning: City bounds seem too large (lat span: {lat_span:.2f}, lon span: {lon_span:.2f})")
            print("This might result in getting data for a very large area")
        
        # NREL Alternative Fuel Stations API
        url = "https://developer.nrel.gov/api/alt-fuel-stations/v1.json"
        params = {
            'api_key': NREL_API_KEY,
            'fuel_type': 'ELEC',  # Electric stations only
            'status': 'E',        # Existing stations
            'access': 'public',   # Public stations only
            'bbox': f"{miny},{minx},{maxy},{maxx}"  # Bounding box (lat,lng,lat,lng)
        }
        
        response = requests.get(url, params=params)
        data = response.json()
        
        if 'fuel_stations' in data:
            stations = data['fuel_stations']
            print(f"Retrieved {len(stations)} charging stations from NREL API within bounding box")
            
            # Convert to GeoDataFrame
            if stations:
                station_points = [Point(s['longitude'], s['latitude']) for s in stations]
                station_gdf = gpd.GeoDataFrame({
                    'geometry': station_points,
                    'name': [s.get('station_name', 'Unknown') for s in stations],
                    'address': [s.get('street_address', 'Unknown') for s in stations],
                    'ev_level': [(s.get('ev_level2_evse_num') or 0) + (s.get('ev_dc_fast_num') or 0) for s in stations]
                }, crs='EPSG:4326')
                
                # Filter stations to only those actually within the city boundary
                stations_in_city = station_gdf[station_gdf.geometry.within(city_geom)]
                
                print(f"Filtered to {len(stations_in_city)} stations actually within city boundary")
                
                # If no stations within exact boundary, use stations within a reasonable buffer
                if len(stations_in_city) == 0:
                    # Create a small buffer around the city (about 1km)
                    city_buffered = city_geom.buffer(0.01)  # roughly 1km buffer
                    stations_near_city = station_gdf[station_gdf.geometry.within(city_buffered)]
                    
                    if len(stations_near_city) > 0:
                        print(f"Using {len(stations_near_city)} stations within buffer of city")
                        return stations_near_city
                    else:
                        print("No stations found within city or nearby buffer")
                        return gpd.GeoDataFrame(geometry=[], crs='EPSG:4326')
                
                return stations_in_city
            else:
                print("No existing stations found in the area")
                return gpd.GeoDataFrame(geometry=[], crs='EPSG:4326')
        else:
            print("Error in NREL API response:", data)
            return gpd.GeoDataFrame(geometry=[], crs='EPSG:4326')
            
    except Exception as e:
        print(f"Error getting existing charging stations: {e}")
        # Generate a few synthetic stations for demonstration
        return generate_synthetic_charging_stations(city_gdf)

def validate_city_geometry(city_gdf):
    """Validate that the city geometry is reasonable"""
    if len(city_gdf) == 0:
        print("Warning: Empty city GeoDataFrame")
        return False
    
    city_geom = city_gdf.iloc[0].geometry
    minx, miny, maxx, maxy = city_geom.bounds
    
    # Check if coordinates are in a reasonable range for US cities
    if not (-180 <= minx <= 180 and -180 <= maxx <= 180):
        print(f"Warning: Longitude values seem out of range: {minx}, {maxx}")
        return False
    
    if not (-90 <= miny <= 90 and -90 <= maxy <= 90):
        print(f"Warning: Latitude values seem out of range: {miny}, {maxy}")
        return False
    
    # Check if the city area is reasonable (not too large)
    lat_span = maxy - miny
    lon_span = maxx - minx
    
    if lat_span > 2 or lon_span > 2:  # Cities shouldn't span more than 2 degrees
        print(f"Warning: City seems very large - lat span: {lat_span:.3f}°, lon span: {lon_span:.3f}°")
        return False
    
    print(f"City geometry validated - bounds: {minx:.6f}, {miny:.6f}, {maxx:.6f}, {maxy:.6f}")
    return True

def get_candidate_locations(road_nodes, existing_stations, city_gdf, num_candidates=NUM_CANDIDATE_LOCATIONS):
    """Generate candidate locations for new charging stations"""
    # Try to get land areas to avoid water bodies
    city_geom = city_gdf.iloc[0].geometry

    # Road networks inherently avoid water, so this is still better than random points
    nodes_filtered = road_nodes[road_nodes.within(city_geom)]
    print(f"Using all road nodes within city: {len(nodes_filtered)} nodes")
    
    # Create a GeoDataFrame of existing stations for spatial operations
    if len(existing_stations) > 0:
        # Convert to projected CRS for accurate distance calculations
        # Use UTM zone appropriate for the location (rough approximation)
        city_center = city_geom.centroid
        utm_crs = f"EPSG:{32600 + int((city_center.x + 180) / 6) + 1}"  # Rough UTM zone calculation
        
        try:
            # Project to UTM for accurate distance calculation
            existing_proj = existing_stations.to_crs(utm_crs)
            nodes_proj = nodes_filtered.to_crs(utm_crs)
            
            # Buffer existing stations by MIN_DISTANCE_BETWEEN_STATIONS (in meters)
            buffered_stations = existing_proj.copy()
            buffered_stations['geometry'] = buffered_stations.geometry.buffer(MIN_DISTANCE_BETWEEN_STATIONS)
            
            # Filter out nodes that are too close to existing stations
            candidate_nodes = nodes_proj[~nodes_proj.intersects(buffered_stations.unary_union)]
            
            # Convert back to original CRS
            candidate_nodes = candidate_nodes.to_crs(nodes_filtered.crs)
            
        except Exception as e:
            print(f"Error with CRS transformation, using degree-based approximation: {e}")
            # Fallback to degree-based buffer (less accurate)
            buffered_stations = existing_stations.copy()
            buffered_stations['geometry'] = buffered_stations.geometry.buffer(MIN_DISTANCE_BETWEEN_STATIONS / 111000)  # Rough conversion from meters to degrees
            
            # Filter out nodes that are too close to existing stations
            candidate_nodes = nodes_filtered[~nodes_filtered.intersects(buffered_stations.unary_union)]
    else:
        candidate_nodes = nodes_filtered
    
    # If we have too many candidates, sample randomly
    if len(candidate_nodes) > num_candidates:
        candidate_nodes = candidate_nodes.sample(num_candidates)
    
    # Add an ID field
    candidate_nodes = candidate_nodes.reset_index(drop=True)
    candidate_nodes['location_id'] = [f"L{i+1}" for i in range(len(candidate_nodes))]
    
    print(f"Generated {len(candidate_nodes)} candidate locations avoiding water areas")
    return candidate_nodes
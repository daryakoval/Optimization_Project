import requests
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pulp import *
import osmnx as ox
import census


from constants import CENSUS_API_KEY, CITY, MIN_DISTANCE_BETWEEN_STATIONS, NREL_API_KEY, NUM_CANDIDATE_LOCATIONS

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
        
        # Get the state code for the city
        state_name = CITY.split(',')[1].strip()
        state_fips = {
            'WA': '53', 'OR': '41', 'CA': '06', 'TX': '48'
        }.get(state_name, '53')  # default to WA
        
        # Get all census tract data for the state (we'll filter by geography later)
        census_data = c.acs5.state_county_tract(
            fields=('NAME', 'B01003_001E', 'B25001_001E'),  # Population and housing units
            state_fips=state_fips,
            county_fips='*',
            tract='*',
            year=2019
        )
        
        # Convert to DataFrame
        census_df = pd.DataFrame(census_data)
        print(f"Retrieved census data for {len(census_df)} tracts in state")
        
        # Filter census tracts to only those that might intersect with our city
        # This is a rough approximation - ideally you'd use census tract shapefiles
        filtered_census = filter_census_data_by_city(census_df, city_gdf)
        
        if len(filtered_census) == 0:
            print("No census tracts found near city boundary. Using synthetic data.")
            return generate_synthetic_population_data(city_gdf)
        
        # Process the filtered census data to create population points
        return process_census_data_to_geodataframe(city_gdf, filtered_census)
        
    except Exception as e:
        print(f"Error getting census data: {e}")
        return generate_synthetic_population_data(city_gdf)

def filter_census_data_by_city(census_df, city_gdf):
    """Filter census data to tracts that are likely within or near the city"""
    # This is a simplified approach since we don't have tract shapefiles
    # In practice, you'd spatially join with actual census tract boundaries
    
    # For now, we'll just take a reasonable sample based on city name
    city_name = CITY.split(',')[0].strip().lower()
    
    # Filter tracts that mention the city name in their NAME field
    city_tracts = census_df[census_df['NAME'].str.lower().str.contains(city_name, na=False)]
    
    if len(city_tracts) > 0:
        print(f"Found {len(city_tracts)} census tracts containing '{city_name}' in name")
        return city_tracts
    
    # If no tracts found by name, take a random sample to avoid processing entire state
    sample_size = min(50, len(census_df))  # Limit to 50 tracts max
    sampled_tracts = census_df.sample(n=sample_size, random_state=42)
    print(f"No tracts found by city name, using random sample of {len(sampled_tracts)} tracts")
    return sampled_tracts

def process_census_data_to_geodataframe(city_gdf, census_df):
    """Process census tract data into a GeoDataFrame with population points"""
    try:
        # Clean and prepare census data
        census_df['population'] = pd.to_numeric(census_df['B01003_001E'], errors='coerce').fillna(0)
        census_df = census_df[census_df['population'] > 0]  # Remove tracts with no population
        
        # Get city boundary
        city_geom = city_gdf.iloc[0].geometry
        minx, miny, maxx, maxy = city_geom.bounds
        
        # For demonstration, we'll create points distributed based on census tract populations
        # In a real implementation, you'd need census tract shapefiles to get exact boundaries
        points = []
        populations = []
        
        # Calculate total population for weighting
        total_population = census_df['population'].sum()
        
        # Create points distributed across the city, weighted by population density
        for _, tract in census_df.iterrows():
            tract_pop = tract['population']
            
            # Number of points for this tract based on its population proportion
            num_points = max(1, int((tract_pop / total_population) * 100))  # Scale to reasonable number of points
            
            # Generate random points within city boundary for this tract
            for _ in range(num_points):
                # Generate random point within city bounds
                attempts = 0
                while attempts < 50:  # Prevent infinite loop
                    x = np.random.uniform(minx, maxx)
                    y = np.random.uniform(miny, maxy)
                    point = Point(x, y)
                    
                    if point.within(city_geom):
                        points.append(point)
                        # Distribute population among points for this tract
                        populations.append(int(tract_pop / num_points))
                        break
                    attempts += 1
        
        if not points:
            print("No valid points generated from census data. Using synthetic data.")
            return generate_synthetic_population_data(city_gdf)
        
        # Create GeoDataFrame
        pop_gdf = gpd.GeoDataFrame({
            'geometry': points,
            'population': populations
        }, crs='EPSG:4326')
        
        print(f"Generated population data from census with {len(pop_gdf)} points, total population: {sum(populations):,}")
        return pop_gdf
        
    except Exception as e:
        print(f"Error processing census data: {e}")
        return generate_synthetic_population_data(city_gdf)

def generate_synthetic_population_data(city_gdf, census_df=None):
    """Generate synthetic population density data for demonstration"""
    # Get city boundary
    city_geom = city_gdf.iloc[0].geometry
    
    # Create a grid of points across the city
    minx, miny, maxx, maxy = city_geom.bounds
    x_coords = np.linspace(minx, maxx, 20)
    y_coords = np.linspace(miny, maxy, 20)
    
    points = []
    population = []
    
    # If we have census data, use it to inform our synthetic generation
    if census_df is not None:
        # Calculate average population from census data
        census_df['population'] = pd.to_numeric(census_df['B01003_001E'], errors='coerce').fillna(0)
        avg_pop = census_df['population'].mean()
        std_pop = census_df['population'].std()
        print(f"Using census statistics: avg={avg_pop:.0f}, std={std_pop:.0f}")
    else:
        avg_pop = 5000
        std_pop = 1000
    
    for x in x_coords:
        for y in y_coords:
            point = Point(x, y)
            if point.within(city_geom):
                points.append(point)
                # Generate population that's higher in the center, lower at edges
                dist_to_center = point.distance(Point((minx + maxx) / 2, (miny + maxy) / 2))
                max_dist = point.distance(Point(minx, miny))
                
                # Use census-informed population generation
                center_weight = (1 - dist_to_center / max_dist)
                pop = int(np.random.normal(avg_pop * center_weight, std_pop))
                population.append(max(100, pop))  # Ensure minimum population
    
    # Create GeoDataFrame
    pop_gdf = gpd.GeoDataFrame({
        'geometry': points,
        'population': population
    }, crs='EPSG:4326')
    
    total_pop = sum(population)
    data_source = "census-informed synthetic" if census_df is not None else "synthetic"
    print(f"Generated {data_source} population data with {len(pop_gdf)} points, total population: {total_pop:,}")
    return pop_gdf

def get_existing_charging_stations(city_gdf):
    """Get existing EV charging stations from the NREL API"""
    try:
        # Get the bounding box for the API request
        minx, miny, maxx, maxy = city_gdf.iloc[0].geometry.bounds
        
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
            print(f"Retrieved {len(stations)} existing charging stations from NREL API")
            
            # Convert to GeoDataFrame
            if stations:
                station_points = [Point(s['longitude'], s['latitude']) for s in stations]
                station_gdf = gpd.GeoDataFrame({
                    'geometry': station_points,
                    'name': [s.get('station_name', 'Unknown') for s in stations],
                    'address': [s.get('street_address', 'Unknown') for s in stations],
                    'ev_level': [(s.get('ev_level2_evse_num') or 0) + (s.get('ev_dc_fast_num') or 0) for s in stations]
                }, crs='EPSG:4326')
                
                return station_gdf
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

def generate_synthetic_charging_stations(city_gdf):
    """Generate synthetic charging station data for demonstration"""
    # Get city boundary
    city_geom = city_gdf.iloc[0].geometry
    
    # Create some random points within the city
    minx, miny, maxx, maxy = city_geom.bounds
    
    points = []
    names = []
    addresses = []
    levels = []
    
    # Generate 10-20 random stations
    num_stations = np.random.randint(10, 21)
    
    for i in range(num_stations):
        while True:
            x = np.random.uniform(minx, maxx)
            y = np.random.uniform(miny, maxy)
            point = Point(x, y)
            if point.within(city_geom):
                points.append(point)
                names.append(f"Charging Station {i+1}")
                addresses.append(f"{np.random.randint(100, 9999)} Example St")
                levels.append(np.random.randint(1, 5))
                break
    
    # Create GeoDataFrame
    stations_gdf = gpd.GeoDataFrame({
        'geometry': points,
        'name': names,
        'address': addresses,
        'ev_level': levels
    }, crs='EPSG:4326')
    
    print(f"Generated {len(stations_gdf)} synthetic charging stations")
    return stations_gdf

def get_candidate_locations(road_nodes, existing_stations, city_gdf, num_candidates=NUM_CANDIDATE_LOCATIONS):
    """Generate candidate locations for new charging stations"""
    # Filter nodes to those within the city
    city_geom = city_gdf.iloc[0].geometry
    nodes_in_city = road_nodes[road_nodes.within(city_geom)]
    
    # Create a GeoDataFrame of existing stations for spatial operations
    if len(existing_stations) > 0:
        # Buffer existing stations by MIN_DISTANCE_BETWEEN_STATIONS
        buffered_stations = existing_stations.copy()
        buffered_stations['geometry'] = buffered_stations.geometry.buffer(MIN_DISTANCE_BETWEEN_STATIONS / 111000)  # Rough conversion from meters to degrees
        
        # Filter out nodes that are too close to existing stations
        candidate_nodes = nodes_in_city[~nodes_in_city.intersects(buffered_stations.unary_union)]
    else:
        candidate_nodes = nodes_in_city
    
    # If we have too many candidates, sample randomly
    if len(candidate_nodes) > num_candidates:
        candidate_nodes = candidate_nodes.sample(num_candidates)
    
    # Add an ID field
    candidate_nodes['location_id'] = [f"L{i+1}" for i in range(len(candidate_nodes))]
    
    print(f"Generated {len(candidate_nodes)} candidate locations")
    return candidate_nodes

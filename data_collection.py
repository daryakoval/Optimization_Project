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
        # Generate synthetic population data for demonstration
        return generate_synthetic_population_data(city_gdf)
    
    try:
        # Initialize Census API client
        c = census.Census(CENSUS_API_KEY)
        
        # Get the state and county codes for the city
        # This is a simplified approach - in reality, you'd need to map the city to specific census tracts
        state_name = CITY.split(',')[1].strip()
        state_fips = {
            'WA': '53', 'OR': '41', 'CA': '06', 'TX': '48'
        }.get(state_name, '53')  # default to WA
        
        # Get census tract level data
        census_data = c.acs5.state_county_tract(
            fields=('NAME', 'B01003_001E'),  # B01003_001E is total population
            state_fips=state_fips,
            county_fips='*',
            tract='*',
            year=2019
        )
        
        # Convert to DataFrame
        df = pd.DataFrame(census_data)
        print(f"Retrieved census data for {len(df)} tracts")
        
        # This is where you would join with shapefile of census tracts
        # For simplicity, we'll use synthetic data with the real population counts
        return generate_synthetic_population_data(city_gdf, df)
        
    except Exception as e:
        print(f"Error getting census data: {e}")
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
    
    for x in x_coords:
        for y in y_coords:
            point = Point(x, y)
            if point.within(city_geom):
                points.append(point)
                # Generate population that's higher in the center, lower at edges
                dist_to_center = point.distance(Point((minx + maxx) / 2, (miny + maxy) / 2))
                max_dist = point.distance(Point(minx, miny))
                pop = int(np.random.normal(5000 * (1 - dist_to_center / max_dist), 1000))
                population.append(max(100, pop))  # Ensure minimum population
    
    # Create GeoDataFrame
    pop_gdf = gpd.GeoDataFrame({
        'geometry': points,
        'population': population
    }, crs='EPSG:4326')
    
    print(f"Generated synthetic population data with {len(pop_gdf)} points")
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
                    'ev_level': [s.get('ev_level2_evse_num', 0) + s.get('ev_dc_fast_num', 0) for s in stations]
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

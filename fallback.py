import requests
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from pulp import *
import osmnx as ox
import census


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


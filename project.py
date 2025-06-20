"""
Electric Vehicle Charging Station Placement using MILP
======================================================

This program determines the optimal locations for new EV charging stations 
in a city to maximize population coverage while minimizing costs.

Data Sources:
- OpenStreetMap API: Road network data
- US Census API: Population density data 
- NREL API: Existing charging station locations
- OpenChargeMap API: Current charging infrastructure

"""
import random

import numpy as np
from constants import CITY, MAX_BUDGET, BASE_STATION_COST, SEED
from data_collection import get_candidate_locations, get_city_boundary, get_existing_charging_stations, get_population_data, get_road_network
from data_prep import prepare_coverage_matrix
from milp import optimize_charging_station_locations
from vizualization import create_interactive_map, visualize_results

random.seed(SEED)
np.random.seed(SEED)

def main():
    """Main execution function"""
    print(f"Starting EV charging station optimization for {CITY}")
    
    print("\n=== COLLECTING DATA ===")
    city_gdf = get_city_boundary(CITY)
    road_nodes, road_edges = get_road_network(city_gdf)
    population_gdf = get_population_data(city_gdf)
    existing_stations_gdf = get_existing_charging_stations(city_gdf)
    
    print("\n=== GENERATING CANDIDATE LOCATIONS ===")
    candidate_locations_gdf = get_candidate_locations(road_nodes, existing_stations_gdf, city_gdf)
    
    print("\n=== PREPARING DATA FOR OPTIMIZATION ===")
    coverage_df = prepare_coverage_matrix(population_gdf, candidate_locations_gdf)
    
    print("\n=== RUNNING OPTIMIZATION ===")
    selected_locations_gdf, covered_population, total_population, actual_total_cost = optimize_charging_station_locations(
        coverage_df, candidate_locations_gdf, MAX_BUDGET, BASE_STATION_COST, population_gdf
    )
    
    print("\n=== CREATING VISUALIZATIONS ===")
    visualize_results(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf)
    interactive_map = create_interactive_map(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf)
    
    print("\n=== OPTIMIZATION COMPLETE ===")
    print(f"Results: Selected {len(selected_locations_gdf)} new charging station locations")
    print(f"Population coverage: {covered_population:.0f} out of {total_population:.0f} ({covered_population/total_population*100:.2f}%)")
    print(f"Total cost: ${actual_total_cost:,}")  # Now uses actual variable costs
    
    return {
        'city_gdf': city_gdf,
        'population_gdf': population_gdf,
        'existing_stations_gdf': existing_stations_gdf,
        'candidate_locations_gdf': candidate_locations_gdf,
        'selected_locations_gdf': selected_locations_gdf,
        'covered_population': covered_population,
        'total_population': total_population,
        'coverage_percentage': covered_population/total_population*100,
        'actual_total_cost': actual_total_cost
    }

if __name__ == "__main__":
    results = main()
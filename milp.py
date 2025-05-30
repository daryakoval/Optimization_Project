from pulp import *
import random
import pandas as pd

from constants import SEED


# =============================================================================
# STEP 3: MILP FORMULATION AND SOLUTION - FIXED VERSION
# =============================================================================

def optimize_charging_station_locations(coverage_df, candidate_locations, max_budget, station_cost, population_gdf):
    """Use MILP to optimize charging station placement
    
    FIXED VERSION: Properly tracks coverage and aligns results with population data
    """
    print("\n=== STARTING MILP OPTIMIZATION ===")
    
    # Create a new MILP problem
    prob = LpProblem("EV_Charging_Station_Placement", LpMaximize)
    
    # Get list of population points and candidate locations
    population_points = coverage_df.index.tolist()
    locations = [col for col in coverage_df.columns if col != 'population']
    
    print(f"Population points: {len(population_points)}")
    print(f"Candidate locations: {len(locations)}")
    print(f"Total population: {coverage_df['population'].sum():,.0f}")
    
    # =============================================================================
    # VARIABLE COSTS
    # =============================================================================
    
    # Variable station costs (based on location characteristics)
    random.seed(SEED)  # For reproducible results
    station_costs = {}
    for loc in locations:
        # Vary costs between 80% to 150% of base cost
        cost_multiplier = random.uniform(0.8, 1.5)
        station_costs[loc] = int(station_cost * cost_multiplier)
    
    print(f"Station costs range: ${min(station_costs.values()):,} - ${max(station_costs.values()):,}")
    
    # =============================================================================
    # DECISION VARIABLES
    # =============================================================================
    
    # Binary variable indicating if a location is selected for a charging station
    location_vars = LpVariable.dicts("Location", locations, cat=LpBinary)
    
    # Binary variable indicating if a population point is covered
    coverage_vars = LpVariable.dicts("Coverage", population_points, cat=LpBinary)
    
    # =============================================================================
    # OBJECTIVE AND CONSTRAINTS
    # =============================================================================
    
    # Objective: Maximize total population covered
    prob += lpSum([coverage_vars[p] * coverage_df.loc[p, 'population'] for p in population_points])
    
    # Constraint 1: Budget constraint (now with variable costs)
    prob += lpSum([location_vars[l] * station_costs[l] for l in locations]) <= max_budget
    
    # Constraint 2: Coverage constraint - a population point is covered if at least one station covers it
    coverage_constraints_added = 0
    for p in population_points:
        # Get the locations that cover this population point
        covering_locations = [l for l in locations if coverage_df.loc[p, l] == 1]
        
        # A point is covered if at least one covering location has a station
        if covering_locations:  # Only add constraint if there are covering locations
            prob += coverage_vars[p] <= lpSum([location_vars[l] for l in covering_locations])
            coverage_constraints_added += 1
        else:
            # If no locations can cover this point, force coverage to 0
            prob += coverage_vars[p] == 0
    
    print(f"Added {coverage_constraints_added} coverage constraints")
    
    # Solve the problem
    print("Solving MILP problem...")
    prob.solve(PULP_CBC_CMD(msg=True))  # Set msg=True for detailed solver output
    
    print(f"Optimization Status: {LpStatus[prob.status]}")
    
    if LpStatus[prob.status] != 'Optimal':
        print("WARNING: Optimization did not find optimal solution!")
        return candidate_locations.iloc[:0], 0, coverage_df['population'].sum(), 0
    
    # =============================================================================
    # EXTRACT AND VALIDATE RESULTS
    # =============================================================================
    
    # Extract selected locations and calculate actual coverage
    selected_locations = []
    total_cost = 0
    
    for l in locations:
        if location_vars[l].value() == 1:
            selected_locations.append(l)
            total_cost += station_costs[l]
    
    print(f"Selected {len(selected_locations)} locations: {selected_locations}")
    
    # Calculate coverage based on optimization results
    covered_population = 0
    coverage_results = {}
    
    for p in population_points:
        is_covered = bool(coverage_vars[p].value())
        coverage_results[p] = is_covered
        if is_covered:
            covered_population += coverage_df.loc[p, 'population']
    
    total_population = coverage_df['population'].sum()
    coverage_percentage = covered_population / total_population * 100
    
    # =============================================================================
    # DETAILED STATION ANALYSIS
    # =============================================================================
    
    print(f"\n=== DETAILED STATION ANALYSIS ===")
    for location_id in selected_locations:
        station_cost_value = station_costs[location_id]
        
        # Find which population points this station covers
        covered_points = []
        total_pop_covered_by_station = 0
        
        for p in population_points:
            if coverage_df.loc[p, location_id] == 1 and coverage_results[p]:
                covered_points.append(p)
                total_pop_covered_by_station += coverage_df.loc[p, 'population']
        
        print(f"\nStation {location_id}:")
        print(f"  Cost: ${station_cost_value:,}")
        print(f"  Covers {len(covered_points)} population points")
        print(f"  Total population covered: {total_pop_covered_by_station:,}")
        print(f"  Population points covered: {covered_points}")
    
    # =============================================================================
    # DETAILED COVERAGE ANALYSIS
    # =============================================================================
    
    print(f"\n=== POPULATION COVERAGE ANALYSIS ===")
    covered_points_list = []
    uncovered_points_list = []
    
    for p in population_points:
        pop_size = coverage_df.loc[p, 'population']
        if coverage_results[p]:
            covered_points_list.append((p, pop_size))
        else:
            uncovered_points_list.append((p, pop_size))
    
    # print(f"\nCovered population points ({len(covered_points_list)}):")
    # for point_id, pop_size in sorted(covered_points_list, key=lambda x: x[1], reverse=True):  # Sort by population size
    #     print(f"  Point {point_id}: {pop_size:,} people")
    
    # print(f"\nUncovered population points ({len(uncovered_points_list)}):")
    # for point_id, pop_size in sorted(uncovered_points_list, key=lambda x: x[1], reverse=True):  # Sort by population size
    #     print(f"  Point {point_id}: {pop_size:,} people")
    
    # =============================================================================
    # CREATE DETAILED COVERAGE MAPPING
    # =============================================================================
    
    # Create a detailed mapping between population points and their coverage
    population_coverage_map = create_population_coverage_mapping(
        coverage_df, selected_locations, population_gdf
    )
    
    # =============================================================================
    # RESULTS SUMMARY
    # =============================================================================
    
    print(f"\n=== OPTIMIZATION RESULTS ===")
    print(f"Total budget: ${max_budget:,}")
    print(f"Used budget: ${total_cost:,}")
    print(f"Selected {len(selected_locations)} locations")
    print(f"Covered population: {covered_population:,.0f} out of {total_population:,.0f} ({coverage_percentage:.2f}%)")
    
    # Validate results with manual calculation
    print(f"\n=== COVERAGE VALIDATION ===")
    manual_coverage = validate_coverage_calculation(coverage_df, selected_locations)
    print(f"Manual coverage calculation: {manual_coverage['covered_population']:,.0f} ({manual_coverage['coverage_percentage']:.2f}%)")
    
    if abs(manual_coverage['coverage_percentage'] - coverage_percentage) > 0.1:
        print("WARNING: Coverage calculation mismatch detected!")
    
    # Get the GeoDataFrame of selected locations and add cost information
    selected_gdf = candidate_locations[candidate_locations['location_id'].isin(selected_locations)].copy()
    
    # Add cost information to the GeoDataFrame
    selected_gdf['station_cost'] = selected_gdf['location_id'].map(station_costs)
    
    return selected_gdf, covered_population, total_population, total_cost


def create_population_coverage_mapping(coverage_df, selected_locations, population_gdf):
    """Create a detailed mapping of which population points are covered"""
    print("Creating detailed population coverage mapping...")
    
    population_points = coverage_df.index.tolist()
    
    # Create coverage mapping
    coverage_mapping = []
    for i, p in enumerate(population_points):
        # Check if this population point is covered by any selected location
        is_covered = False
        covering_stations = []
        
        for loc in selected_locations:
            if coverage_df.loc[p, loc] == 1:
                is_covered = True
                covering_stations.append(loc)
        
        coverage_mapping.append({
            'population_point_id': p,
            'population_index': i,
            'population': coverage_df.loc[p, 'population'],
            'is_covered': is_covered,
            'covering_stations': covering_stations,
            'num_covering_stations': len(covering_stations)
        })
    
    coverage_df_detailed = pd.DataFrame(coverage_mapping)
    
    # Summary statistics
    total_covered = coverage_df_detailed['is_covered'].sum()
    total_points = len(coverage_df_detailed)
    covered_pop = coverage_df_detailed[coverage_df_detailed['is_covered']]['population'].sum()
    total_pop = coverage_df_detailed['population'].sum()
    
    print(f"Coverage mapping complete:")
    print(f"  - Points covered: {total_covered}/{total_points} ({total_covered/total_points*100:.1f}%)")
    print(f"  - Population covered: {covered_pop:,.0f}/{total_pop:,.0f} ({covered_pop/total_pop*100:.1f}%)")
    
    return coverage_df_detailed


def validate_coverage_calculation(coverage_df, selected_locations):
    """Manually validate the coverage calculation"""
    population_points = coverage_df.index.tolist()
    
    covered_population = 0
    covered_points = 0
    
    for p in population_points:
        # Check if this point is covered by any selected location
        is_covered = False
        for loc in selected_locations:
            if coverage_df.loc[p, loc] == 1:
                is_covered = True
                break
        
        if is_covered:
            covered_points += 1
            covered_population += coverage_df.loc[p, 'population']
    
    total_population = coverage_df['population'].sum()
    coverage_percentage = covered_population / total_population * 100
    
    return {
        'covered_points': covered_points,
        'total_points': len(population_points),
        'covered_population': covered_population,
        'total_population': total_population,
        'coverage_percentage': coverage_percentage
    }
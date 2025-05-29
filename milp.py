from pulp import *
import random


# =============================================================================
# STEP 3: MILP FORMULATION AND SOLUTION
# =============================================================================

def optimize_charging_station_locations(coverage_df, candidate_locations, max_budget, station_cost):
    """Use MILP to optimize charging station placement"""
    # Create a new MILP problem
    prob = LpProblem("EV_Charging_Station_Placement", LpMaximize)
    
    # Get list of population points and candidate locations
    population_points = coverage_df.index.tolist()
    locations = [col for col in coverage_df.columns if col != 'population']
    
    # =============================================================================
    # VARIABLE COSTS
    # =============================================================================
    
    # Variable station costs (based on location characteristics)
    random.seed(42)  # For reproducible results
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
    for p in population_points:
        # Get the locations that cover this population point
        covering_locations = [l for l in locations if coverage_df.loc[p, l] == 1]
        
        # A point is covered if at least one covering location has a station
        if covering_locations:  # Only add constraint if there are covering locations
            prob += coverage_vars[p] <= lpSum([location_vars[l] for l in covering_locations])
    
    # Constraint 3: Minimum distance between stations
    # This is implicitly handled by our candidate location generation
    
    # Solve the problem
    print("Solving MILP problem...")
    prob.solve(PULP_CBC_CMD(msg=True))
    
    print(f"Status: {LpStatus[prob.status]}")
    
    # Extract results
    selected_locations = []
    total_cost = 0
    
    for l in locations:
        if location_vars[l].value() == 1:
            selected_locations.append(l)
            total_cost += station_costs[l]
    
    covered_population = sum(coverage_vars[p].value() * coverage_df.loc[p, 'population'] for p in population_points)
    total_population = sum(coverage_df['population'])
    coverage_percentage = covered_population / total_population * 100
    
    print(f"Total budget: ${max_budget}")
    print(f"Used budget: ${total_cost}")
    print(f"Selected {len(selected_locations)} locations")
    print(f"Covered population: {covered_population} out of {total_population} ({coverage_percentage:.2f}%)")
    
    # Get the GeoDataFrame of selected locations
    selected_gdf = candidate_locations[candidate_locations['location_id'].isin(selected_locations)]
    
    return selected_gdf, covered_population, total_population
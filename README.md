# Electric Vehicle Charging Station Placement using MILP

## Overview

**Integer or Mixed Integer Linear Programming (MILP) – Branch and Bound Method Electric Vehicle Charging Station Placement**

**Problem**: Determine optimal locations for Electric Vehicle charging stations across a city to maximize coverage while minimizing costs.

## Data Sources

### Real Data Sources

* **US Census API**: https://api.census.gov/data/key_signup.html
  * Population density data
  * Demand Estimation: Population density directly correlates with potential Electric Vehicle adoption and charging needs
  * Helps ensure equitable access across different neighborhoods

* **NREL API**: https://developer.nrel.gov/signup/
  * Existing charging station locations

## Configuration Parameters

You can modify these parameters in the code:

* `CITY`: The city to analyze
* `MAX_BUDGET`: Maximum budget for new stations
* `BASE_STATION_COST`: Cost per station
* `MAX_COVERAGE_DISTANCE`: Maximum distance in meters for a station to cover a population point
* `MIN_DISTANCE_BETWEEN_STATIONS`: Minimum distance between any two stations
* `NUM_CANDIDATE_LOCATIONS`: Number of candidate locations to consider

## MILP Formulation

### Key MILP Components

* Binary decision variables for potential locations (x_i)
* Coverage constraints ensuring population access
* Budget constraints
* Distance requirements between stations

### Decision Variables

1. **Binary Location Variables (location_vars)**:
   * For each candidate location j, we define a binary variable x_j
   * x_j = 1 if we place a charging station at location j, and 0 otherwise

2. **Binary Coverage Variables (coverage_vars)**:
   * For each population point i, we define a binary variable y_i
   * y_i = 1 if population point i is covered by at least one charging station, and 0 otherwise

### Objective Function

Maximize the total population covered:

```
Maximize ∑(i∈P) y_i · population_i
```

Where:
* P is the set of all population points
* population_i is the population at point i
* y_i is the binary coverage variable for point i

### Constraints

#### 1. Budget Constraint

We can't spend more than our maximum budget:

```
∑(j∈L) x_j · cost_j ≤ MAX_BUDGET
```

Where:
* L is the set of all candidate locations
* cost_j is the cost of placing a station at location j (cost_j is the cost of placing a station at location j (each station location has a different cost ranging from 80% to 150% of the BASE_STATION_COST in our code))
* x_j is the binary decision variable for location j

#### 2. Coverage Constraint

A population point is covered if at least one station within the coverage distance is selected:

```
y_i ≤ ∑(j∈C_i) x_j ∀i∈P
```

Where:
* C_i is the set of candidate locations that can cover population point i
* This constraint ensures that y_i can only be 1 if at least one covering location has a station

#### 3. Distance Between Stations Constraint

We will handle this constraint during the candidate location generation phase, where we filter out locations that are too close to existing stations. This simplifies the MILP formulation.

## Interpreting the Results

The solution gives us:

1. The set of optimal locations for new charging stations (x_i)
2. The total population covered (y_i)
3. The total cost used from our budget

This solution maximizes the population coverage while respecting our budget constraint and ensuring charging stations are properly distributed.
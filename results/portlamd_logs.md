SEED = 35 
CITY = "Portland, OR, USA"
POPULATION_POINTS = 200
MAX_BUDGET = 1000000  # $1M budget for new stations
BASE_STATION_COST = 100000  # Cost per station
MAX_COVERAGE_DISTANCE = 1000  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters
NUM_CANDIDATE_LOCATIONS = 50


Starting EV charging station optimization for Portland, OR, USA

=== COLLECTING DATA ===
Retrieved 20038 road network nodes and 56680 edges
Getting census data for specific counties: ['051']
Retrieved census data for 171 tracts
Generated 200 population points from road network as fallback
City bounds: -122.836749, 45.432536, -122.472025, 45.652881
Retrieved 72812 charging stations from NREL API within bounding box
Filtered to 189 stations actually within city boundary

=== GENERATING CANDIDATE LOCATIONS ===
Using all road nodes within city: 20034 nodes
Generated 50 candidate locations avoiding water areas

=== PREPARING DATA FOR OPTIMIZATION ===
Preparing coverage matrix with visualization-consistent method...

  0%|          | 0/50 [00:00<?, ?it/s]
 14%|#4        | 7/50 [00:00<00:00, 65.31it/s]
 28%|##8       | 14/50 [00:00<00:00, 64.83it/s]
 42%|####2     | 21/50 [00:00<00:00, 62.83it/s]
 58%|#####8    | 29/50 [00:00<00:00, 66.15it/s]
 72%|#######2  | 36/50 [00:00<00:00, 67.02it/s]
 88%|########8 | 44/50 [00:00<00:00, 68.95it/s]
100%|##########| 50/50 [00:00<00:00, 67.55it/s]
Coverage matrix: (200, 51) - should now match visualization!

=== RUNNING OPTIMIZATION ===

=== STARTING MILP OPTIMIZATION ===
Population points: 200
Candidate locations: 50
Total population: 804,600
Station costs range: $80,789 - $148,072
Added 50 coverage constraints
Solving MILP problem...
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - C:\Users\Darya\AppData\Local\Programs\Python\Python311\Lib\site-packages\pulp\apis\../solverdir/cbc/win/i64/cbc.exe C:\Users\Darya\AppData\Local\Temp\f5536ff025e94941a658557ef16169fb-pulp.mps -max -timeMode elapsed -branch -printingOptions all -solution C:\Users\Darya\AppData\Local\Temp\f5536ff025e94941a658557ef16169fb-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 206 COLUMNS
At line 1212 RHS
At line 1414 BOUNDS
At line 1665 ENDATA
Problem MODEL has 201 rows, 250 columns and 305 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 103291 - 0.00 seconds
Cgl0002I 150 variables fixed
Cgl0004I processed model has 6 rows, 38 columns (38 integer (38 of which binary)) and 48 elements
Cbc0038I Initial state - 2 integers unsatisfied sum - 0.324964
Cbc0038I Pass   1: suminf.    0.13895 (1) obj. -100685 iterations 3
Cbc0038I Solution found of -76437
Cbc0038I Rounding solution of -80460 is better than previous of -76437

Cbc0038I Before mini branch and bound, 35 integers at bound fixed and 0 continuous
Cbc0038I Full problem 6 rows 38 columns, reduced to 1 rows 2 columns
Cbc0038I Mini branch and bound improved solution from -80460 to -96552 (0.01 seconds)
Cbc0038I Round again with cutoff of -97225.9
Cbc0038I Reduced cost fixing fixed 2 variables on major pass 2
Cbc0038I Pass   2: suminf.    0.14863 (1) obj. -102804 iterations 1
Cbc0038I Pass   3: suminf.    0.38917 (1) obj. -97225.9 iterations 3
Cbc0038I Pass   4: suminf.    0.79607 (3) obj. -97225.9 iterations 7
Cbc0038I Pass   5: suminf.    0.38917 (1) obj. -97225.9 iterations 3
Cbc0038I Pass   6: suminf.    0.46488 (1) obj. -98139.7 iterations 3
Cbc0038I Pass   7: suminf.    0.40645 (2) obj. -97225.9 iterations 5
Cbc0038I Pass   8: suminf.    0.08375 (1) obj. -97225.9 iterations 6
Cbc0038I Pass   9: suminf.    0.27262 (1) obj. -98745.5 iterations 3
Cbc0038I Pass  10: suminf.    0.83250 (3) obj. -97225.9 iterations 10
Cbc0038I Pass  11: suminf.    0.35651 (2) obj. -97225.9 iterations 5
Cbc0038I Pass  12: suminf.    0.41625 (1) obj. -97225.9 iterations 5
Cbc0038I Pass  13: suminf.    0.35590 (1) obj. -97711.5 iterations 4
Cbc0038I Pass  14: suminf.    0.41625 (1) obj. -97225.9 iterations 4
Cbc0038I Pass  15: suminf.    0.73238 (2) obj. -97225.9 iterations 7
Cbc0038I Pass  16: suminf.    0.73238 (2) obj. -97225.9 iterations 1
Cbc0038I Pass  17: suminf.    0.05368 (1) obj. -99927.1 iterations 5
Cbc0038I Pass  18: suminf.    0.27750 (1) obj. -97225.9 iterations 3
Cbc0038I Pass  19: suminf.    0.48974 (2) obj. -97225.9 iterations 8
Cbc0038I Pass  20: suminf.    0.33551 (2) obj. -97225.9 iterations 3
Cbc0038I Pass  21: suminf.    0.41625 (1) obj. -97225.9 iterations 4
Cbc0038I Pass  22: suminf.    0.36790 (1) obj. -97614.9 iterations 3
Cbc0038I Pass  23: suminf.    0.41625 (1) obj. -97225.9 iterations 3
Cbc0038I Pass  24: suminf.    1.22939 (4) obj. -97225.9 iterations 7
Cbc0038I Pass  25: suminf.    1.22939 (4) obj. -97225.9 iterations 0
Cbc0038I Pass  26: suminf.    0.00405 (1) obj. -100526 iterations 5
Cbc0038I Pass  27: suminf.    0.27750 (1) obj. -97225.9 iterations 1
Cbc0038I Pass  28: suminf.    0.71097 (3) obj. -97225.9 iterations 12
Cbc0038I Pass  29: suminf.    0.35777 (2) obj. -97225.9 iterations 4
Cbc0038I Pass  30: suminf.    0.41625 (1) obj. -97225.9 iterations 4
Cbc0038I Pass  31: suminf.    0.38739 (1) obj. -97458.1 iterations 2
Cbc0038I Before mini branch and bound, 19 integers at bound fixed and 0 continuous
Cbc0038I Full problem 6 rows 38 columns, reduced to 2 rows 16 columns
Cbc0038I Mini branch and bound improved solution from -96552 to -100575 (0.01 seconds)
Cbc0038I Round again with cutoff of -101118
Cbc0038I Reduced cost fixing fixed 19 variables on major pass 3
Cbc0038I Pass  31: suminf.    0.18432 (1) obj. -103115 iterations 1
Cbc0038I Pass  32: suminf.    0.43250 (1) obj. -101118 iterations 4
Cbc0038I Pass  33: suminf.    0.33900 (1) obj. -101870 iterations 3
Cbc0038I Pass  34: suminf.    0.58399 (2) obj. -101118 iterations 7
Cbc0038I Pass  35: suminf.    0.42133 (1) obj. -101208 iterations 5
Cbc0038I Pass  36: suminf.    0.43250 (1) obj. -101118 iterations 2
Cbc0038I Pass  37: suminf.    0.43250 (1) obj. -101118 iterations 2
Cbc0038I Pass  38: suminf.    0.38150 (1) obj. -101528 iterations 3
Cbc0038I Pass  39: suminf.    0.43250 (1) obj. -101118 iterations 2
Cbc0038I Pass  40: suminf.    0.44926 (2) obj. -101118 iterations 5
Cbc0038I Pass  41: suminf.    0.44926 (2) obj. -101118 iterations 0
Cbc0038I Pass  42: suminf.    0.19949 (1) obj. -102993 iterations 4
Cbc0038I Pass  43: suminf.    0.43250 (1) obj. -101118 iterations 3
Cbc0038I Pass  44: suminf.    0.23011 (1) obj. -102747 iterations 2
Cbc0038I Pass  45: suminf.    0.63488 (2) obj. -101118 iterations 3
Cbc0038I Pass  46: suminf.    0.23011 (1) obj. -102747 iterations 3
Cbc0038I Pass  47: suminf.    0.08761 (2) obj. -101118 iterations 2
Cbc0038I Pass  48: suminf.    0.06750 (1) obj. -101118 iterations 3
Cbc0038I Pass  49: suminf.    0.08021 (1) obj. -101220 iterations 3
Cbc0038I Pass  50: suminf.    0.55717 (2) obj. -101118 iterations 5
Cbc0038I Pass  51: suminf.    0.06750 (1) obj. -101118 iterations 7
Cbc0038I Pass  52: suminf.    0.15931 (1) obj. -101857 iterations 3
Cbc0038I Pass  53: suminf.    0.67000 (2) obj. -101118 iterations 4
Cbc0038I Pass  54: suminf.    0.67000 (2) obj. -101118 iterations 1
Cbc0038I Pass  55: suminf.    0.67000 (2) obj. -101118 iterations 1
Cbc0038I Pass  56: suminf.    0.55717 (2) obj. -101118 iterations 4
Cbc0038I Pass  57: suminf.    0.41793 (2) obj. -101118 iterations 4
Cbc0038I Pass  58: suminf.    0.06750 (1) obj. -101118 iterations 8
Cbc0038I Pass  59: suminf.    0.12356 (1) obj. -101569 iterations 3
Cbc0038I Pass  60: suminf.    0.15621 (2) obj. -101118 iterations 1
Cbc0038I Before mini branch and bound, 24 integers at bound fixed and 0 continuous
Cbc0038I Full problem 6 rows 38 columns, reduced to 4 rows 14 columns
Cbc0038I Mini branch and bound did not improve solution (0.01 seconds)
Cbc0038I Round again with cutoff of -101770
Cbc0038I Reduced cost fixing fixed 23 variables on major pass 4
Cbc0038I Pass  60: suminf.    0.18432 (1) obj. -103115 iterations 0
Cbc0038I Pass  61: suminf.    0.35149 (1) obj. -101770 iterations 4
Cbc0038I Pass  62: suminf.    0.33900 (1) obj. -101870 iterations 3
Cbc0038I Pass  63: suminf.    0.34004 (1) obj. -101862 iterations 1
Cbc0038I Pass  64: suminf.    0.34004 (1) obj. -101862 iterations 0
Cbc0038I Pass  65: suminf.    1.13660 (3) obj. -101770 iterations 3
Cbc0038I Pass  66: suminf.    0.64851 (2) obj. -101770 iterations 6
Cbc0038I Pass  67: suminf.    0.23132 (1) obj. -102737 iterations 4
Cbc0038I Pass  68: suminf.    0.23132 (1) obj. -102737 iterations 0
Cbc0038I Pass  69: suminf.    0.35149 (1) obj. -101770 iterations 4
Cbc0038I Pass  70: suminf.    0.23011 (1) obj. -102747 iterations 3
Cbc0038I Pass  71: suminf.    0.28130 (3) obj. -101770 iterations 5
Cbc0038I Pass  72: suminf.    0.14851 (1) obj. -101770 iterations 3
Cbc0038I Pass  73: suminf.    0.15931 (1) obj. -101857 iterations 3
Cbc0038I Pass  74: suminf.    1.29702 (3) obj. -101770 iterations 7
Cbc0038I Pass  75: suminf.    0.99465 (3) obj. -101770 iterations 1
Cbc0038I Pass  76: suminf.    0.19949 (1) obj. -102993 iterations 3
Cbc0038I Pass  77: suminf.    0.19949 (1) obj. -102993 iterations 0
Cbc0038I Pass  78: suminf.    0.35149 (1) obj. -101770 iterations 3
Cbc0038I Pass  79: suminf.    0.23011 (1) obj. -102747 iterations 2
Cbc0038I Pass  80: suminf.    0.23011 (1) obj. -102747 iterations 0
Cbc0038I Pass  81: suminf.    0.15260 (2) obj. -101770 iterations 3
Cbc0038I Pass  82: suminf.    0.14851 (1) obj. -101770 iterations 1
Cbc0038I Pass  83: suminf.    0.15194 (1) obj. -101797 iterations 1
Cbc0038I Pass  84: suminf.    0.15666 (2) obj. -101770 iterations 3
Cbc0038I Pass  85: suminf.    0.16293 (2) obj. -101770 iterations 3
Cbc0038I Pass  86: suminf.    1.08180 (3) obj. -101770 iterations 5
Cbc0038I Pass  87: suminf.    0.64851 (2) obj. -101770 iterations 4
Cbc0038I Pass  88: suminf.    0.23132 (1) obj. -102737 iterations 3
Cbc0038I Pass  89: suminf.    0.23132 (1) obj. -102737 iterations 0
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 25 integers at bound fixed and 0 continuous
Cbc0038I Full problem 6 rows 38 columns, reduced to 2 rows 11 columns
Cbc0038I Mini branch and bound did not improve solution (0.02 seconds)
Cbc0038I After 0.02 seconds - Feasibility pump exiting with objective of -100575 - took 0.01 seconds
Cbc0012I Integer solution of -100575 found by feasibility pump after 0 iterations and 0 nodes (0.02 seconds)
Cbc0038I Full problem 6 rows 38 columns, reduced to 0 rows 0 columns
Cbc0031I 3 added rows had average density of 12.666667
Cbc0013I At root node, 5 cuts changed objective from -103290.67 to -100575 in 2 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 4 row cuts average 8.8 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 6 (TwoMirCuts) - 3 row cuts average 12.7 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0001I Search completed - best objective -100575, took 8 iterations and 0 nodes (0.02 seconds)
Cbc0035I Maximum depth 0, 20 variables fixed on reduced cost
Cuts at root node changed objective from -103291 to -100575
Probing was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Knapsack was tried 2 times and created 4 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Clique was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 2 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 2 times and created 3 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

Result - Optimal solution found

Objective value:                100575.00000000
Enumerated nodes:               0
Total iterations:               8
Time (CPU seconds):             0.02
Time (Wallclock seconds):       0.02

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.03   (Wallclock seconds):       0.03

Optimization Status: Optimal
Selected 9 locations: ['L5', 'L9', 'L20', 'L27', 'L28', 'L31', 'L39', 'L44', 'L45']

=== DETAILED STATION ANALYSIS ===

Station L5:
  Cost: $100,013
  Covers 2 population points
  Total population covered: 8,046
  Population points covered: [40526642, 40567912]

Station L9:
  Cost: $132,842
  Covers 3 population points
  Total population covered: 12,069
  Population points covered: [40607124, 40725358, 40464263]

Station L20:
  Cost: $106,218
  Covers 2 population points
  Total population covered: 8,046
  Population points covered: [40465242, 2446145984]

Station L27:
  Cost: $91,489
  Covers 3 population points
  Total population covered: 12,069
  Population points covered: [40539764, 40539692, 40535049]

Station L28:
  Cost: $85,153
  Covers 2 population points
  Total population covered: 8,046
  Population points covered: [40614556, 40521016]

Station L31:
  Cost: $91,256
  Covers 1 population points
  Total population covered: 4,023
  Population points covered: [40714175]

Station L39:
  Cost: $107,224
  Covers 2 population points
  Total population covered: 8,046
  Population points covered: [40765012, 40780131]

Station L44:
  Cost: $132,965
  Covers 3 population points
  Total population covered: 12,069
  Population points covered: [40514597, 40538703, 40514683]

Station L45:
  Cost: $142,227
  Covers 7 population points
  Total population covered: 28,161
  Population points covered: [2111219930, 40523951, 1367319909, 40523941, 40516062, 40523863, 40570436]

=== POPULATION COVERAGE ANALYSIS ===
Creating detailed population coverage mapping...
Coverage mapping complete:
  - Points covered: 25/200 (12.5%)
  - Population covered: 100,575/804,600 (12.5%)

=== OPTIMIZATION RESULTS ===
Total budget: $1,000,000
Used budget: $989,387
Selected 9 locations
Covered population: 100,575 out of 804,600 (12.50%)

=== COVERAGE VALIDATION ===
Manual coverage calculation: 100,575 (12.50%)

=== CREATING VISUALIZATIONS ===
Creating visualization with accurate coverage display...
Calculating actual coverage for 200 population points...
Actual coverage calculation:
  - Points covered: 25/200 (12.5%)
  - Population covered: 100,575/804,600 (12.5%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:128: UserWarning: Legend does not support handles for PatchCollection instances.
See: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#implementing-a-custom-legend-handler
  plt.legend(fontsize=10, loc='upper right')
Calculating actual coverage for 200 population points...
Actual coverage calculation:
  - Points covered: 25/200 (12.5%)
  - Population covered: 100,575/804,600 (12.5%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:228: UserWarning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

  city_center = city_gdf.centroid.iloc[0]
Interactive map saved as 'ev_charging_optimization_map_portland.html'
Coverage statistics: 12.5% of population covered

=== OPTIMIZATION COMPLETE ===
Results: Selected 9 new charging station locations
Population coverage: 100575 out of 804600 (12.50%)
Total cost: $989,387
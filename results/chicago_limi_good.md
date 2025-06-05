
SEED = 7   # good for seatle - 15, portland - 35, austin - 47
CITY = "Chicago, IL, USA"

POPULATION_POINTS = 2000

MAX_BUDGET = 700000  # $1M budget for new stations
BASE_STATION_COST = 100000  # Cost per station

MAX_COVERAGE_DISTANCE = 600  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters

NUM_CANDIDATE_LOCATIONS = 1000



Starting EV charging station optimization for Chicago, IL, USA

=== COLLECTING DATA ===
Retrieved 29201 road network nodes and 76889 edges
Getting census data for specific counties: ['031']
Retrieved census data for 1319 tracts
Generated 2000 population points from road network as fallback
City bounds: -87.940088, 41.644531, -87.524081, 42.023040
Retrieved 73014 charging stations from NREL API within bounding box
Filtered to 301 stations actually within city boundary

=== GENERATING CANDIDATE LOCATIONS ===
Using all road nodes within city: 29094 nodes
Generated 1000 candidate locations avoiding water areas

=== PREPARING DATA FOR OPTIMIZATION ===
Preparing coverage matrix with visualization-consistent method...
100%|██████████| 1000/1000 [03:30<00:00,  4.76it/s]
Coverage matrix: (2000, 1001) - should now match visualization!

=== RUNNING OPTIMIZATION ===

=== STARTING MILP OPTIMIZATION ===
Population points: 2000
Candidate locations: 1000
Total population: 5,198,000
Station costs range: $80,012 - $149,915
Added 1346 coverage constraints
Solving MILP problem...
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\venv\Lib\site-packages\pulp\apis\../solverdir/cbc/win/i64/cbc.exe C:\Users\LIMOR~1.HOD\AppData\Local\Temp\0054ed1b23fd44f5988c93613a56f964-pulp.mps -max -timeMode elapsed -branch -printingOptions all -solution C:\Users\LIMOR~1.HOD\AppData\Local\Temp\0054ed1b23fd44f5988c93613a56f964-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 2006 COLUMNS
At line 15541 RHS
At line 17543 BOUNDS
At line 20544 ENDATA
Problem MODEL has 2001 rows, 3000 columns and 5534 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 158344 - 0.02 seconds
Cgl0002I 654 variables fixed
Cgl0004I processed model has 733 rows, 1631 columns (1631 integer (1631 of which binary)) and 3551 elements
Cutoff increment increased from 1e-05 to 2599
Cbc0038I Initial state - 1 integers unsatisfied sum - 0.27497
Cbc0038I Solution found of -153341
Cbc0038I Before mini branch and bound, 1630 integers at bound fixed and 0 continuous
Cbc0038I Full problem 733 rows 1631 columns, reduced to 0 rows 0 columns
Cbc0038I Mini branch and bound did not improve solution (0.06 seconds)
Cbc0038I Round again with cutoff of -156180
Cbc0038I Reduced cost fixing fixed 887 variables on major pass 2
Cbc0038I Pass   1: suminf.    0.15607 (1) obj. -156180 iterations 695
Cbc0038I Pass   2: suminf.    0.27497 (1) obj. -158344 iterations 2
Cbc0038I Pass   3: suminf.    0.44266 (2) obj. -156180 iterations 596
Cbc0038I Pass   4: suminf.    0.44266 (2) obj. -156180 iterations 21
Cbc0038I Pass   5: suminf.    0.44266 (2) obj. -156180 iterations 16
Cbc0038I Pass   6: suminf.    0.44266 (2) obj. -156180 iterations 16
Cbc0038I Pass   7: suminf.    0.44266 (2) obj. -156180 iterations 47
Cbc0038I Pass   8: suminf.    0.44266 (2) obj. -156180 iterations 15
Cbc0038I Pass   9: suminf.    0.44266 (2) obj. -156180 iterations 11
Cbc0038I Pass  10: suminf.    0.44266 (2) obj. -156180 iterations 9
Cbc0038I Pass  11: suminf.    0.27497 (1) obj. -158344 iterations 604
Cbc0038I Pass  12: suminf.    0.15607 (1) obj. -156180 iterations 2
Cbc0038I Pass  13: suminf.    0.44266 (2) obj. -156180 iterations 592
Cbc0038I Pass  14: suminf.    0.44266 (2) obj. -156180 iterations 16
Cbc0038I Pass  15: suminf.    2.39892 (8) obj. -156180 iterations 51
Cbc0038I Pass  16: suminf.    0.44266 (2) obj. -156180 iterations 32
Cbc0038I Pass  17: suminf.    0.44266 (2) obj. -156180 iterations 158
Cbc0038I Pass  18: suminf.    0.44266 (2) obj. -156180 iterations 22
Cbc0038I Pass  19: suminf.    0.44266 (2) obj. -156180 iterations 127
Cbc0038I Pass  20: suminf.    0.44266 (2) obj. -156180 iterations 17
Cbc0038I Pass  21: suminf.    0.27497 (1) obj. -158344 iterations 572
Cbc0038I Pass  22: suminf.    0.15607 (1) obj. -156180 iterations 3
Cbc0038I Pass  23: suminf.    0.44266 (2) obj. -156180 iterations 597
Cbc0038I Pass  24: suminf.    0.44266 (2) obj. -156180 iterations 27
Cbc0038I Pass  25: suminf.    1.40350 (5) obj. -156180 iterations 84
Cbc0038I Pass  26: suminf.    0.27312 (1) obj. -156180 iterations 656
Cbc0038I Pass  27: suminf.    0.29589 (2) obj. -156180 iterations 5
Cbc0038I Pass  28: suminf.    1.11329 (4) obj. -156180 iterations 595
Cbc0038I Pass  29: suminf.    1.40350 (5) obj. -156180 iterations 103
Cbc0038I Pass  30: suminf.    1.40350 (5) obj. -156180 iterations 13
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 1602 integers at bound fixed and 0 continuous
Cbc0038I Full problem 733 rows 1631 columns, reduced to 1 rows 3 columns
Cbc0038I Mini branch and bound did not improve solution (0.20 seconds)
Cbc0038I After 0.20 seconds - Feasibility pump exiting with objective of -153341 - took 0.15 seconds
Cbc0012I Integer solution of -153341 found by feasibility pump after 0 iterations and 0 nodes (0.20 seconds)
Cbc0013I At root node, 0 cuts changed objective from -158343.53 to -158343.53 in 1 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0010I After 0 nodes, 1 on tree, -153341 best solution, best possible -158343.53 (0.27 seconds)
Cbc0012I Integer solution of -155940 found by DiveCoefficient after 11 iterations and 5 nodes (0.44 seconds)
Cbc0001I Search completed - best objective -155940, took 11 iterations and 5 nodes (0.44 seconds)
Cbc0032I Strong branching done 78 times (183 iterations), fathomed 0 nodes and fixed 0 variables
Cbc0035I Maximum depth 5, 887 variables fixed on reduced cost
Cuts at root node changed objective from -158344 to -158344
Probing was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Gomory was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Knapsack was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Clique was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
FlowCover was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)

Result - Optimal solution found

Objective value:                155940.00000000
Enumerated nodes:               5
Total iterations:               11
Time (CPU seconds):             0.45
Time (Wallclock seconds):       0.45

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.49   (Wallclock seconds):       0.49

Optimization Status: Optimal
Selected 7 locations: ['L104', 'L262', 'L346', 'L400', 'L409', 'L592', 'L890']

=== DETAILED STATION ANALYSIS ===

Station L104:
  Cost: $113,947
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [286841694, 261230004, 3413894355, 261158078, 305903401, 9165857535, 288470605, 305903402, 261147324]

Station L262:
  Cost: $118,953
  Covers 8 population points
  Total population covered: 20,792
  Population points covered: [367789428, 261138368, 261159283, 261153751, 261135622, 261191326, 261171340, 375654579]

Station L346:
  Cost: $84,026
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [261224907, 261101452, 350565643, 1894138899, 261096312, 468419465, 385122543, 349881667, 7185816176]

Station L400:
  Cost: $89,087
  Covers 8 population points
  Total population covered: 20,792
  Population points covered: [261151263, 261161802, 261249982, 261184826, 261240294, 261184828, 536282913, 261162180]

Station L409:
  Cost: $99,735
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [9813792275, 261127655, 261239987, 261161854, 9813792329, 261251110, 261223296, 261161856, 261177634]

Station L592:
  Cost: $104,056
  Covers 8 population points
  Total population covered: 20,792
  Population points covered: [261207095, 261202199, 261123907, 261275870, 261123911, 4332627045, 261207094, 261260035]

Station L890:
  Cost: $87,097
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [261177936, 261210807, 261177937, 261227593, 261147063, 261223355, 261289003, 369649712, 261288997]

=== POPULATION COVERAGE ANALYSIS ===
Creating detailed population coverage mapping...
Coverage mapping complete:
  - Points covered: 60/2000 (3.0%)
  - Population covered: 155,940/5,198,000 (3.0%)

=== OPTIMIZATION RESULTS ===
Total budget: $700,000
Used budget: $696,901
Selected 7 locations
Covered population: 155,940 out of 5,198,000 (3.00%)

=== COVERAGE VALIDATION ===
Manual coverage calculation: 155,940 (3.00%)

=== CREATING VISUALIZATIONS ===
Creating visualization with accurate coverage display...
Calculating actual coverage for 2000 population points...
Actual coverage calculation:
  - Points covered: 60/2000 (3.0%)
  - Population covered: 155,940/5,198,000 (3.0%)
C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\vizualization.py:128: UserWarning: Legend does not support handles for PatchCollection instances.
See: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#implementing-a-custom-legend-handler
  plt.legend(fontsize=10, loc='upper right')
Calculating actual coverage for 2000 population points...
Actual coverage calculation:
  - Points covered: 60/2000 (3.0%)
  - Population covered: 155,940/5,198,000 (3.0%)
C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\vizualization.py:228: UserWarning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

  city_center = city_gdf.centroid.iloc[0]
Interactive map saved as 'ev_charging_optimization_map_chicago.html'
Coverage statistics: 3.0% of population covered

=== OPTIMIZATION COMPLETE ===
Results: Selected 7 new charging station locations
Population coverage: 155940 out of 5198000 (3.00%)
Total cost: $696,901

Process finished with exit code 0
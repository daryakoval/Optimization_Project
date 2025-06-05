SEED = 7   # good for seatle - 15, portland - 35, austin - 47
CITY = "Chicago, IL, USA"

POPULATION_POINTS = 2000
MAX_BUDGET = 700000  # $1M budget for new stations
BASE_STATION_COST = 100000  # Cost per station

MAX_COVERAGE_DISTANCE = 700  # meters
MIN_DISTANCE_BETWEEN_STATIONS = 500  # meters

NUM_CANDIDATE_LOCATIONS = 1000


Starting EV charging station optimization for Chicago, IL, USA

=== COLLECTING DATA ===
Retrieved 29201 road network nodes and 76889 edges
Getting census data for specific counties: ['031']
Retrieved census data for 1319 tracts
Generated 2000 population points from road network as fallback
City bounds: -87.940088, 41.644531, -87.524081, 42.023040
Retrieved 73013 charging stations from NREL API within bounding box
Filtered to 301 stations actually within city boundary

=== GENERATING CANDIDATE LOCATIONS ===
Using all road nodes within city: 29094 nodes
Generated 1000 candidate locations avoiding water areas

=== PREPARING DATA FOR OPTIMIZATION ===
Preparing coverage matrix with visualization-consistent method...
100%|██████████| 1000/1000 [03:27<00:00,  4.81it/s]
Coverage matrix: (2000, 1001) - should now match visualization!

=== RUNNING OPTIMIZATION ===

=== STARTING MILP OPTIMIZATION ===
Population points: 2000
Candidate locations: 1000
Total population: 5,198,000
Station costs range: $80,012 - $149,915
Added 1506 coverage constraints
Solving MILP problem...
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\venv\Lib\site-packages\pulp\apis\../solverdir/cbc/win/i64/cbc.exe C:\Users\LIMOR~1.HOD\AppData\Local\Temp\f74958cded2f41fca47c479def37f6ea-pulp.mps -max -timeMode elapsed -branch -printingOptions all -solution C:\Users\LIMOR~1.HOD\AppData\Local\Temp\f74958cded2f41fca47c479def37f6ea-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 2006 COLUMNS
At line 16456 RHS
At line 18458 BOUNDS
At line 21459 ENDATA
Problem MODEL has 2001 rows, 3000 columns and 6449 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 189243 - 0.02 seconds
Cgl0002I 494 variables fixed
Cgl0004I processed model has 1013 rows, 1964 columns (1964 integer (1963 of which binary)) and 4916 elements
Cutoff increment increased from 1e-05 to 2599
Cbc0038I Initial state - 10 integers unsatisfied sum - 4.65117
Cbc0038I Pass   1: suminf.    1.94431 (4) obj. -186766 iterations 954
Cbc0038I Solution found of -174133
Cbc0038I Cleaned solution of -174133
Cbc0038I Before mini branch and bound, 1950 integers at bound fixed and 0 continuous
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 1 rows 2 columns
Cbc0038I Mini branch and bound improved solution from -174133 to -176732 (0.07 seconds)
Cbc0038I Round again with cutoff of -180322
Cbc0038I Reduced cost fixing fixed 841 variables on major pass 2
Cbc0038I Pass   2: suminf.    1.94431 (4) obj. -186766 iterations 0
Cbc0038I Pass   3: suminf.    0.34020 (1) obj. -180322 iterations 49
Cbc0038I Pass   4: suminf.    0.48608 (1) obj. -182976 iterations 24
Cbc0038I Pass   5: suminf.    2.42371 (5) obj. -180322 iterations 853
Cbc0038I Pass   6: suminf.    1.46492 (4) obj. -180322 iterations 128
Cbc0038I Pass   7: suminf.    1.94431 (4) obj. -181568 iterations 748
Cbc0038I Pass   8: suminf.    1.46492 (4) obj. -180322 iterations 982
Cbc0038I Pass   9: suminf.    1.46492 (4) obj. -180322 iterations 54
Cbc0038I Pass  10: suminf.    4.63618 (10) obj. -180322 iterations 71
Cbc0038I Pass  11: suminf.    1.71939 (5) obj. -180322 iterations 63
Cbc0038I Pass  12: suminf.    1.66201 (4) obj. -182772 iterations 796
Cbc0038I Pass  13: suminf.    0.71939 (2) obj. -180322 iterations 402
Cbc0038I Pass  14: suminf.    0.83100 (2) obj. -180612 iterations 380
Cbc0038I Pass  15: suminf.    2.27752 (5) obj. -180322 iterations 736
Cbc0038I Pass  16: suminf.    2.27752 (5) obj. -180322 iterations 112
Cbc0038I Pass  17: suminf.    0.71939 (2) obj. -180322 iterations 439
Cbc0038I Pass  18: suminf.    0.83100 (2) obj. -180612 iterations 377
Cbc0038I Pass  19: suminf.    1.71939 (5) obj. -180322 iterations 821
Cbc0038I Pass  20: suminf.    1.71939 (5) obj. -180322 iterations 32
Cbc0038I Pass  21: suminf.    1.66201 (4) obj. -182772 iterations 810
Cbc0038I Pass  22: suminf.    0.71939 (2) obj. -180322 iterations 396
Cbc0038I Pass  23: suminf.    0.83100 (2) obj. -180612 iterations 375
Cbc0038I Pass  24: suminf.    3.42471 (9) obj. -180322 iterations 843
Cbc0038I Pass  25: suminf.    0.71939 (2) obj. -180322 iterations 484
Cbc0038I Pass  26: suminf.    0.83100 (2) obj. -180612 iterations 381
Cbc0038I Pass  27: suminf.    2.62031 (9) obj. -180322 iterations 763
Cbc0038I Pass  28: suminf.    1.71939 (5) obj. -180322 iterations 111
Cbc0038I Pass  29: suminf.    1.71939 (4) obj. -180322 iterations 53
Cbc0038I Pass  30: suminf.    1.24651 (3) obj. -181692 iterations 699
Cbc0038I Pass  31: suminf.    3.29783 (9) obj. -180322 iterations 756
Cbc0038I Rounding solution of -179331 is better than previous of -176732

Cbc0038I Before mini branch and bound, 1903 integers at bound fixed and 0 continuous
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 1 rows 6 columns
Cbc0038I Mini branch and bound did not improve solution (0.31 seconds)
Cbc0038I Round again with cutoff of -183393
Cbc0038I Reduced cost fixing fixed 893 variables on major pass 3
Cbc0038I Pass  31: suminf.    1.94431 (4) obj. -186766 iterations 0
Cbc0038I Pass  32: suminf.    0.64632 (2) obj. -183393 iterations 153
Cbc0038I Pass  33: suminf.    0.97216 (2) obj. -184240 iterations 131
Cbc0038I Pass  34: suminf.    2.24231 (5) obj. -183393 iterations 842
Cbc0038I Pass  35: suminf.    1.64632 (4) obj. -183393 iterations 98
Cbc0038I Pass  36: suminf.    1.94431 (4) obj. -184167 iterations 751
Cbc0038I Pass  37: suminf.    2.24231 (5) obj. -183393 iterations 873
Cbc0038I Pass  38: suminf.    1.64632 (4) obj. -183393 iterations 153
Cbc0038I Pass  39: suminf.    1.94431 (4) obj. -184167 iterations 747
Cbc0038I Pass  40: suminf.    3.90233 (9) obj. -183393 iterations 724
Cbc0038I Pass  41: suminf.    3.56055 (12) obj. -183393 iterations 695
Cbc0038I Pass  42: suminf.    1.57852 (4) obj. -183393 iterations 756
Cbc0038I Pass  43: suminf.    1.39402 (3) obj. -183872 iterations 726
Cbc0038I Pass  44: suminf.    1.28017 (3) obj. -183393 iterations 647
Cbc0038I Pass  45: suminf.    1.28017 (3) obj. -183393 iterations 9
Cbc0038I Pass  46: suminf.    1.28017 (3) obj. -183393 iterations 285
Cbc0038I Pass  47: suminf.    1.28017 (3) obj. -183393 iterations 3
Cbc0038I Pass  48: suminf.    1.28017 (3) obj. -183393 iterations 1015
Cbc0038I Pass  49: suminf.    1.57852 (4) obj. -183393 iterations 160
Cbc0038I Pass  50: suminf.    1.39402 (3) obj. -183872 iterations 784
Cbc0038I Pass  51: suminf.    1.28017 (3) obj. -183393 iterations 647
Cbc0038I Pass  52: suminf.    1.28017 (3) obj. -183393 iterations 6
Cbc0038I Pass  53: suminf.    1.28017 (3) obj. -183393 iterations 282
Cbc0038I Pass  54: suminf.    1.28017 (3) obj. -183393 iterations 4
Cbc0038I Pass  55: suminf.    1.28017 (3) obj. -183393 iterations 1024
Cbc0038I Pass  56: suminf.    2.21640 (5) obj. -183393 iterations 210
Cbc0038I Pass  57: suminf.    2.21640 (5) obj. -183393 iterations 23
Cbc0038I Pass  58: suminf.    2.21640 (5) obj. -183393 iterations 234
Cbc0038I Pass  59: suminf.    2.21640 (5) obj. -183393 iterations 9
Cbc0038I Pass  60: suminf.    2.21640 (5) obj. -183393 iterations 233
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 1938 integers at bound fixed and 0 continuous
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 1 rows 4 columns
Cbc0038I Mini branch and bound did not improve solution (0.54 seconds)
Cbc0038I After 0.54 seconds - Feasibility pump exiting with objective of -179331 - took 0.48 seconds
Cbc0012I Integer solution of -179331 found by feasibility pump after 0 iterations and 0 nodes (0.54 seconds)
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 1 rows 2 columns
Cbc0013I At root node, 0 cuts changed objective from -189243.45 to -189243.45 in 1 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.001 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0010I After 0 nodes, 1 on tree, -179331 best solution, best possible -189243.45 (0.61 seconds)
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 1 rows 3 columns
Cbc0038I Full problem 1013 rows 1964 columns, reduced to 130 rows 204 columns
Cbc0044I Reduced cost fixing - 130 rows, 204 columns - restarting search
Cbc0012I Integer solution of -179331 found by Previous solution after 0 iterations and 0 nodes (1.29 seconds)
Cbc0038I Full problem 130 rows 204 columns, reduced to 1 rows 2 columns
Cbc0012I Integer solution of -181930 found by DiveCoefficient after 67 iterations and 0 nodes (1.31 seconds)
Cbc0031I 8 added rows had average density of 53.75
Cbc0013I At root node, 8 cuts changed objective from -189243.45 to -184661.09 in 8 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 1 column cuts (1 active)  in 0.001 seconds - new frequency is 1
Cbc0014I Cut generator 1 (Gomory) - 1 row cuts average 77.0 elements, 0 column cuts (0 active)  in 0.003 seconds - new frequency is -100
Cbc0014I Cut generator 2 (Knapsack) - 3 row cuts average 34.0 elements, 0 column cuts (0 active)  in 0.003 seconds - new frequency is 1
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 6 (TwoMirCuts) - 30 row cuts average 58.6 elements, 0 column cuts (0 active)  in 0.005 seconds - new frequency is -100
Cbc0014I Cut generator 7 (ZeroHalf) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.005 seconds - new frequency is -100
Cbc0001I Search completed - best objective -181930, took 74 iterations and 0 nodes (1.32 seconds)
Cbc0032I Strong branching done 46 times (141 iterations), fathomed 1 nodes and fixed 0 variables
Cbc0035I Maximum depth 0, 33 variables fixed on reduced cost
Cbc0038I Probing was tried 8 times and created 1 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Cbc0038I Gomory was tried 8 times and created 1 cuts of which 0 were active after adding rounds of cuts (0.003 seconds)
Cbc0038I Knapsack was tried 8 times and created 3 cuts of which 0 were active after adding rounds of cuts (0.003 seconds)
Cbc0038I Clique was tried 8 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Cbc0038I MixedIntegerRounding2 was tried 8 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Cbc0038I FlowCover was tried 8 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Cbc0038I TwoMirCuts was tried 8 times and created 30 cuts of which 0 were active after adding rounds of cuts (0.005 seconds)
Cbc0038I ZeroHalf was tried 8 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.005 seconds)
Cbc0012I Integer solution of -181930 found by Reduced search after 497 iterations and 50 nodes (1.33 seconds)
Cbc0001I Search completed - best objective -181930, took 497 iterations and 50 nodes (1.33 seconds)
Cbc0032I Strong branching done 394 times (2018 iterations), fathomed 16 nodes and fixed 0 variables
Cbc0035I Maximum depth 19, 1397 variables fixed on reduced cost
Cuts at root node changed objective from -189243 to -189243
Probing was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Gomory was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Knapsack was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
Clique was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)
FlowCover was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.002 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.001 seconds)

Result - Optimal solution found

Objective value:                181930.00000000
Enumerated nodes:               50
Total iterations:               497
Time (CPU seconds):             1.34
Time (Wallclock seconds):       1.34

Option for printingOptions changed from normal to all
Total time (CPU seconds):       1.38   (Wallclock seconds):       1.38

Optimization Status: Optimal
Selected 7 locations: ['L315', 'L346', 'L400', 'L431', 'L592', 'L790', 'L890']

=== DETAILED STATION ANALYSIS ===

Station L315:
  Cost: $116,092
  Covers 10 population points
  Total population covered: 25,990
  Population points covered: [261214845, 734791867, 287238679, 5872364079, 707916304, 2503413062, 261198426, 739187886, 261164174, 739187883]

Station L346:
  Cost: $84,026
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [261224907, 261101452, 350565643, 1894138899, 261096312, 468419465, 385122543, 349881667, 7185816176]

Station L400:
  Cost: $89,087
  Covers 10 population points
  Total population covered: 25,990
  Population points covered: [261184830, 261151263, 261161802, 261114664, 261249982, 261184826, 261240294, 261184828, 536282913, 261162180]

Station L431:
  Cost: $86,282
  Covers 9 population points
  Total population covered: 23,391
  Population points covered: [261142347, 261152735, 8891689967, 5578495317, 1884990508, 261174947, 261152799, 261275568, 261177742]

Station L592:
  Cost: $104,056
  Covers 10 population points
  Total population covered: 25,990
  Population points covered: [1445893721, 261207095, 261202199, 261192893, 261123907, 261275870, 261123911, 4332627045, 261207094, 261260035]

Station L790:
  Cost: $113,263
  Covers 12 population points
  Total population covered: 31,188
  Population points covered: [11484243290, 261211963, 261161854, 12242446381, 261160630, 261214571, 2123487246, 261214573, 261342991, 261251110, 261161856, 4335557432]

Station L890:
  Cost: $87,097
  Covers 10 population points
  Total population covered: 25,990
  Population points covered: [261177936, 261210807, 261177937, 261227593, 261147063, 261223355, 261289003, 369649712, 261288997, 261102595]

=== POPULATION COVERAGE ANALYSIS ===
Creating detailed population coverage mapping...
Coverage mapping complete:
  - Points covered: 70/2000 (3.5%)
  - Population covered: 181,930/5,198,000 (3.5%)

=== OPTIMIZATION RESULTS ===
Total budget: $700,000
Used budget: $679,903
Selected 7 locations
Covered population: 181,930 out of 5,198,000 (3.50%)

=== COVERAGE VALIDATION ===
Manual coverage calculation: 181,930 (3.50%)

=== CREATING VISUALIZATIONS ===
Creating visualization with accurate coverage display...
Calculating actual coverage for 2000 population points...
Actual coverage calculation:
  - Points covered: 70/2000 (3.5%)
  - Population covered: 181,930/5,198,000 (3.5%)
C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\vizualization.py:128: UserWarning: Legend does not support handles for PatchCollection instances.
See: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#implementing-a-custom-legend-handler
  plt.legend(fontsize=10, loc='upper right')
Calculating actual coverage for 2000 population points...
Actual coverage calculation:
  - Points covered: 70/2000 (3.5%)
  - Population covered: 181,930/5,198,000 (3.5%)
C:\Users\limor.hodory\OneDrive - AU10TIX\Desktop\opt\Optimization_Project\vizualization.py:228: UserWarning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

  city_center = city_gdf.centroid.iloc[0]
Interactive map saved as 'ev_charging_optimization_map_chicago.html'
Coverage statistics: 3.5% of population covered

=== OPTIMIZATION COMPLETE ===
Results: Selected 7 new charging station locations
Population coverage: 181930 out of 5198000 (3.50%)
Total cost: $679,903

Process finished with exit code 0
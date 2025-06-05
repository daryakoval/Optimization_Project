Starting EV charging station optimization for Seattle, WA, USA

=== COLLECTING DATA ===
Retrieved 19054 road network nodes and 50188 edges
Getting census data for specific counties: ['033']
Retrieved census data for 398 tracts
Generated 200 population points from road network as fallback
City bounds: -122.459696, 47.481002, -122.224433, 47.734150
Retrieved 72822 charging stations from NREL API within bounding box
Filtered to 643 stations actually within city boundary

=== GENERATING CANDIDATE LOCATIONS ===
Using all road nodes within city: 19030 nodes
Generated 50 candidate locations avoiding water areas

=== PREPARING DATA FOR OPTIMIZATION ===
Preparing coverage matrix with visualization-consistent method...

  0%|          | 0/50 [00:00<?, ?it/s]
 16%|#6        | 8/50 [00:00<00:00, 75.00it/s]
 32%|###2      | 16/50 [00:00<00:00, 76.87it/s]
 48%|####8     | 24/50 [00:00<00:00, 77.74it/s]
 64%|######4   | 32/50 [00:00<00:00, 77.32it/s]
 80%|########  | 40/50 [00:00<00:00, 77.54it/s]
 96%|#########6| 48/50 [00:00<00:00, 77.07it/s]
100%|##########| 50/50 [00:00<00:00, 76.96it/s]
Coverage matrix: (200, 51) - should now match visualization!

=== RUNNING OPTIMIZATION ===

=== STARTING MILP OPTIMIZATION ===
Population points: 200
Candidate locations: 50
Total population: 2,195,400
Station costs range: $81,248 - $149,891
Added 46 coverage constraints
Solving MILP problem...
Welcome to the CBC MILP Solver 
Version: 2.10.3 
Build Date: Dec 15 2019 

command line - C:\Users\Darya\AppData\Local\Programs\Python\Python311\Lib\site-packages\pulp\apis\../solverdir/cbc/win/i64/cbc.exe C:\Users\Darya\AppData\Local\Temp\2372318b4e9a489aa774c71165b7ef79-pulp.mps -max -timeMode elapsed -branch -printingOptions all -solution C:\Users\Darya\AppData\Local\Temp\2372318b4e9a489aa774c71165b7ef79-pulp.sol (default strategy 1)
At line 2 NAME          MODEL
At line 3 ROWS
At line 206 COLUMNS
At line 1218 RHS
At line 1420 BOUNDS
At line 1671 ENDATA
Problem MODEL has 201 rows, 250 columns and 311 elements
Coin0008I MODEL read with 0 errors
Option for timeMode changed from cpu to elapsed
Continuous objective value is 249683 - 0.00 seconds
Cgl0002I 154 variables fixed
Cgl0004I processed model has 11 rows, 42 columns (42 integer (42 of which binary)) and 67 elements
Cbc0038I Initial state - 1 integers unsatisfied sum - 0.372998
Cbc0038I Solution found of -241494
Cbc0038I Before mini branch and bound, 41 integers at bound fixed and 0 continuous
Cbc0038I Full problem 11 rows 42 columns, reduced to 0 rows 0 columns
Cbc0038I Mini branch and bound did not improve solution (0.01 seconds)
Cbc0038I Round again with cutoff of -242313
Cbc0038I Reduced cost fixing fixed 25 variables on major pass 2
Cbc0038I Pass   1: suminf.    0.02487 (1) obj. -242313 iterations 9
Cbc0038I Pass   2: suminf.    0.24739 (1) obj. -249641 iterations 1
Cbc0038I Pass   3: suminf.    0.50914 (3) obj. -242313 iterations 9
Cbc0038I Pass   4: suminf.    0.03730 (1) obj. -242313 iterations 7
Cbc0038I Pass   5: suminf.    0.74588 (2) obj. -242313 iterations 4
Cbc0038I Pass   6: suminf.    0.03730 (1) obj. -242313 iterations 3
Cbc0038I Pass   7: suminf.    0.70214 (3) obj. -242313 iterations 9
Cbc0038I Pass   8: suminf.    0.62760 (2) obj. -242313 iterations 1
Cbc0038I Pass   9: suminf.    0.30847 (1) obj. -242313 iterations 7
Cbc0038I Pass  10: suminf.    0.13825 (1) obj. -247918 iterations 1
Cbc0038I Pass  11: suminf.    0.04426 (1) obj. -242951 iterations 2
Cbc0038I Pass  12: suminf.    0.02487 (1) obj. -242313 iterations 2
Cbc0038I Pass  13: suminf.    0.04426 (1) obj. -242951 iterations 1
Cbc0038I Pass  14: suminf.    0.10243 (2) obj. -242313 iterations 3
Cbc0038I Pass  15: suminf.    0.70160 (2) obj. -242313 iterations 10
Cbc0038I Pass  16: suminf.    0.57983 (2) obj. -242313 iterations 4
Cbc0038I Pass  17: suminf.    0.24739 (1) obj. -249641 iterations 4
Cbc0038I Pass  18: suminf.    0.02487 (1) obj. -242313 iterations 1
Cbc0038I Pass  19: suminf.    1.92540 (4) obj. -242313 iterations 11
Cbc0038I Pass  20: suminf.    0.45576 (1) obj. -245526 iterations 8
Cbc0038I Pass  21: suminf.    0.35820 (2) obj. -242313 iterations 3
Cbc0038I Pass  22: suminf.    0.45576 (1) obj. -245526 iterations 2
Cbc0038I Pass  23: suminf.    0.70160 (2) obj. -242313 iterations 6
Cbc0038I Pass  24: suminf.    0.57983 (2) obj. -242313 iterations 3
Cbc0038I Pass  25: suminf.    0.24739 (1) obj. -249641 iterations 3
Cbc0038I Pass  26: suminf.    0.02487 (1) obj. -242313 iterations 1
Cbc0038I Pass  27: suminf.    0.02487 (1) obj. -242313 iterations 0
Cbc0038I Pass  28: suminf.    0.57983 (2) obj. -242313 iterations 6
Cbc0038I Pass  29: suminf.    0.57983 (2) obj. -242313 iterations 1
Cbc0038I Pass  30: suminf.    1.06224 (3) obj. -242313 iterations 1
Cbc0038I No solution found this major pass
Cbc0038I Before mini branch and bound, 27 integers at bound fixed and 0 continuous
Cbc0038I Full problem 11 rows 42 columns, reduced to 3 rows 10 columns
Cbc0038I Mini branch and bound did not improve solution (0.01 seconds)
Cbc0038I After 0.01 seconds - Feasibility pump exiting with objective of -241494 - took 0.00 seconds
Cbc0012I Integer solution of -241494 found by feasibility pump after 0 iterations and 0 nodes (0.01 seconds)
Cbc0038I Full problem 11 rows 42 columns, reduced to 0 rows 0 columns
Cbc0031I 4 added rows had average density of 8
Cbc0013I At root node, 15 cuts changed objective from -249682.79 to -241494 in 3 passes
Cbc0014I Cut generator 0 (Probing) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 1 (Gomory) - 2 row cuts average 10.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 2 (Knapsack) - 6 row cuts average 6.8 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0014I Cut generator 3 (Clique) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 4 (MixedIntegerRounding2) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 5 (FlowCover) - 0 row cuts average 0.0 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is -100
Cbc0014I Cut generator 6 (TwoMirCuts) - 12 row cuts average 10.1 elements, 0 column cuts (0 active)  in 0.000 seconds - new frequency is 1
Cbc0001I Search completed - best objective -241494, took 10 iterations and 0 nodes (0.01 seconds)
Cbc0035I Maximum depth 0, 26 variables fixed on reduced cost
Cuts at root node changed objective from -249683 to -241494
Probing was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Gomory was tried 3 times and created 2 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Knapsack was tried 3 times and created 6 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
Clique was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
MixedIntegerRounding2 was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
FlowCover was tried 3 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
TwoMirCuts was tried 3 times and created 12 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)
ZeroHalf was tried 1 times and created 0 cuts of which 0 were active after adding rounds of cuts (0.000 seconds)

Result - Optimal solution found

Objective value:                241494.00000000
Enumerated nodes:               0
Total iterations:               10
Time (CPU seconds):             0.01
Time (Wallclock seconds):       0.01

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.03   (Wallclock seconds):       0.03

Optimization Status: Optimal
Selected 7 locations: ['L1', 'L12', 'L14', 'L19', 'L30', 'L39', 'L41']

=== DETAILED STATION ANALYSIS ===

Station L1:
  Cost: $116,538
  Covers 3 population points
  Total population covered: 32,931
  Population points covered: [53220273, 9191964890, 9198490549]

Station L12:
  Cost: $97,666
  Covers 4 population points
  Total population covered: 43,908
  Population points covered: [9178560401, 53219757, 53112191, 9178180887]

Station L14:
  Cost: $102,220
  Covers 3 population points
  Total population covered: 32,931
  Population points covered: [53149114, 53085531, 4410199251]

Station L19:
  Cost: $84,353
  Covers 3 population points
  Total population covered: 32,931
  Population points covered: [53069755, 53128588, 53140461]

Station L30:
  Cost: $101,643
  Covers 3 population points
  Total population covered: 32,931
  Population points covered: [53194403, 4003575222, 53218311]

Station L39:
  Cost: $81,248
  Covers 2 population points
  Total population covered: 21,954
  Population points covered: [53231343, 53175596]

Station L41:
  Cost: $83,616
  Covers 4 population points
  Total population covered: 43,908
  Population points covered: [53215778, 53217347, 53244343, 9200312210]

=== POPULATION COVERAGE ANALYSIS ===
Creating detailed population coverage mapping...
Coverage mapping complete:
  - Points covered: 22/200 (11.0%)
  - Population covered: 241,494/2,195,400 (11.0%)

=== OPTIMIZATION RESULTS ===
Total budget: $700,000
Used budget: $667,284
Selected 7 locations
Covered population: 241,494 out of 2,195,400 (11.00%)

=== COVERAGE VALIDATION ===
Manual coverage calculation: 241,494 (11.00%)

=== CREATING VISUALIZATIONS ===
Creating visualization with accurate coverage display...
Calculating actual coverage for 200 population points...
Actual coverage calculation:
  - Points covered: 22/200 (11.0%)
  - Population covered: 241,494/2,195,400 (11.0%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:128: UserWarning: Legend does not support handles for PatchCollection instances.
See: https://matplotlib.org/stable/tutorials/intermediate/legend_guide.html#implementing-a-custom-legend-handler
  plt.legend(fontsize=10, loc='upper right')
Calculating actual coverage for 200 population points...
Actual coverage calculation:
  - Points covered: 22/200 (11.0%)
  - Population covered: 241,494/2,195,400 (11.0%)
c:\Users\Darya\Desktop\Optimization_Project\vizualization.py:228: UserWarning: Geometry is in a geographic CRS. Results from 'centroid' are likely incorrect. Use 'GeoSeries.to_crs()' to re-project geometries to a projected CRS before this operation.

  city_center = city_gdf.centroid.iloc[0]
Interactive map saved as 'ev_charging_optimization_map_seattle.html'
Coverage statistics: 11.0% of population covered

=== OPTIMIZATION COMPLETE ===
Results: Selected 7 new charging station locations
Population coverage: 241494 out of 2195400 (11.00%)
Total cost: $667,284
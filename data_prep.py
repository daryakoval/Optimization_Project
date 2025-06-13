# =============================================================================
# STEP 2: DATA PREPARATION
# =============================================================================

import pandas as pd
from tqdm import tqdm
import geopandas as gpd
from pyproj import CRS

from constants import MAX_COVERAGE_DISTANCE


def prepare_coverage_matrix(population_points, candidate_locations):
    print("Preparing coverage matrix with visualization-consistent method...")
    
    # Use Web Mercator (same as visualization)
    if population_points.crs.is_geographic:
        pop_projected = population_points.to_crs('EPSG:3857')
        candidates_projected = candidate_locations.to_crs('EPSG:3857')
    else:
        pop_projected = population_points.copy()
        candidates_projected = candidate_locations.copy()
    
    # Create matrix using DISTANCE method (not buffer)
    coverage_data = {'population': pop_projected['population'].values}
    
    for _, candidate in tqdm(candidates_projected.iterrows(), total=len(candidates_projected)):
        location_id = candidate['location_id']
        coverage_column = []
        
        for _, pop_point in pop_projected.iterrows():
            distance = pop_point.geometry.distance(candidate.geometry)
            is_covered = 1 if distance <= MAX_COVERAGE_DISTANCE else 0
            coverage_column.append(is_covered)
        
        coverage_data[location_id] = coverage_column
    
    coverage_df = pd.DataFrame(coverage_data, index=pop_projected.index)
    
    print(f"Coverage matrix: {coverage_df.shape} - should now match visualization!")
    return coverage_df


def validate_coverage_matrix(coverage_df, population_points, candidate_locations):
    """Validate the coverage matrix for debugging purposes"""
    print("\n=== COVERAGE MATRIX VALIDATION ===")
    
    # Check dimensions
    expected_rows = len(population_points)
    expected_cols = len(candidate_locations) + 1  # +1 for population column
    actual_rows, actual_cols = coverage_df.shape
    
    print(f"Expected dimensions: {expected_rows} x {expected_cols}")
    print(f"Actual dimensions: {actual_rows} x {actual_cols}")
    
    if expected_rows != actual_rows or expected_cols != actual_cols:
        print("WARNING: Coverage matrix dimensions don't match input data!")
    
    # Check for any population points with no coverage possibilities
    location_cols = [col for col in coverage_df.columns if col != 'population']
    no_coverage_points = coverage_df[coverage_df[location_cols].sum(axis=1) == 0]
    
    if len(no_coverage_points) > 0:
        print(f"WARNING: {len(no_coverage_points)} population points have no coverage possibilities!")
        print("This means no candidate locations are within MAX_COVERAGE_DISTANCE of these points")
    
    avg_coverage_per_point = coverage_df[location_cols].sum(axis=1).mean()
    print(f"Average number of candidate locations that can cover each population point: {avg_coverage_per_point:.1f}")
    
    return len(no_coverage_points) == 0
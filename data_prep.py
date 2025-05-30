# =============================================================================
# STEP 2: DATA PREPARATION - FIXED VERSION
# =============================================================================

import pandas as pd
from tqdm import tqdm
import geopandas as gpd
from pyproj import CRS

from constants import MAX_COVERAGE_DISTANCE


def prepare_coverage_matrix(population_points, candidate_locations):
    """Create a coverage matrix showing which populations are covered by which candidate locations.
    
    FIXED VERSION: Uses proper projected coordinates for accurate distance calculations.
    """
    print("Preparing coverage matrix with accurate distance calculations...")
    
    # Convert to a projected coordinate system for accurate distance calculations
    # Use UTM zone appropriate for the location
    city_center_lon = candidate_locations.geometry.centroid.iloc[0].x
    utm_zone = int((city_center_lon + 180) / 6) + 1
    utm_crs = f"EPSG:{32600 + utm_zone}"  # Northern hemisphere UTM
    
    print(f"Using projected CRS: {utm_crs} for accurate distance calculations")
    
    # Project both datasets to UTM
    pop_projected = population_points.to_crs(utm_crs)
    candidates_projected = candidate_locations.to_crs(utm_crs)
    
    # Create a coverage matrix (population points x candidate locations)
    coverage_matrix = {}
    
    print(f"Calculating coverage for {len(pop_projected)} population points and {len(candidates_projected)} candidate locations")
    
    # For each population point
    for i, pop_point in tqdm(pop_projected.iterrows(), total=len(pop_projected), desc="Calculating coverage matrix"):
        point_id = f"P{i+1}"
        coverage_matrix[point_id] = {}
        
        # Create buffer around population point using actual meters
        buffer = pop_point.geometry.buffer(MAX_COVERAGE_DISTANCE)
        
        # For each candidate location, check if it's within the buffer
        for j, candidate in candidates_projected.iterrows():
            location_id = candidate['location_id']
            # Check if candidate is within the buffer (covered)
            coverage_matrix[point_id][location_id] = 1 if candidate.geometry.intersects(buffer) else 0
    
    # Convert to pandas DataFrame for easier handling
    coverage_df = pd.DataFrame(coverage_matrix).T
    
    # Add population data - ensure proper alignment
    coverage_df['population'] = population_points['population'].values
    
    # Calculate and display coverage statistics
    total_coverage_possibilities = len(coverage_df) * (len(coverage_df.columns) - 1)
    actual_coverage_connections = (coverage_df.drop('population', axis=1) == 1).sum().sum()
    
    print(f"Created coverage matrix with {len(coverage_df)} population points and {len(coverage_df.columns)-1} candidate locations")
    print(f"Coverage connections: {actual_coverage_connections}/{total_coverage_possibilities} ({actual_coverage_connections/total_coverage_possibilities*100:.1f}%)")
    
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
    
    # Show coverage summary
    avg_coverage_per_point = coverage_df[location_cols].sum(axis=1).mean()
    print(f"Average number of candidate locations that can cover each population point: {avg_coverage_per_point:.1f}")
    
    return len(no_coverage_points) == 0
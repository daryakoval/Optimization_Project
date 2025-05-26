# =============================================================================
# STEP 2: DATA PREPARATION
# =============================================================================

import pandas as pd
from tqdm import tqdm

from constants import MAX_COVERAGE_DISTANCE


def prepare_coverage_matrix(population_points, candidate_locations):
    """Create a coverage matrix showing which populations are covered by which candidate locations"""
    # Convert population points and candidate locations to the same CRS if needed
    if population_points.crs != candidate_locations.crs:
        population_points = population_points.to_crs(candidate_locations.crs)
    
    # Create a coverage matrix (population points x candidate locations)
    coverage_matrix = {}
    
    # For each population point
    for i, pop_point in tqdm(population_points.iterrows(), total=len(population_points), desc="Calculating coverage matrix"):
        point_id = f"P{i+1}"
        coverage_matrix[point_id] = {}
        
        # Buffer the population point by MAX_COVERAGE_DISTANCE
        buffer = pop_point.geometry.buffer(MAX_COVERAGE_DISTANCE / 111000)  # Rough conversion from meters to degrees
        
        # For each candidate location, check if it's within the buffer
        for j, candidate in candidate_locations.iterrows():
            location_id = candidate['location_id']
            coverage_matrix[point_id][location_id] = 1 if candidate.geometry.intersects(buffer) else 0
    
    # Convert to pandas DataFrame for easier handling
    coverage_df = pd.DataFrame(coverage_matrix).T
    
    # Add population data
    coverage_df['population'] = population_points['population'].values
    
    print(f"Created coverage matrix with {len(coverage_df)} population points and {len(coverage_df.columns)-1} candidate locations")
    return coverage_df

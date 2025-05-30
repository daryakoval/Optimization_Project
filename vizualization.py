import matplotlib.pyplot as plt
import folium
from pulp import *
import contextily as ctx
from pyproj import CRS
import numpy as np
import math
from constants import CITY, MAX_COVERAGE_DISTANCE

def visualize_results(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf):
    """Visualize the results using GeoPandas and Matplotlib
    
    FIXED VERSION: Properly shows covered vs uncovered population points with size-based markers and cost-based station colors
    """
    print("Creating visualization with accurate coverage display...")
    
    # Check if CRS is geographic (degrees), convert to projected (meters) if needed
    if selected_locations_gdf.crs.is_geographic:
        projected_crs = CRS.from_epsg(3857)  # Web Mercator, good general-purpose projected CRS
        city_gdf = city_gdf.to_crs(projected_crs)
        population_gdf = population_gdf.to_crs(projected_crs)
        existing_stations_gdf = existing_stations_gdf.to_crs(projected_crs)
        candidate_locations_gdf = candidate_locations_gdf.to_crs(projected_crs)
        selected_locations_gdf = selected_locations_gdf.to_crs(projected_crs)

    # FIXED: Calculate actual coverage based on distance to selected stations
    population_gdf = calculate_actual_coverage(population_gdf, selected_locations_gdf)
    
    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 15))

    # Plot city boundary
    city_gdf.plot(ax=ax, alpha=0.3, color='lightgray', edgecolor='black')

    # FIXED: Plot population density with proper covered/uncovered distinction and population-based sizing
    if 'covered' in population_gdf.columns:
        # Calculate marker sizes based on population (scale them appropriately)
        min_pop = population_gdf['population'].min()
        max_pop = population_gdf['population'].max()
        
        # Scale marker sizes between 10 and 200
        def scale_marker_size(population):
            if max_pop == min_pop:
                return 50  # Default size if all populations are the same
            normalized = (population - min_pop) / (max_pop - min_pop)
            return 10 + normalized * 190  # Scale between 10 and 200
        
        # Plot covered population in blue
        covered_pop = population_gdf[population_gdf['covered'] == True]
        if len(covered_pop) > 0:
            marker_sizes_covered = [scale_marker_size(pop) for pop in covered_pop['population']]
            covered_pop.plot(ax=ax, alpha=0.7, color='blue', 
                           markersize=marker_sizes_covered, 
                           label=f'Covered pop ({len(covered_pop)} points)')
        
        # Plot uncovered population in orange
        uncovered_pop = population_gdf[population_gdf['covered'] == False]
        if len(uncovered_pop) > 0:
            marker_sizes_uncovered = [scale_marker_size(pop) for pop in uncovered_pop['population']]
            uncovered_pop.plot(ax=ax, alpha=0.7, color='orange', 
                             markersize=marker_sizes_uncovered, 
                             label=f'Uncovered pop ({len(uncovered_pop)} points)')
    else:
        # Fallback: plot all population in blue with size-based markers
        marker_sizes_all = [scale_marker_size(pop) for pop in population_gdf['population']]
        population_gdf.plot(ax=ax, alpha=0.5, color='blue', 
                          markersize=marker_sizes_all, 
                          label='Population')

    # Plot existing stations
    if len(existing_stations_gdf) > 0:
        existing_stations_gdf.plot(ax=ax, color='green', markersize=50, marker='^', 
                                 label=f'Existing Stations ({len(existing_stations_gdf)})')

    # Plot candidate locations (in gray, smaller)
    candidate_locations_gdf.plot(ax=ax, color='gray', markersize=20, marker='o', 
                               alpha=0.5, label=f'Candidate Locations ({len(candidate_locations_gdf)})')

    # Plot selected locations with cost-based coloring (prominent stars)
    if len(selected_locations_gdf) > 0 and 'station_cost' in selected_locations_gdf.columns:
        # Determine cost-based colors
        min_cost = selected_locations_gdf['station_cost'].min()
        max_cost = selected_locations_gdf['station_cost'].max()
        
        # Create color mapping: cheap = light red, expensive = dark red
        def get_cost_color(cost):
            if max_cost == min_cost:
                return 'red'  # Default red if all costs are the same
            normalized = (cost - min_cost) / (max_cost - min_cost)
            # Use RGB values: light red (255, 150, 150) to dark red (139, 0, 0)
            r = int(255 - normalized * (255 - 139))
            g = int(150 - normalized * 150)
            b = int(150 - normalized * 150)
            return f'#{r:02x}{g:02x}{b:02x}'
        
        colors = [get_cost_color(cost) for cost in selected_locations_gdf['station_cost']]
        
        selected_locations_gdf.plot(ax=ax, color=colors, markersize=100, marker='*', 
                                  label=f'Selected New Stations ({len(selected_locations_gdf)})')
        
        # Add a color legend for costs
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#ffaaaa', label=f'Cheap stations (${min_cost:,})'),
            Patch(facecolor='#8b0000', label=f'Expensive stations (${max_cost:,})')
        ]
        ax.legend(handles=legend_elements, loc='upper left', title='Station Costs')
    else:
        # Fallback: plot all selected locations in red
        selected_locations_gdf.plot(ax=ax, color='red', markersize=100, marker='*', 
                                  label=f'Selected New Stations ({len(selected_locations_gdf)})')

    # Add coverage circles (proper radius in projected coordinates)
    if len(selected_locations_gdf) > 0:
        reachable_area = selected_locations_gdf.copy()
        reachable_area['geometry'] = reachable_area.buffer(MAX_COVERAGE_DISTANCE)
        reachable_area.plot(ax=ax, facecolor='red', alpha=0.1, edgecolor='red', 
                          linewidth=2, linestyle='--', 
                          label=f'{MAX_COVERAGE_DISTANCE}m Coverage Areas')

    # Add title with coverage statistics
    coverage_stats = get_coverage_statistics(population_gdf)
    title = f'EV Charging Station Optimization for {CITY}\n'
    title += f'Coverage: {coverage_stats["covered_pop"]:,.0f}/{coverage_stats["total_pop"]:,.0f} people '
    title += f'({coverage_stats["coverage_percentage"]:.1f}%)'
    
    plt.title(title, fontsize=16)
    plt.legend(fontsize=10, loc='upper right')

    # Add background map
    try:
        ctx.add_basemap(ax, crs=city_gdf.crs.to_string())
    except Exception as e:
        print(f"Couldn't add basemap: {e}")
        
    city_parts = CITY.split(',')
    city_name = city_parts[0].strip().lower().replace(" ", "_")
    plt.tight_layout()
    plt.savefig(f'ev_charging_optimization_results_{city_name}.png', dpi=300, bbox_inches='tight')
    plt.show()


def calculate_actual_coverage(population_gdf, selected_locations_gdf):
    """Calculate actual coverage based on distance to selected stations
    
    This ensures the visualization matches the optimization results
    """
    if len(selected_locations_gdf) == 0:
        population_gdf['covered'] = False
        return population_gdf
    
    print(f"Calculating actual coverage for {len(population_gdf)} population points...")
    
    # Ensure both are in the same projected CRS for accurate distance calculation
    if population_gdf.crs != selected_locations_gdf.crs:
        selected_locations_gdf = selected_locations_gdf.to_crs(population_gdf.crs)
    
    # For each population point, check if it's within MAX_COVERAGE_DISTANCE of any selected station
    covered_flags = []
    
    for idx, pop_point in population_gdf.iterrows():
        is_covered = False
        
        # Check distance to each selected station
        for _, station in selected_locations_gdf.iterrows():
            distance = pop_point.geometry.distance(station.geometry)
            if distance <= MAX_COVERAGE_DISTANCE:
                is_covered = True
                break
        
        covered_flags.append(is_covered)
    
    population_gdf['covered'] = covered_flags
    
    # Print coverage statistics
    covered_count = sum(covered_flags)
    total_count = len(covered_flags)
    covered_pop = population_gdf[population_gdf['covered']]['population'].sum()
    total_pop = population_gdf['population'].sum()
    
    print(f"Actual coverage calculation:")
    print(f"  - Points covered: {covered_count}/{total_count} ({covered_count/total_count*100:.1f}%)")
    print(f"  - Population covered: {covered_pop:,.0f}/{total_pop:,.0f} ({covered_pop/total_pop*100:.1f}%)")
    
    return population_gdf


def get_coverage_statistics(population_gdf):
    """Get coverage statistics from population GeoDataFrame"""
    if 'covered' not in population_gdf.columns:
        return {
            'covered_pop': 0,
            'total_pop': population_gdf['population'].sum(),
            'coverage_percentage': 0
        }
    
    covered_pop = population_gdf[population_gdf['covered']]['population'].sum()
    total_pop = population_gdf['population'].sum()
    coverage_percentage = (covered_pop / total_pop * 100) if total_pop > 0 else 0
    
    return {
        'covered_pop': covered_pop,
        'total_pop': total_pop,
        'coverage_percentage': coverage_percentage
    }

def create_interactive_map(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf):
    """Create an interactive map using Folium
    
    FIXED VERSION: Shows proper coverage distinction and correct coverage areas
    """
    # FIXED: Calculate actual coverage BEFORE any coordinate transformations
    # Make copies to avoid modifying originals
    population_work = population_gdf.copy()
    selected_work = selected_locations_gdf.copy()
    
    # Ensure we're working in projected coordinates for accurate distance calculation
    if population_work.crs.is_geographic:
        projected_crs = CRS.from_epsg(3857)  # Web Mercator
        population_work = population_work.to_crs(projected_crs)
        selected_work = selected_work.to_crs(projected_crs)
    
    # Calculate coverage in projected coordinates
    population_work = calculate_actual_coverage(population_work, selected_work)
    
    # Get city center (convert to geographic coordinates if needed)
    if city_gdf.crs.is_geographic:
        city_center = city_gdf.centroid.iloc[0]
    else:
        # Convert to geographic coordinates for Folium
        city_center = city_gdf.to_crs('EPSG:4326').centroid.iloc[0]
    
    # Create a map centered on the city
    m = folium.Map(location=[city_center.y, city_center.x], zoom_start=12, tiles='OpenStreetMap')
    
    # Add city boundary (convert to geographic if needed)
    city_geo = city_gdf.to_crs('EPSG:4326') if not city_gdf.crs.is_geographic else city_gdf
    folium.GeoJson(
        city_geo,
        style_function=lambda x: {'color': 'black', 'weight': 2, 'fillOpacity': 0.1}
    ).add_to(m)
    
    # Convert population data to geographic coordinates for Folium, preserving coverage info
    population_geo = population_work.to_crs('EPSG:4326')
    
    # Add population points with coverage distinction
    if 'covered' in population_geo.columns:
        # Covered population points (blue)
        covered_pop = population_geo[population_geo['covered'] == True]
        covered_group = folium.FeatureGroup(name=f'Covered Population ({len(covered_pop)} points)')
        for idx, row in covered_pop.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=max(3, min(15, row['population'] / 1000)),
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.6,
                tooltip=f"Covered Population: {row['population']:,}"
            ).add_to(covered_group)
        covered_group.add_to(m)
        
        # Uncovered population points (orange)
        uncovered_pop = population_geo[population_geo['covered'] == False]
        uncovered_group = folium.FeatureGroup(name=f'Uncovered Population ({len(uncovered_pop)} points)')
        for idx, row in uncovered_pop.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=max(3, min(15, row['population'] / 1000)),
                color='orange',
                fill=True,
                fill_color='orange',
                fill_opacity=0.6,
                tooltip=f"Uncovered Population: {row['population']:,}"
            ).add_to(uncovered_group)
        uncovered_group.add_to(m)
    else:
        # Fallback: all population in blue
        population_group = folium.FeatureGroup(name='Population Density')
        for idx, row in population_geo.iterrows():
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=max(5, min(20, row['population'] / 1000)),
                color='blue',
                fill=True,
                fill_color='blue',
                fill_opacity=0.2,
                tooltip=f"Population: {row['population']:,}"
            ).add_to(population_group)
        population_group.add_to(m)
    
    # Convert existing stations to geographic coordinates
    existing_geo = existing_stations_gdf.to_crs('EPSG:4326') if not existing_stations_gdf.crs.is_geographic else existing_stations_gdf
    
    # Add existing stations
    if len(existing_geo) > 0:
        existing_stations = folium.FeatureGroup(name='Existing Charging Stations')
        for idx, row in existing_geo.iterrows():
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=folium.Icon(color='green', icon='plug', prefix='fa'),
                popup=f"Existing Station<br>Name: {row.get('name', 'Unknown')}<br>Address: {row.get('address', 'Unknown')}"
            ).add_to(existing_stations)
        existing_stations.add_to(m)
    
    # Convert candidate locations to geographic coordinates
    candidates_geo = candidate_locations_gdf.to_crs('EPSG:4326') if not candidate_locations_gdf.crs.is_geographic else candidate_locations_gdf
    selected_geo = selected_locations_gdf.to_crs('EPSG:4326') if not selected_locations_gdf.crs.is_geographic else selected_locations_gdf
    
    # Add candidate locations
    candidates = folium.FeatureGroup(name='Candidate Locations (not selected)')
    for idx, row in candidates_geo.iterrows():
        if row['location_id'] not in selected_geo['location_id'].values:
            folium.CircleMarker(
                location=[row.geometry.y, row.geometry.x],
                radius=3,
                color='gray',
                fill=True,
                fill_color='gray',
                fill_opacity=0.5,
                tooltip=f"Candidate Location {row['location_id']}"
            ).add_to(candidates)
    candidates.add_to(m)
    
    # Add selected locations with cost-based color using CircleMarker
    selected = folium.FeatureGroup(name=f'Selected New Stations ({len(selected_geo)})')

    if 'station_cost' in selected_geo.columns:
        min_cost = selected_geo['station_cost'].min()
        max_cost = selected_geo['station_cost'].max()

        def get_folium_color(cost):
            if max_cost == min_cost:
                return 'red'
            norm = (cost - min_cost) / (max_cost - min_cost)
            if norm < 0.33:
                return 'lightred'
            elif norm < 0.66:
                return 'red'
            else:
                return 'darkred'

        for _, row in selected_geo.iterrows():
            color = get_folium_color(row['station_cost'])
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=folium.Icon(color=color, icon='bolt', prefix='fa'),
                tooltip=f"Station ID: {row['location_id']}<br>Cost: ${row['station_cost']:,}"
            ).add_to(selected)
    else:
        for _, row in selected_geo.iterrows():
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=folium.Icon(color='red', icon='bolt', prefix='fa'),
                tooltip=f"Station ID: {row['location_id']}"
            ).add_to(selected)

    selected.add_to(m)
    
    # FIXED: Add coverage circles with proper radius calculation
    # Folium circles need radius in meters, but we need to account for geographic distortion
    coverage = folium.FeatureGroup(name=f'Coverage Areas ({MAX_COVERAGE_DISTANCE}m radius)')
    for idx, row in selected_geo.iterrows():
        # For better accuracy, we can approximate the radius in degrees
        # This is a rough approximation: 1 degree ≈ 111,000 meters at the equator
        # For better accuracy, you might want to use a more sophisticated conversion
        lat = row.geometry.y
        # Adjust for latitude (meters per degree longitude varies by latitude)
        meters_per_degree_lat = 111000
        meters_per_degree_lon = 111000 * math.cos(math.radians(lat))
        
        # Convert coverage distance to approximate degrees
        radius_degrees = MAX_COVERAGE_DISTANCE / meters_per_degree_lat
        
        folium.Circle(
            location=[row.geometry.y, row.geometry.x],
            radius=MAX_COVERAGE_DISTANCE-300,  # Folium expects radius in meters
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.1,
            weight=2,
            popup=f"Coverage area: {MAX_COVERAGE_DISTANCE}m radius"
        ).add_to(coverage)
    coverage.add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Add coverage statistics to the map title
    coverage_stats = get_coverage_statistics(population_work)  # Use the working copy with coverage data
    map_title = f"""
    <h3 align="center" style="font-size:16px"><b>EV Charging Station Optimization for {CITY}</b></h3>
    <p align="center">Coverage: {coverage_stats["covered_pop"]:,.0f}/{coverage_stats["total_pop"]:,.0f} people 
    ({coverage_stats["coverage_percentage"]:.1f}%)</p>
    """
    m.get_root().html.add_child(folium.Element(map_title))
    
    # Save the map
    city_parts = CITY.split(',')
    city_name = city_parts[0].strip().lower().replace(" ", "_")
    m.save(f'ev_charging_optimization_map_{city_name}.html')
    print(f"Interactive map saved as 'ev_charging_optimization_map_{city_name}.html'")
    print(f"Coverage statistics: {coverage_stats['coverage_percentage']:.1f}% of population covered")
    
    return m
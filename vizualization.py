
import matplotlib.pyplot as plt
import folium
from pulp import *
import contextily as ctx

from constants import CITY, MAX_COVERAGE_DISTANCE


def visualize_results(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf):
    """Visualize the results using GeoPandas and Matplotlib"""
    # Set up the figure
    fig, ax = plt.subplots(figsize=(15, 15))
    
    # Plot city boundary
    city_gdf.plot(ax=ax, alpha=0.3, color='lightgray', edgecolor='black')
    
    # Plot population density (sized by population)
    population_gdf.plot(ax=ax, alpha=0.5, color='blue', markersize=population_gdf['population']/500, label='Population')
    
    # Plot existing stations
    if len(existing_stations_gdf) > 0:
        existing_stations_gdf.plot(ax=ax, color='green', markersize=50, marker='^', label='Existing Stations')
    
    # Plot candidate locations
    candidate_locations_gdf.plot(ax=ax, color='gray', markersize=30, marker='o', label='Candidate Locations')
    
    # Plot selected locations
    selected_locations_gdf.plot(ax=ax, color='red', markersize=80, marker='*', label='Selected New Stations')
    
    # Add labels and legend
    plt.title(f'EV Charging Station Optimization for {CITY}', fontsize=16)
    plt.legend(fontsize=12)
    
    # Add background map
    try:
        ctx.add_basemap(ax, crs=city_gdf.crs.to_string())
    except Exception as e:
        print(f"Couldn't add basemap: {e}")
    
    plt.tight_layout()
    plt.savefig('ev_charging_optimization_results.png', dpi=300)
    plt.show()

def create_interactive_map(city_gdf, population_gdf, existing_stations_gdf, candidate_locations_gdf, selected_locations_gdf):
    """Create an interactive map using Folium"""
    # Get city center
    city_center = city_gdf.centroid.iloc[0]
    
    # Create a map centered on the city
    m = folium.Map(location=[city_center.y, city_center.x], zoom_start=12, tiles='OpenStreetMap')
    
    # Add city boundary
    folium.GeoJson(
        city_gdf,
        style_function=lambda x: {'color': 'black', 'weight': 2, 'fillOpacity': 0.1}
    ).add_to(m)
    
    # Add population density as a heatmap-like visualization
    for idx, row in population_gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=max(5, min(20, row['population'] / 1000)),  # Scale circle size by population
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.2,
            tooltip=f"Population: {row['population']}"
        ).add_to(m)
    
    # Add existing stations
    if len(existing_stations_gdf) > 0:
        existing_stations = folium.FeatureGroup(name='Existing Charging Stations')
        for idx, row in existing_stations_gdf.iterrows():
            folium.Marker(
                location=[row.geometry.y, row.geometry.x],
                icon=folium.Icon(color='green', icon='plug', prefix='fa'),
                popup=f"Existing Station<br>Name: {row['name']}<br>Address: {row['address']}"
            ).add_to(existing_stations)
        existing_stations.add_to(m)
    
    # Add candidate locations
    candidates = folium.FeatureGroup(name='Candidate Locations')
    for idx, row in candidate_locations_gdf.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=5,
            color='gray',
            fill=True,
            fill_color='gray',
            fill_opacity=0.7,
            tooltip=f"Candidate Location {row['location_id']}"
        ).add_to(candidates)
    candidates.add_to(m)
    
    # Add selected locations
    selected = folium.FeatureGroup(name='Selected New Stations')
    for idx, row in selected_locations_gdf.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            icon=folium.Icon(color='red', icon='bolt', prefix='fa'),
            popup=f"New Charging Station<br>Location ID: {row['location_id']}"
        ).add_to(selected)
    selected.add_to(m)
    
    # Add coverage circles for selected locations
    coverage = folium.FeatureGroup(name='Coverage Areas')
    for idx, row in selected_locations_gdf.iterrows():
        folium.Circle(
            location=[row.geometry.y, row.geometry.x],
            radius=MAX_COVERAGE_DISTANCE,  # meters
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.1
        ).add_to(coverage)
    coverage.add_to(m)
    
    # Add layer control
    folium.LayerControl().add_to(m)
    
    # Save the map
    m.save('ev_charging_optimization_map.html')
    print("Interactive map saved as 'ev_charging_optimization_map.html'")
    
    return m
import folium
import os

os.makedirs("output", exist_ok=True)

# Nagpur Coordinates
nagpur = [21.1458, 79.0882]

# Create Map
m = folium.Map(
    location=nagpur,
    zoom_start=12
)

# Hospitals
folium.Marker(
    [21.1498,79.0821],
    popup="Hospital",
    icon=folium.Icon(color="red",icon="plus-sign")
).add_to(m)

# School
folium.Marker(
    [21.1600,79.1000],
    popup="School",
    icon=folium.Icon(color="blue",icon="education")
).add_to(m)

# Park
folium.Marker(
    [21.1350,79.0750],
    popup="Park",
    icon=folium.Icon(color="green")
).add_to(m)

# Water Body
folium.Marker(
    [21.1200,79.0950],
    popup="Water Body",
    icon=folium.Icon(color="cadetblue")
).add_to(m)

# Save Map
m.save("output/Nagpur_Map.html")

print("Interactive Map Created Successfully")
print("Output: output/Nagpur_Map.html")
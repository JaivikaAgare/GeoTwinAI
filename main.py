import os
import osmnx as ox

# Create output folder
os.makedirs("output", exist_ok=True)

place = "Nagpur, Maharashtra, India"

print("Downloading Buildings...")
buildings = ox.features_from_place(place, tags={"building": True})
buildings.to_csv("output/Nagpur_Buildings.csv")

print("Downloading Roads...")
graph = ox.graph_from_place(place, network_type="drive")
roads = ox.graph_to_gdfs(graph, nodes=False)
roads.to_csv("output/Nagpur_Roads.csv")

print("Downloading Hospitals...")
hospitals = ox.features_from_place(place, tags={"amenity": "hospital"})
hospitals.to_csv("output/Nagpur_Hospitals.csv")

print("Downloading Schools...")
schools = ox.features_from_place(place, tags={"amenity": "school"})
schools.to_csv("output/Nagpur_Schools.csv")

print("Downloading Parks...")
parks = ox.features_from_place(place, tags={"leisure": "park"})
parks.to_csv("output/Nagpur_Parks.csv")

print("Downloading Water Bodies...")
water = ox.features_from_place(
    place,
    tags={
        "natural": "water",
        "water": True
    }
)
water.to_csv("output/Nagpur_WaterBodies.csv")

print("\n✅ All Nagpur datasets downloaded successfully!")
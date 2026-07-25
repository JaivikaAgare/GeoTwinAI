from pystac_client import Client

print("Connecting to Microsoft Planetary Computer...")

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

bbox = [78.95, 21.05, 79.20, 21.25]

search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=bbox,
    datetime="2024-01-01/2024-12-31",
    limit=5
)

items = list(search.items())

print(f"Found {len(items)} Sentinel-2 images")

for i, item in enumerate(items):
    print(f"{i+1}. {item.id}")
from pystac_client import Client
import planetary_computer
import requests
import os

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

bbox = [78.95, 21.05, 79.20, 21.25]

search = catalog.search(
    collections=["sentinel-2-l2a"],
    bbox=bbox,
    datetime="2024-01-01/2024-12-31",
    limit=1
)

items = list(search.items())

if not items:
    print("No image found.")
    exit()

item = planetary_computer.sign(items[0])

asset = item.assets["visual"]

url = asset.href

os.makedirs("satellite/data", exist_ok=True)

output = "satellite/data/nagpur_visual.tif"

print("Downloading image...")

response = requests.get(url, stream=True)

with open(output, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Download completed!")
print(output)
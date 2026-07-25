from pystac_client import Client
import planetary_computer
import requests
import os

print("Connecting to Microsoft Planetary Computer...")

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

os.makedirs("satellite/data", exist_ok=True)

bands = {
    "B04": "B04.tif",
    "B08": "B08.tif"
}

for band, filename in bands.items():

    print(f"Downloading {band}...")

    url = item.assets[band].href

    response = requests.get(url, stream=True)

    with open(f"satellite/data/{filename}", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

print("\nDownload Completed Successfully!")
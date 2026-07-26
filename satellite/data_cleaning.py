import os
import rasterio
import numpy as np

print("="*50)
print("DATA CLEANING STARTED")
print("="*50)

RED = "satellite/data/B04.tif"
NIR = "satellite/data/B08.tif"
VISUAL = "satellite/data/nagpur_visual.tif"

for file in [RED, NIR, VISUAL]:
    if os.path.exists(file):
        print(f"Found: {file}")
    else:
        print(f"Missing: {file}")

print("\nLoading images...")

with rasterio.open(RED) as src:
    red = src.read(1, out_shape=(500,500)).astype(np.float32)

with rasterio.open(NIR) as src:
    nir = src.read(1, out_shape=(500,500)).astype(np.float32)

with rasterio.open(VISUAL) as src:
    visual = src.read(out_shape=(src.count,500,500)).astype(np.float32)

red = np.nan_to_num(red)
nir = np.nan_to_num(nir)
visual = np.nan_to_num(visual)

red[red < 0] = 0
nir[nir < 0] = 0
visual[visual < 0] = 0

print("\nCleaning Completed Successfully")
print("B04 Shape :", red.shape)
print("B08 Shape :", nir.shape)
print("Visual Shape :", visual.shape)

print("="*50)
print("DATA CLEANING FINISHED")
print("="*50)
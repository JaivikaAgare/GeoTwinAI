import os
import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder
os.makedirs("output", exist_ok=True)

# Read Bands
red = rasterio.open("satellite/data/B04.tif").read(1).astype(float)
nir = rasterio.open("satellite/data/B08.tif").read(1).astype(float)

# Calculate NDVI
ndvi = (nir - red) / (nir + red + 1e-10)

# Heat Index
heat = 1 - ((ndvi + 1) / 2)

# Save CSV
df = pd.DataFrame({
    "HeatIndex": heat.flatten()
})

df.to_csv("output/Nagpur_HeatMap.csv", index=False)

# Save PNG
plt.figure(figsize=(8,6))
plt.imshow(heat, cmap="hot")
plt.colorbar(label="Heat Intensity")
plt.title("Nagpur Heat Map")
plt.axis("off")

plt.savefig(
    "output/Nagpur_HeatMap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Heat Map Generated Successfully")
print("CSV Saved -> output/Nagpur_HeatMap.csv")
print("PNG Saved -> output/Nagpur_HeatMap.png")
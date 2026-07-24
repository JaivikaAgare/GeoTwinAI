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

# Land Use Classification
landuse = np.zeros(ndvi.shape, dtype=np.uint8)

# Rule-based Classification
landuse[ndvi < 0] = 1                     # Water
landuse[(ndvi >= 0) & (ndvi < 0.2)] = 2   # Built-up
landuse[(ndvi >= 0.2) & (ndvi < 0.5)] = 3 # Vegetation
landuse[ndvi >= 0.5] = 4                  # Dense Vegetation

# Labels
labels = {
    1: "Water",
    2: "Built-up",
    3: "Vegetation",
    4: "Dense Vegetation"
}

# Save CSV
df = pd.DataFrame({
    "LandUse": landuse.flatten()
})

df["Class"] = df["LandUse"].map(labels)

df.to_csv("output/Nagpur_LandUse.csv", index=False)

# Save PNG
plt.figure(figsize=(8,6))
plt.imshow(landuse, cmap="terrain")
plt.colorbar(label="Land Use Class")
plt.title("Nagpur Land Use Classification")
plt.axis("off")

plt.savefig("output/Nagpur_LandUse.png", dpi=300, bbox_inches="tight")
plt.close()

print("Land Use Classification Completed Successfully")
print("CSV Saved: output/Nagpur_LandUse.csv")
print("PNG Saved: output/Nagpur_LandUse.png")
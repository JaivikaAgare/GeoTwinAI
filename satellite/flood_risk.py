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

# Flood Risk Classification
# 1 = High Risk
# 2 = Medium Risk
# 3 = Low Risk

risk = np.zeros(ndvi.shape, dtype=np.uint8)

risk[ndvi < 0] = 1
risk[(ndvi >= 0) & (ndvi < 0.3)] = 2
risk[ndvi >= 0.3] = 3

labels = {
    1: "High Risk",
    2: "Medium Risk",
    3: "Low Risk"
}

# Save CSV
df = pd.DataFrame({
    "FloodRisk": risk.flatten()
})

df["Class"] = df["FloodRisk"].map(labels)

df.to_csv("output/Nagpur_FloodRisk.csv", index=False)

# Save Image
plt.figure(figsize=(8,6))
plt.imshow(risk, cmap="RdYlGn")
plt.title("Nagpur Flood Risk Map")
plt.colorbar(label="Flood Risk")
plt.axis("off")

plt.savefig(
    "output/Nagpur_FloodRisk.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Flood Risk Analysis Completed Successfully")
print("CSV Saved -> output/Nagpur_FloodRisk.csv")
print("PNG Saved -> output/Nagpur_FloodRisk.png")
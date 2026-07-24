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

# NDVI
ndvi = (nir - red) / (nir + red + 1e-10)

# Built-up Detection
builtup = np.zeros(ndvi.shape, dtype=np.uint8)

# Rule:
# NDVI < 0.2 = Built-up
builtup[ndvi < 0.2] = 1
builtup[ndvi >= 0.2] = 0

# Save CSV
df = pd.DataFrame({
    "BuiltUp": builtup.flatten()
})

df["Class"] = df["BuiltUp"].map({
    0: "Non Built-up",
    1: "Built-up"
})

df.to_csv("output/Nagpur_BuiltUp.csv", index=False)

# Save PNG
plt.figure(figsize=(8,6))
plt.imshow(builtup, cmap="gray")
plt.title("Nagpur Built-up Area")
plt.colorbar(label="Built-up")
plt.axis("off")

plt.savefig("output/Nagpur_BuiltUp.png",
            dpi=300,
            bbox_inches="tight")

plt.close()

print("Built-up Detection Completed Successfully")
print("CSV Saved -> output/Nagpur_BuiltUp.csv")
print("PNG Saved -> output/Nagpur_BuiltUp.png")
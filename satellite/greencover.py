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

# Green Cover Detection
green = np.zeros(ndvi.shape, dtype=np.uint8)

green[ndvi >= 0.3] = 1

green_percentage = (np.sum(green == 1) / green.size) * 100

# Save CSV
df = pd.DataFrame({
    "GreenCover": green.flatten()
})

df["Class"] = df["GreenCover"].map({
    0: "Non Green",
    1: "Green Area"
})

df.to_csv("output/Nagpur_GreenCover.csv", index=False)

# Save PNG
plt.figure(figsize=(8,6))
plt.imshow(green, cmap="Greens")
plt.title(f"Nagpur Green Cover ({green_percentage:.2f}%)")
plt.colorbar(label="Green Cover")
plt.axis("off")

plt.savefig(
    "output/Nagpur_GreenCover.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Green Cover Analysis Completed")
print(f"Green Cover = {green_percentage:.2f}%")
print("CSV Saved -> output/Nagpur_GreenCover.csv")
print("PNG Saved -> output/Nagpur_GreenCover.png")
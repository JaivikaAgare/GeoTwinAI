import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("output", exist_ok=True)

print("Opening image...")

with rasterio.open("satellite/data/nagpur_visual.tif") as src:

    # Read a smaller preview
    red = src.read(1, out_shape=(500, 500)).astype(float)
    green = src.read(2, out_shape=(500, 500)).astype(float)
    blue = src.read(3, out_shape=(500, 500)).astype(float)

print("Calculating Green Cover...")

# Simple Green Cover Index
green_index = green / (red + blue + 1e-10)

green_cover = np.where(
    green_index > 0.45,
    "Dense Vegetation",
    np.where(
        green_index > 0.30,
        "Moderate Vegetation",
        "Low Vegetation"
    )
)

df = pd.DataFrame({
    "GreenIndex": green_index.flatten(),
    "GreenCover": green_cover.flatten()
})

df.to_csv("output/Nagpur_GreenCover.csv", index=False)

plt.imshow(green_index, cmap="Greens")
plt.colorbar(label="Green Index")
plt.title("Nagpur Green Cover")
plt.savefig("output/Nagpur_GreenCover.png")
plt.close()

print("Green Cover Analysis Completed!")
print("Output saved as:")
print("output/Nagpur_GreenCover.csv")
print("output/Nagpur_GreenCover.png")
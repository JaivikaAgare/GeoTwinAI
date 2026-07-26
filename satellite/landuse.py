import os
import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)

print("=" * 50)
print("Opening Satellite Image...")
print("=" * 50)

with rasterio.open("satellite/data/nagpur_visual.tif") as src:

    red = src.read(1, out_shape=(500, 500)).astype(float)
    green = src.read(2, out_shape=(500, 500)).astype(float)
    blue = src.read(3, out_shape=(500, 500)).astype(float)

print("Image Loaded Successfully")

# -------------------------
# LAND USE CLASSIFICATION
# -------------------------

landuse = np.zeros(red.shape)

# Water
landuse[(blue > green) & (blue > red)] = 1

# Vegetation
landuse[(green > red) & (green > blue)] = 2

# Built-up
landuse[(red > green) & (red > blue)] = 3

# Bare Land
landuse[landuse == 0] = 4

# -------------------------
# GRID SUMMARY
# -------------------------

GRID = 20

rows, cols = landuse.shape

cell_h = rows // GRID
cell_w = cols // GRID

records = []

grid = 1

for r in range(GRID):

    for c in range(GRID):

        rs = r * cell_h
        re = (r + 1) * cell_h

        cs = c * cell_w
        ce = (c + 1) * cell_w

        block = landuse[rs:re, cs:ce]

        total = block.size

        water = np.sum(block == 1)
        vegetation = np.sum(block == 2)
        built = np.sum(block == 3)
        bare = np.sum(block == 4)

        values = {
            "Water": water,
            "Vegetation": vegetation,
            "Built-up": built,
            "Bare Land": bare
        }

        dominant = max(values, key=values.get)

        records.append({

            "Grid_ID": f"G{grid}",

            "Water_%": round(water * 100 / total, 2),

            "Vegetation_%": round(vegetation * 100 / total, 2),

            "BuiltUp_%": round(built * 100 / total, 2),

            "BareLand_%": round(bare * 100 / total, 2),

            "Dominant_Class": dominant

        })

        grid += 1

df = pd.DataFrame(records)

csv_path = "output/Nagpur_LandUse.csv"

df.to_csv(csv_path, index=False)

print("CSV Saved Successfully")

# -------------------------
# SAVE PNG
# -------------------------

plt.figure(figsize=(10,10))

plt.imshow(landuse, cmap="terrain")

cbar = plt.colorbar()

cbar.set_ticks([1,2,3,4])

cbar.set_ticklabels([
    "Water",
    "Vegetation",
    "Built-up",
    "Bare Land"
])

plt.title("Nagpur Land Use Classification")

plt.axis("off")

png_path = "output/Nagpur_LandUse.png"

plt.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("PNG Saved Successfully")

print("=" * 50)
print("LAND USE ANALYSIS COMPLETED")
print("=" * 50)

print(f"CSV : {csv_path}")
print(f"PNG : {png_path}")

print("\nPreview:")
print(df.head())
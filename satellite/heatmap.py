import os
import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create output folder
os.makedirs("output", exist_ok=True)

print("Reading Satellite Bands...")

# Read Red & NIR bands
red = rasterio.open("satellite/data/B04.tif").read(
    1,
    out_shape=(500, 500)
).astype(float)

nir = rasterio.open("satellite/data/B08.tif").read(
    1,
    out_shape=(500, 500)
).astype(float)

# Calculate NDVI
ndvi = (nir - red) / (nir + red + 1e-10)

# Heat Index
heat = 1 - ((ndvi + 1) / 2)

GRID = 20

rows, cols = heat.shape

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

        block = heat[rs:re, cs:ce]

        avg_heat = np.mean(block)

        if avg_heat >= 0.70:
            level = "High"

        elif avg_heat >= 0.40:
            level = "Medium"

        else:
            level = "Low"

        records.append({

            "Grid_ID": f"G{grid}",

            "Average_Heat_Index": round(avg_heat, 3),

            "Heat_Level": level

        })

        grid += 1

# Save CSV
df = pd.DataFrame(records)

csv_path = "output/Nagpur_HeatMap.csv"

df.to_csv(csv_path, index=False)

print("CSV Saved Successfully")

# Save PNG
plt.figure(figsize=(8,8))

plt.imshow(heat, cmap="hot")

plt.colorbar(label="Heat Index")

plt.title("Nagpur Heat Map")

plt.axis("off")

png_path = "output/Nagpur_HeatMap.png"

plt.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("PNG Saved Successfully")

print("=" * 50)
print("HEAT MAP ANALYSIS COMPLETED")
print("=" * 50)

print(f"CSV : {csv_path}")
print(f"PNG : {png_path}")

print("\nPreview:")
print(df.head())
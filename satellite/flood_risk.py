import os
import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

os.makedirs("output", exist_ok=True)

print("Reading Satellite Bands...")

red = rasterio.open("satellite/data/B04.tif").read(
    1,
    out_shape=(500, 500)
).astype(float)

nir = rasterio.open("satellite/data/B08.tif").read(
    1,
    out_shape=(500, 500)
).astype(float)

print("Calculating NDVI...")

ndvi = (nir - red) / (nir + red + 1e-10)

# Flood Risk Classification
risk = np.zeros(ndvi.shape)

risk[ndvi < 0] = 1
risk[(ndvi >= 0) & (ndvi < 0.3)] = 2
risk[ndvi >= 0.3] = 3

GRID = 20

rows, cols = risk.shape

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

        block = risk[rs:re, cs:ce]

        total = block.size

        high = np.sum(block == 1)
        medium = np.sum(block == 2)
        low = np.sum(block == 3)

        values = {
            "High Risk": high,
            "Medium Risk": medium,
            "Low Risk": low
        }

        dominant = max(values, key=values.get)

        records.append({

            "Grid_ID": f"G{grid}",

            "HighRisk_%": round(high * 100 / total, 2),

            "MediumRisk_%": round(medium * 100 / total, 2),

            "LowRisk_%": round(low * 100 / total, 2),

            "Dominant_Risk": dominant

        })

        grid += 1

df = pd.DataFrame(records)

csv_path = "output/Nagpur_FloodRisk.csv"

df.to_csv(csv_path, index=False)

print("CSV Saved Successfully")

plt.figure(figsize=(8,8))

plt.imshow(risk, cmap="RdYlGn_r")

plt.colorbar(label="Flood Risk")

plt.title("Nagpur Flood Risk Map")

plt.axis("off")

png_path = "output/Nagpur_FloodRisk.png"

plt.savefig(
    png_path,
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("PNG Saved Successfully")

print("="*50)
print("FLOOD RISK ANALYSIS COMPLETED")
print("="*50)

print(df.head())
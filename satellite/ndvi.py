import rasterio
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

red = rasterio.open("satellite/data/B04.tif").read(1).astype(float)
nir = rasterio.open("satellite/data/B08.tif").read(1).astype(float)

ndvi = (nir - red) / (nir + red + 1e-10)

# Save NDVI Image
plt.imshow(ndvi, cmap="RdYlGn")
plt.colorbar(label="NDVI")
plt.title("Nagpur NDVI")
plt.savefig("output/Nagpur_NDVI.png")
plt.close()

# Save NDVI CSV
df = pd.DataFrame({
    "NDVI": ndvi.flatten()
})

df.to_csv("output/Nagpur_NDVI.csv", index=False)

print("NDVI Image Generated Successfully")
print("NDVI CSV Generated Successfully")
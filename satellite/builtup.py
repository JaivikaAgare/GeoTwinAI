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

print("Detecting Built-up Areas...")

# Simple Built-up Index
builtup_index = (red + green) / (blue + 1e-10)

builtup = np.where(
    builtup_index > 2.0,
    "Built-up",
    "Non Built-up"
)

df = pd.DataFrame({
    "BuiltUpIndex": builtup_index.flatten(),
    "BuiltUp": builtup.flatten()
})

df.to_csv("output/Nagpur_BuiltUp.csv", index=False)

plt.imshow(builtup_index, cmap="gray")
plt.colorbar(label="Built-up Index")
plt.title("Nagpur Built-up Area")
plt.savefig("output/Nagpur_BuiltUp.png")
plt.close()

print("Built-up Analysis Completed!")
print("Output saved as:")
print("output/Nagpur_BuiltUp.csv")
print("output/Nagpur_BuiltUp.png")
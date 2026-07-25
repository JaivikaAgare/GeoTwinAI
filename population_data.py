import pandas as pd
import os

os.makedirs("output", exist_ok=True)

data = {
    "City": ["Nagpur"],
    "Population": [2405665],
    "Area_km2": [217.65]
}

df = pd.DataFrame(data)

df["Population_Density"] = (
    df["Population"] / df["Area_km2"]
).round(2)

df.to_csv("output/Nagpur_Population.csv", index=False)

print(df)
print("\nNagpur_Population.csv created successfully!")
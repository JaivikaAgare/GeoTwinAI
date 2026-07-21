import pandas as pd
import os

output_path = "output/"

print("Loading datasets...")

# Population data
population = pd.read_csv(
    output_path + "Nagpur_Population.csv"
)

# OSM datasets
files = {
    "Buildings": "Nagpur_Buildings.csv",
    "Roads": "Nagpur_Roads.csv",
    "Hospitals": "Nagpur_Hospitals.csv",
    "Schools": "Nagpur_Schools.csv",
    "Parks": "Nagpur_Parks.csv",
    "WaterBodies": "Nagpur_WaterBodies.csv"
}


summary = []


for category, file in files.items():

    path = output_path + file

    if os.path.exists(path):

        df = pd.read_csv(path)

        count = len(df)

        summary.append({
            "Feature": category,
            "Count": count
        })

        print(category, ":", count)

    else:
        print(file, "not found")


# Convert summary into dataframe
osm_summary = pd.DataFrame(summary)


# Add population information
population_value = population["Population"][0]
area = population["Area_km2"][0]
density = population["Population_Density"][0]


final_data = {
    "City": ["Nagpur"],
    "Population": [population_value],
    "Area_km2": [area],
    "Population_Density": [density]
}


final_df = pd.DataFrame(final_data)


# Add OSM counts

for index,row in osm_summary.iterrows():

    final_df[row["Feature"]+"_Count"] = row["Count"]



final_df.to_csv(
    output_path+"Nagpur_Master_Dataset.csv",
    index=False
)


print("\n✅ Master Dataset Created Successfully!")

print(final_df)
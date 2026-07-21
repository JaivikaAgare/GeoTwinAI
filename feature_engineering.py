import pandas as pd
import os


input_file = "output/Nagpur_Master_Dataset.csv"


print("Loading Master Dataset...")

df = pd.read_csv(input_file)


# Building Density

df["Building_Density"] = (
    df["Buildings_Count"] / df["Area_km2"]
).round(2)



# Healthcare Index

df["Healthcare_Index"] = (
    df["Hospitals_Count"] / df["Population"]
    * 100000
).round(2)



# Education Index

df["Education_Index"] = (
    df["Schools_Count"] / df["Population"]
    * 100000
).round(2)



# Green Cover Index

df["Green_Cover_Index"] = (
    df["Parks_Count"] / df["Area_km2"]
).round(2)



# Water Availability Score

df["Water_Availability_Score"] = (
    df["WaterBodies_Count"] / df["Area_km2"]
).round(2)



# Urban Development Score

df["Urban_Development_Score"] = (

    df["Building_Density"] * 0.4
    +
    df["Healthcare_Index"] * 0.2
    +
    df["Education_Index"] * 0.2
    +
    df["Green_Cover_Index"] * 0.1
    +
    df["Water_Availability_Score"] * 0.1

).round(2)



# Save final ML dataset

df.to_csv(
    "output/Nagpur_Feature_Dataset.csv",
    index=False
)


print("\n✅ Feature Engineering Completed!")

print(df)
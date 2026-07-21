import pandas as pd
import os
import joblib

from sklearn.ensemble import RandomForestRegressor


print("Loading Feature Dataset...")

df = pd.read_csv(
    "output/Nagpur_Feature_Dataset.csv"
)


# Input Features

X = df[
[
    "Population_Density",
    "Building_Density",
    "Healthcare_Index",
    "Education_Index",
    "Green_Cover_Index",
    "Water_Availability_Score"
]
]


# Target Variable

y = df[
    "Urban_Development_Score"
]


print("Training ML Model...")


model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


model.fit(X,y)



# Create model folder

os.makedirs(
    "model",
    exist_ok=True
)



# Save model

joblib.dump(
    model,
    "model/nagpur_urban_model.pkl"
)



print("\n✅ ML Model Training Completed!")

print(
    "Model saved at: model/nagpur_urban_model.pkl"
)
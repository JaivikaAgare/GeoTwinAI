import pandas as pd
import joblib


print("Loading ML Model...")


# Load trained model

model = joblib.load(
    "model/nagpur_urban_model.pkl"
)


print("Model Loaded Successfully!")


# Future Scenario Input

future_data = pd.DataFrame({

    "Population_Density":[12000],

    "Building_Density":[1800],

    "Healthcare_Index":[12],

    "Education_Index":[40],

    "Green_Cover_Index":[2],

    "Water_Availability_Score":[0.5]

})


print("\nPredicting Future Urban Development...")


prediction = model.predict(
    future_data
)


print(
    "\nPredicted Urban Development Score:",
    round(prediction[0],2)
)


if prediction[0] > 100:

    print("Status: High Urban Growth Zone")

elif prediction[0] > 50:

    print("Status: Moderate Growth Zone")

else:

    print("Status: Low Growth Zone")
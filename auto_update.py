import os
import subprocess
from datetime import datetime


def run_command(name, command):

    print("\n" + "="*60)
    print(name)
    print("="*60)

    result = subprocess.run(
        command,
        shell=True
    )

    if result.returncode != 0:
        print("❌ Error in:", name)
        exit()

    print("✅ Completed:", name)



print("""
====================================
 GeoTwinAI AUTO UPDATE SYSTEM
====================================
""")


# Current time
print(
    "Update Time:",
    datetime.now()
)


# 1 Check Satellite Data

if os.path.exists("satellite/data"):

    print("\nSatellite folder found")

else:

    print("\nSatellite data missing")
    

run_command(
    "Downloading Latest Satellite Data",
    "python satellite/download_satellite.py"
)



# 2 Update OpenStreetMap Data

run_command(
    "Updating OSM Infrastructure Data",
    "python main.py"
)



# 3 Feature Creation

run_command(
    "Updating Features",
    "python feature_engineering.py"
)



# 4 Merge Dataset

run_command(
    "Merging Updated Dataset",
    "python merge_data.py"
)



# 5 Retrain Model

run_command(
    "Retraining AI Model",
    "python ml_model.py"
)



# 6 New Prediction

run_command(
    "Generating Future Scenario",
    "python predict.py"
)



print("""
====================================
 🚀 GeoTwinAI Updated Successfully
====================================
""")
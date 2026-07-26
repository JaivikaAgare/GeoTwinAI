import subprocess
import sys

print("=" * 60)
print("GeoTwinAI Automated Processing Pipeline")
print("=" * 60)

scripts = [
    "satellite/download_image.py",
    "satellite/data_cleaning.py",
    "satellite/ndvi.py",
    "satellite/landuse.py",
    "satellite/builtup.py",
    "satellite/greencover.py",
    "satellite/flood_risk.py",
    "satellite/heatmap.py"
]

for script in scripts:
    print(f"\nRunning: {script}")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"\nError while running {script}")
        break

print("\nPipeline Finished Successfully")
print("=" * 60)
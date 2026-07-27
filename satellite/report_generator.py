from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

os.makedirs("output", exist_ok=True)

doc = SimpleDocTemplate("output/GeoTwinAI_Report.pdf")

styles = getSampleStyleSheet()

story = []

story.append(Paragraph("<b>GeoTwinAI Project Report</b>", styles["Title"]))

story.append(Paragraph("Project: AI-Powered Digital Twin for Smart Cities", styles["Heading2"]))

story.append(Paragraph("Location: Nagpur", styles["Normal"]))

story.append(Paragraph("<br/><b>Modules Completed</b>", styles["Heading2"]))

modules = [
    "✔️ Satellite Image Download",
    "✔️ Data Cleaning",
    "✔️ NDVI Analysis",
    "✔️ Green Cover Detection",
    "✔️ Land Use Classification",
    "✔️ Built-up Area Detection",
    "✔️ Flood Risk Analysis",
    "✔️ Heat Map Generation",
    "✔️ Interactive Map"
]

for module in modules:
    story.append(Paragraph(module, styles["Normal"]))

story.append(Paragraph("<br/><b>Summary</b>", styles["Heading2"]))

story.append(Paragraph(
    "GeoTwinAI processes Sentinel-2 satellite imagery to generate "
    "multiple geospatial analyses such as NDVI, Green Cover, "
    "Land Use, Built-up Area, Flood Risk, and Heat Map. "
    "These outputs help support smart city planning and decision-making.",
    styles["Normal"]
))

doc.build(story)

print("PDF Report Generated Successfully!")
print("Saved as: output/GeoTwinAI_Report.pdf")
import json
import os

# Define paths
JSON_FILE = "results/adverts.json"
OUTPUT_DIR = "docs"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "index.html")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load adverts data
try:
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        adverts = json.load(file)
except FileNotFoundError:
    print(f"❌ ERROR: {JSON_FILE} not found. Make sure it exists before running.")
    exit(1)

# Generate static HTML
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AdGator: Adverts in Ireland</title>
</head>
<body>
    <h1>Latest Adverts</h1>
    <ul>
"""

for ad in adverts:
    html_content += f"""
        <li>
            <img src="{ad['image']}" alt="{ad['title']}" width="50">
            <a href="{ad['link']}" target="_blank">{ad['title']}</a> - {ad['price']} ({ad['location']})
        </li>
    """

html_content += """
    </ul>
</body>
</html>
"""

# Write to file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"✅ index.html generated at {OUTPUT_FILE}")

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

# Generate static HTML with full styling and preloaded ads
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AdGator: Adverts in Ireland</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 20px auto;
            padding: 10px;
        }
        .logo img {
            width: 180px;
        }
        .logo {
            text-align: center;
        }
        .ad-list {
            list-style: none;
            padding: 0;
            margin: 0;
        }
        .ad-item {
            display: flex;
            align-items: center;
            padding: 8px;
            border-bottom: 1px solid #ddd;
            font-size: 14px;
            cursor: pointer;
            transition: background-color 0.2s ease-in-out;
        }
        .ad-item:hover {
            background-color: #f5f5f5;
        }
        .ad-item img {
            width: 40px;
            height: 40px;
            object-fit: cover;
            border-radius: 5px;
            transition: transform 0.3s ease-in-out;
        }
        .ad-item img:hover {
            transform: scale(4);
        }
        .ad-details {
            margin-left: 10px;
            flex-grow: 1;
        }
        .ad-title {
            font-weight: bold;
            margin: 0;
            font-size: 14px;
        }
        .ad-price {
            color: green;
        }
        .ad-location {
            color: gray;
        }
        .view-button {
            padding: 5px 10px;
            font-size: 12px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.2s ease-in-out;
        }
        .view-button:hover {
            background-color: #0056b3;
        }
        .footer {
            position: fixed;
            bottom: 10px;
            right: 10px;
            display: flex;
            gap: 15px;
            align-items: center;
            background: rgba(255, 255, 255, 0.9);
            padding: 8px;
            border-radius: 8px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }
        .footer a {
            text-decoration: none;
            color: #1e1e1e60;
            font-size: 14px;
        }
    </style>
</head>
<body>    
    <div class="logo">
        <a href="https://ads.t-o.ie/"><img src="logo.png"></a>
    </div>

    <h2 style="text-align: center;">Latest Adverts</h2>

    <ul class="ad-list">
"""

# Add adverts from JSON
for ad in adverts:
    html_content += f"""
        <li class="ad-item" onclick="window.open('{ad['link']}', '_blank')">
            <img src="{ad['image']}" alt="{ad['title']}">
            <div class="ad-details">
                <p class="ad-title">{ad['title']}</p>
                <span class="ad-price">{ad['price']}</span> |
                <span class="ad-location">{ad['location']}</span>
            </div>
            <button class="view-button" onclick="window.open('{ad['link']}', '_blank'); event.stopPropagation();">View</button>
        </li>
    """

html_content += """
    </ul>

    <!-- Footer -->
    <footer class="footer">
        <span>
            <a href="#">What's this about?</a>
        </span>
        <span>
            <a href="#">Help!</a>
        </span>
    </footer>

</body>
</html>
"""

# Write to file
with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"✅ index.html successfully generated at {OUTPUT_FILE}")

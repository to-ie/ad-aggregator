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

# Generate static HTML with footer, tooltips, optimized filtering, and correct ad visibility logic
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
        .filter-box {
            display: flex;
            gap: 10px;
            margin-bottom: 10px;
        }
        .filter-box input {
            flex: 1;
            padding: 5px;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        .filter-box input:focus-visible {
            outline: 1px solid #cccccc;
        }
        .ad-list {
            list-style: none;
            padding: 0;
            margin: 0;
            display: none; /* Hide ads initially */
        }
        .ad-item {
            display: none; /* Hide individual ads initially */
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
        .no-results {
            text-align: center;
            color: gray;
            font-size: 14px;
            margin-top: 10px;
            display: none;
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
            color: #1e1e1e;
            font-size: 14px;
        }
        .tooltip-footer {
            position: relative;
            display: inline-block;
            cursor: pointer;
            color: #1e1e1e;
            font-size: 14px;
        }
        .tooltip-footer .tooltip-text {
            visibility: hidden;
            width: 250px;
            background-color: black;
            color: white;
            text-align: center;
            padding: 5px;
            border-radius: 5px;
            position: absolute;
            z-index: 10;
            bottom: 30px;
            left: 50%;
            transform: translateX(-50%);
            opacity: 0;
            transition: opacity 0.3s;
        }
        .tooltip-footer:hover .tooltip-text {
            visibility: visible;
            opacity: 1;
        }
    </style>
</head>
<body>    
    <div class="logo">
        <a href="https://ads.t-o.ie/"><img src="logo.png"></a>
    </div>

    <h2 style="text-align: center;">Latest Adverts</h2>

    <!-- Filter Inputs -->
    <div class="filter-box">
        <input type="text" id="titleFilter" placeholder="Search by title..." oninput="debounceFilterAds()">
        <input type="text" id="locationFilter" placeholder="Search by location..." oninput="debounceFilterAds()">
    </div>

    <!-- Adverts List -->
    <ul class="ad-list" id="adverts-list">
"""

# Add adverts from JSON
for ad in adverts:
    html_content += f"""
        <li class="ad-item" data-title="{ad['title'].lower()}" data-location="{ad['location'].lower()}" onclick="window.open('{ad['link']}', '_blank')">
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
    <p class="no-results" id="no-results">No matching results.</p>

    <!-- Footer with Tooltips -->
    <footer class="footer">
        <span class="tooltip-footer">
            <a href="#" class="footer-link">What's this about?</a>
            <span class="tooltip-text">Find the best deals in Ireland, all in one place! We feature ads from Adverts.ie, with DoneDeal.ie, eBay.ie, and Facebook Marketplace coming soon.</span>
        </span>

        <span class="tooltip-footer">
            <a href="#" class="footer-link">Help!</a>
            <span class="tooltip-text">If you don't see any ads, check if script blockers are interfering. Email: toie -at- pm -dot- me.</span>
        </span>
    </footer>

    <script>
        let debounceTimer;
        function debounceFilterAds() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(filterAds, 200);
        }

        function filterAds() {
            let titleFilter = document.getElementById("titleFilter").value.toLowerCase().trim();
            let locationFilter = document.getElementById("locationFilter").value.toLowerCase().trim();
            let adItems = document.querySelectorAll(".ad-item");
            let listContainer = document.getElementById("adverts-list");
            let hasResults = false;

            adItems.forEach(ad => {
                let title = ad.getAttribute("data-title");
                let location = ad.getAttribute("data-location");

                if (title.includes(titleFilter) && location.includes(locationFilter)) {
                    ad.style.display = "flex";
                    hasResults = true;
                } else {
                    ad.style.display = "none";
                }
            });

            listContainer.style.display = hasResults ? "block" : "none";
            document.getElementById("no-results").style.display = hasResults ? "none" : "block";
        }
    </script>
</body>
</html>
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"✅ index.html successfully generated at {OUTPUT_FILE}")

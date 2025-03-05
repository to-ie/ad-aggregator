# 🛒 Ad Aggregator

**Ad Aggregator** is a marketplace listing aggregator for Ireland, designed to scrape and track advertisements from multiple platforms. Currently, it supports **Adverts.ie**, with future plans to include **Facebook Marketplace**, **Ebay**, and **DoneDeal**.

This tool allows users to:
- Collect daily snapshots of listings.
- Identify new and removed ads.
- Store data in a structured format (JSON).
- Automate scraping with cron jobs.

## 🚀 Features

✅ Adverts.ie Scraper – Extracts key details from listings, including:

- 📷 Image URL
- 📍 Location
- 🏷 Title
- 💰 Price
- 🔗 Ad Link

✅ Data Storage – Saves results in a structured JSON file. <br>
✅ Automation – Set up scheduled daily scrapes using cron jobs. <br>
✅ Future Expansion – Planned support for Facebook Marketplace, Gumtree, and DoneDeal. <br>

## 🛠 Installation & Setup

### 1️⃣ Prerequisites
Ensure Python 3 is installed on your system.

### 2️⃣ Create a Virtual Environment (Optional)
```
python3 -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

Run the following command to install required packages:
```
pip install -r requirements.txt
```
Or manually install:
```
pip install selenium undetected-chromedriver beautifulsoup4 webdriver-manager setuptools
```

### 4️⃣ Running the Scraper

To manually run the scraper:
```
python scraper.py
```

### 5️⃣ Automate with Cron Jobs (Linux/macOS)

To schedule the scraper to run daily at 8 AM, add this to your crontab:
```
crontab -e
```
Then add:
```
0 8 * * * /usr/bin/python /path/to/your/scraper.py
```
Replace /path/to/your/scraper.py with the actual path to the script.

## 📁 Data Storage

- Scraped ads are saved in results/adverts.json.
- The JSON file contains structured data for easy integration into web applications.

Example JSON structure:
```
[
  {
    "title": "Used iPhone 12 - Excellent Condition",
    "price": "€450",
    "location": "Dublin",
    "image": "https://example.com/image.jpg",
    "link": "https://www.adverts.ie/iphone-12"
  }
]
```

## 🔧 Troubleshooting

- Issue: selenium.common.exceptions.WebDriverException
    - Solution: Ensure Chromedriver is up to date. Run:
        ```
        pip install --upgrade webdriver-manager
        ```
- Issue: Scraper not running in cron job
    - Solution: Use absolute paths for Python and script files in your cron job.


## 📜 License

This project is open-source under the MIT License.

## 🌟 Future Plans

- 🔄 Multi-platform support (Facebook Marketplace, Gumtree, DoneDeal).
- 📊 Web dashboard for viewing listings.
- 🔔 Notification system for new ads.

## 🤝 Contributing

PRs and suggestions are welcome! Feel free to fork and submit a pull request. 🚀



test
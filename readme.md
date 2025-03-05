# 🛒 Ad Aggregator

Ad Aggregator is a marketplace listing aggregator for Ireland, designed to scrape and track advertisements from multiple platforms. Currently, it supports Adverts.ie, with future plans to include Facebook Marketplace, eBay, and DoneDeal.

This tool allows users to:

- Collect daily snapshots of listings.
- Identify new and removed ads.
- Store data in a structured format (JSON).
- Automate scraping with cron jobs.
- Display ads in a simple, filterable list.

## ✨ Features

- **Adverts.ie Scraper** – Extracts key details from listings, including:
  - Image URL
  - Location
  - Title
  - Price
  - Ad Link
- **Data Storage** – Saves results in a structured JSON file.
- **Automation** – Set up scheduled daily scrapes using cron jobs.
- **Future Expansion** – Planned support for Facebook Marketplace, eBay, and DoneDeal.

## 🔨 Installation & Setup

### 1️⃣ Prerequisites

Ensure Python 3 is installed on your system.

### 2️⃣ Create a Virtual Environment

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use 'env\\Scripts\\activate'
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Run the Scraper

```
python scrapers/adverts_scraper.py
```

This will generate a JSON file (results/adverts.json) containing the scraped data.

## 🕒 Automation with Cron Jobs

To automate daily scraping add the following entries to your crontab:
```
0 0 * * * /path/to/env/bin/python /path/to/scrapers/adverts_scraper.py
```
Replace /path/to/ with the actual paths on your system.

## ✏️ Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes.

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

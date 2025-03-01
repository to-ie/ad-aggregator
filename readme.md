# Ads in Dublin

## What is this? 
This project is a marketplace agregator from websites in Ireland.
It includes: 
- adverts.ie

Future versions will include: 
- Facebook marketplace
- Gumtree
- Done deal

## Requirements
- Python 3
- The following libraries 
    `pip install selenium undetected-chromedriver beautifulsoup4 webdriver-manager setuptools`

### Python environment
To activate the environment: `source myenv/bin/activate`
To deactivate the environment: `deactivate`

## Scrapers
Below, some notes on how each scraper works.

### Adverts.ie
- Scrapes adverts from a [category/page on adverts.ie](https://www.adverts.ie/for-sale)
- Compares today's ads with the previous day's ads
- Identifies new ads and removed ads
- Saves findings to a JSON file
- Runs daily using a scheduler (e.g., cron on Linux)

This will collect:
- Image URL of the ad
- Location of the ad
- Title of the ad
- Price of the ad
- Ad link

## Setting up the scrapers
Set up the daily scrappers via CRON jobs.

```
crontab -e
```

Add this line to run the script daily at 8 AM:
```
0 8 * * * /usr/bin/python3 /path/to/your/adverts-scraper.py
```
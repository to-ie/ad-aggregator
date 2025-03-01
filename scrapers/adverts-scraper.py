import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json
import os
import random

def get_total_pages(base_url):
    """Use Selenium to bypass Cloudflare and retrieve the total number of pages."""

    options = uc.ChromeOptions()
    options.headless = False    # Keep browser visible for debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")

    # Start undetected Chrome
    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"Opening {base_url} to detect total pages...")
        driver.get(base_url)  
        time.sleep(random.uniform(5, 8))  # Delay to mimic a human

        soup = BeautifulSoup(driver.page_source, "html.parser")
        pagination = soup.find("ul", class_="paging")

        if not pagination:
            print("Pagination not found. Defaulting to 1 page.")
            return 1

        # Extract the highest page number
        page_numbers = []
        for li in pagination.find_all("li"):
            a_tag = li.find("a", href=True)
            if a_tag and "page-" in a_tag["href"]:
                try:
                    num = int(a_tag.text.strip())
                    page_numbers.append(num)
                except ValueError:
                    continue

        max_page = max(page_numbers) if page_numbers and min(page_numbers) > 0 else 1
        print(f"Total pages detected: {max_page}")
        return max_page

    finally:
        driver.quit()  # Close browser

def fetch_ads(base_url):
    """Fetch adverts from multiple pages while avoiding detection."""
    
    options = uc.ChromeOptions()
    options.headless = False     # Keep browser visible for debugging
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")

    driver = uc.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    total_pages = get_total_pages(base_url)
    print(f"Total pages to scrape: {total_pages}")

    ads = []

    for page in range(1, total_pages + 1):          
    # testing at small scale
    # for page in range(1, 6):                      
        url = f"{base_url}page-{page}"
        print(f"Fetching: {url}")

        try:
            driver.get(url)
            time.sleep(random.uniform(3, 7))  # Random delay to mimic a human
            
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            for listing in soup.find_all('div', class_='sr-grid-cell quick-peek-container'):
                title_tag = listing.find('div', class_='title').find('a') if listing.find('div', class_='title') else None
                price_tag = listing.find('div', class_='price')
                image_tag = listing.find('a', class_='main-image').find('img') if listing.find('a', class_='main-image') else None
                location_tag = listing.find('div', class_='location')

                if title_tag and price_tag and image_tag and location_tag:
                    title = title_tag.text.strip()
                    link = "https://www.adverts.ie" + title_tag['href']
                    price = price_tag.text.strip()
                    image = image_tag['src'] if image_tag else None
                    location = location_tag.text.strip()

                    ads.append({'title': title, 'link': link, 'price': price, 'image': image, 'location': location})

        except Exception as e:
            print(f"Error fetching page {page}: {e}")

    driver.quit()
    return ads

def save_ads(filename, ads):
    """Save scraped ads to a JSON file."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(ads, file, indent=4, ensure_ascii=False)

def main():
    base_url = 'https://www.adverts.ie/for-sale/'  # Base URL to scrape
    data_file = 'results/adverts.json'
    
    print("Fetching latest ads...")
    current_ads = fetch_ads(base_url)
    
    save_ads(data_file, current_ads)

    print(f"Total ads scraped: {len(current_ads)}")

if __name__ == "__main__":
    main()

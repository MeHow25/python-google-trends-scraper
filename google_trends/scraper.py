from typing import List, Dict, Any
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class GoogleTrendsScraper:
    def __init__(self, lang: str):
        self.geo_code = lang.upper()
        self.url = f"https://trends.google.com/trends/trendingsearches/daily?geo={self.geo_code}"
        self.driver = None
        print(f"Initializing scraper for URL: {self.url}")

    def initialize(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless=new")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            
            # Use system-installed ChromeDriver
            service = Service('/usr/bin/chromedriver')
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
        except Exception as error:
            print("Error initializing Google Trends scraper:", str(error))
            raise

    def scrape(self) -> List[Dict[str, str]]:
        try:
            self.initialize()
            self.driver.get(self.url)
            
            # Wait for the trending searches to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "trend-table"))
            )
            
            # Give it a moment to fully load
            time.sleep(2)
            
            # Find all trend items
            items = self.driver.find_elements(By.CSS_SELECTOR, "#trend-table tbody")[1].find_elements(By.TAG_NAME, "tr")
            
            trends = []
            for item in items:
                columns = item.find_elements(By.TAG_NAME, "td")
                if len(columns) >= 4:
                    title = columns[1].find_element(By.TAG_NAME, "div").text.strip()
                    search_count = columns[2].text.strip()
                    description = columns[3].text.strip()
                    
                    search_parts = search_count.split("+")
                    count = search_parts[0].strip()
                    trend = search_parts[1].strip() if len(search_parts) > 1 else "0%"
                    
                    if title:
                        trends.append({
                            "title": title,
                            "searchCount": count,
                            "searchTrend": trend,
                            "description": description or ""
                        })
            
            return trends
            
        except Exception as error:
            print("Error scraping Google Trends:", str(error))
            raise
        finally:
            if self.driver:
                self.driver.quit() 
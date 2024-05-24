import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging

# Logging for error handling & info
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def scrape_mmlu_data(url):
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(url)

        driver.implicitly_wait(10)

        table = driver.find_element(By.CSS_SELECTOR, 'table.rounded-lg.shadow-md.table')

        leaderboard = []

        header_row = table.find_element(By.TAG_NAME, 'thead').find_element(By.TAG_NAME, 'tr')
        headers = [header.text.strip() for header in header_row.find_elements(By.TAG_NAME, 'th')]
        leaderboard.append(headers)

        rows = table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, 'td')
            data = [col.text.strip() for col in columns]
            if data:
                leaderboard.append(data)

        # Need to convert to exporting to dictionary instead, to match populate_tables 
        with open('leaderboard.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(leaderboard)

        logging.info("Data scraping completed successfully.")

    except Exception as e:
        logging.error(f"Error occurred during scraping: {e}")

    finally:
        # Quit the WebDriver
        try:
            driver.quit()
        except Exception as e:
            logging.error(f"Error occurred while quitting the WebDriver: {e}")

url = "https://crfm.stanford.edu/helm/mmlu/latest/#/leaderboard"
scrape_mmlu_data(url)


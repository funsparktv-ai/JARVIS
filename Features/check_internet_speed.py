from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

# Set up logging to only show warnings
logging.getLogger('selenium').setLevel(logging.WARNING)

def get_internet_speed():
    """Fetches internet speed using the Fast.com website."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        # Open Fast.com and wait for the speed value to be present
        driver.get("https://fast.com/")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'speed-value')))

        # Optional: Wait a bit more to ensure the speed test has completed
        time.sleep(5)

        # Retrieve the speed value
        speed_value = driver.find_element(By.ID, 'speed-value').text
        return speed_value
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        driver.quit()  # Ensure the driver is properly closed

if __name__ == "__main__":
    speed = get_internet_speed()
    if speed:
        print(f"Internet Speed: {speed} Mbps")
    else:
        print("Failed to retrieve internet speed.")

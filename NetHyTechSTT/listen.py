from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from os import getcwd, path
import time

# File path for saving recognized input
Recog_File = path.join(getcwd(), "input.txt")


# Function to configure Chrome options
def setup_chrome_options(headless=True) :
    chrome_options = Options()
    chrome_options.add_argument("--use-fake-ui-for-media-stream")
    if headless :
        chrome_options.add_argument("--headless=new")  # Use new headless mode
    return chrome_options


# Initialize the Chrome driver
def initialize_driver() :
    chrome_driver_path = path.join(getcwd(), "chromedriver.exe")
    service = Service(executable_path=chrome_driver_path)
    options = setup_chrome_options(headless=True)  # Set headless to False if you want to see the browser
    driver = webdriver.Chrome(service=service, options=options)
    return driver


# Function to listen and capture speech-to-text from the web app
def listen() :
    driver = initialize_driver()  # Initialize the Chrome WebDriver
    website = "https://amit-2013.github.io/jarivisprojectspeaktotext/"

    try :
        # Open the website and set up the listening functionality
        driver.get(website)
        print("Support on YouTube @funsparktvYT")

        # Wait for the start button to be clickable
        start_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, 'startButton'))
        )

        # Click the start button to initiate listening
        start_button.click()
        print("Listening...")

        # Initialize variables
        output_text = ""
        is_second_click = False

        while True :
            # Wait for the output element to update and get the recognized text
            output_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'output'))
            )
            current_text = output_element.text.strip()

            # Handle the toggle between listening states
            if "Start Listening" in start_button.text and is_second_click :
                if output_text :  # Output has been captured
                    is_second_click = False
            elif "Listening..." in start_button.text :
                is_second_click = True

            # If there is new output, write it to the file
            if current_text != output_text and current_text :
                output_text = current_text
                with open(Recog_File, "w") as file :
                    file.write(output_text.lower())
                print("User:", output_text)

            # Delay to avoid high-frequency polling (optional tuning)
            time.sleep(0.5)

    except KeyboardInterrupt :
        print("Process interrupted by user.")
    except Exception as e :
        print(f"An error occurred: {e}")

    finally :
        # Ensure the driver is properly closed
        driver.quit()


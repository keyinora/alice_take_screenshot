from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def take_fullpage_screenshot(url, output_file, driver_path):
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1440,1080")
    options.add_argument("--headless")  # Run Chrome in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    # Start WebDriver
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Load the webpage
        driver.get(url)
        time.sleep(5)  # Allow time for JavaScript to load (adjust if necessary)

        # Adjust to full height of the page
        #scroll_height = driver.execute_script("return document.body.scrollHeight")
        #driver.set_window_size(1440, scroll_height)
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        for scroll_position in range(0, scroll_height, 500):
            driver.execute_script(f"window.scrollTo(0, {scroll_position});")
            time.sleep(0.5)
        # Save screenshot
        driver.save_screenshot(output_file)
        print(f"Screenshot saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        driver.quit()

# Usage Example
if __name__ == "__main__":
    take_fullpage_screenshot(
        url="https://captivation.agency/",
        output_file="screenshot.png",
        driver_path="/usr/bin/chromedriver"
    )

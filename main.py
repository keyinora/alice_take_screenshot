from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import datetime


# Define the main function
def main():
    # Step 1: Set up the Chrome WebDriver with headless option
    print("[Step 1] Setting up Chrome WebDriver...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Step 2: Open Google
    site_name = "Captivation Agency"
    print("f[Step 2] Opening {site_name}...")
    url = "https://captivation.agency/"
    driver.get(url)

    # Step 3: Wait for the page to fully load
    print("[Step 3] Waiting for the page to fully load...")
    time.sleep(10)

    # Step 4: Adjust the window size to capture the whole page
    print("[Step 4] Adjusting window size to capture the full page...")
    page_width = driver.execute_script("return document.body.scrollWidth")
    page_height = driver.execute_script("return document.body.scrollHeight")
    
    driver.set_window_size(page_width, page_height)

    # Step 5: Slowly scroll from the top of the page to the bottom
    print("[Step 5] Scrolling through the page...")
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    for scroll_position in range(0, scroll_height, 500):
        driver.execute_script(f"window.scrollTo(0, {scroll_position});")
        time.sleep(0.5)

    # Step 6: Take a screenshot of the loaded page
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"{url.replace('https://', '').replace('/', '')}-{timestamp}.png"
    print(f"[Step 6] Taking a screenshot and saving it as '{screenshot_filename}'...")
    driver.save_screenshot(screenshot_filename)

    # Step 7: Close the browser
    print("[Step 7] Closing the browser...")
    driver.quit()

# Run the main function
if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import datetime
import os
import base64
import time
from PIL import Image
from io import BytesIO

# Define the main function
def main():
    print("[Step 1] Setting up Chrome WebDriver...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    )
    chrome_options.add_argument("window-size=1440,900")  # Set the width to 1440px and an initial height of 900px

    service = Service('/usr/bin/chromedriver')  # Update the path if needed
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("[Step 2] Opening the website...")
    url = "https://captivation.agency/"
    driver.get(url)

    print("[Step 3] Waiting for the page to load completely...")
    driver.implicitly_wait(10)

    # Step 4: Scroll to the bottom of the page and back to the top
    print("[Step 4] Scrolling to the bottom of the page...")
    scroll_height = driver.execute_script("return document.body.scrollHeight")
    current_scroll = 0

    while current_scroll < scroll_height:
        current_scroll += 500
        driver.execute_script(f"window.scrollTo(0, {current_scroll});")
        time.sleep(0.5)
        scroll_height = driver.execute_script("return document.body.scrollHeight")

    print("[Step 5] Scrolling back to the top...")
    for current_scroll in range(scroll_height, 0, -500):
        driver.execute_script(f"window.scrollTo(0, {current_scroll});")
        time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # Step 6: Capture full-page screenshot using Chrome DevTools Protocol (CDP)
    print("[Step 6] Capturing full-page screenshot...")
    screenshot_folder = "screenshots"
    os.makedirs(screenshot_folder, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = os.path.join(screenshot_folder, f"{url.replace('https://', '').replace('/', '')}-{timestamp}.webp")

    # Use Chrome DevTools Protocol for full-page screenshot
    full_screenshot = driver.execute_cdp_cmd("Page.captureScreenshot", {"format": "webp", "captureBeyondViewport": True})
    original_image = Image.open(BytesIO(base64.b64decode(full_screenshot["data"])))

    # Step 7: Compress and save the screenshot
    compressed_filename = os.path.join(screenshot_folder, f"{url.replace('https://', '').replace('/', '')}-{timestamp}-compressed.webp")
    original_image.save(compressed_filename, "webp", optimize=True)

    print(f"Original screenshot saved as {screenshot_filename}")
    print(f"Compressed screenshot saved as {compressed_filename}")

    print("[Step 8] Closing the browser...")
    driver.quit()


# Run the main function
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")

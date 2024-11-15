import os
import time
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from PIL import Image, ImageChops

# Determine URL based on command-line arguments
url = sys.argv[1] if len(sys.argv) > 1 else "https://captivation.agency/"
print(f"[INFO] URL to monitor: {url}")

# Setup Firefox options
firefox_options = FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')
firefox_options.add_argument('--window-size=1920x1080')
print("[INFO] Firefox options configured")

# Create Firefox WebDriver with manually specified GeckoDriver path and increased timeout
print("[INFO] Setting up Firefox WebDriver...")
service = Service("/usr/local/bin/geckodriver", timeout=300)  # Update the path if different and increase timeout
try:
    browser = webdriver.Firefox(service=service, options=firefox_options)
    print("[INFO] Firefox WebDriver created successfully")
except Exception as e:
    print(f"[ERROR] Failed to create WebDriver: {e}")
    sys.exit(1)

# Specify the URL to monitor
domain = url.split('//')[-1].split('/')[0]
domain_folder = os.path.join(os.getcwd(), domain)

# Create a folder for the domain if it doesn't exist
if not os.path.exists(domain_folder):
    os.makedirs(domain_folder)
    print(f"[INFO] Created directory for domain: {domain_folder}")
else:
    print(f"[INFO] Using existing directory for domain: {domain_folder}")

# Load the page and take a screenshot
print(f"[INFO] Loading URL: {url}")
browser.get(url)
time.sleep(5)  # Wait for page to load completely
print("[INFO] Page loaded, taking screenshot...")
screenshot_path = os.path.join(domain_folder, f"{domain}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
browser.save_screenshot(screenshot_path)
print(f"[INFO] Screenshot saved at: {screenshot_path}")

# Close the browser
browser.quit()
print("[INFO] Browser closed")

# Log the screenshot action
log_path = os.path.join(domain_folder, "log.txt")
with open(log_path, "a") as log_file:
    log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Screenshot taken: {screenshot_path}\n"
    log_file.write(log_message)
    print(f"[LOG] {log_message.strip()}")

# Compare screenshots if there's more than one
screenshots = sorted([f for f in os.listdir(domain_folder) if f.endswith('.png')])
if len(screenshots) > 1:
    print("[INFO] Comparing screenshots...")
    latest_screenshot = Image.open(os.path.join(domain_folder, screenshots[-1]))
    previous_screenshot = Image.open(os.path.join(domain_folder, screenshots[-2]))

    # Compare images
    diff = ImageChops.difference(latest_screenshot, previous_screenshot)
    diff_bbox = diff.getbbox()

    # Calculate pixel difference ratio
    diff_pixels = diff.crop(diff_bbox).getdata() if diff_bbox else []
    diff_ratio = len(diff_pixels) / (latest_screenshot.width * latest_screenshot.height)

    # Log the comparison result
    with open(log_path, "a") as log_file:
        log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Pixel difference ratio: {diff_ratio:.2%}\n"
        log_file.write(log_message)
        print(f"[LOG] {log_message.strip()}")
else:
    print("[INFO] Not enough screenshots to compare")

# Delete the oldest screenshot if there are more than two
if len(screenshots) > 2:
    oldest_screenshot = os.path.join(domain_folder, screenshots[0])
    os.remove(oldest_screenshot)
    print(f"[INFO] Deleted oldest screenshot: {oldest_screenshot}")

    # Log the deletion
    with open(log_path, "a") as log_file:
        log_message = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Deleted oldest screenshot: {oldest_screenshot}\n"
        log_file.write(log_message)
        print(f"[LOG] {log_message.strip()}")
else:
    print("[INFO] No screenshots to delete")

# README: Selenium Web Scraper Script

## Overview
This Python script uses Selenium to automate the Chrome browser. It opens a specified URL, waits for the page to load, scrolls slowly from top to bottom, and takes a screenshot of the entire page. The screenshot is saved with a filename that includes the URL and a timestamp for easy identification.

## Prerequisites

1. **Python 3**: Make sure Python 3 is installed on your machine.
2. **WSL (Windows Subsystem for Linux)**: This script is intended to run using WSL on Windows 11.
3. **Selenium**: Install Selenium using pip.
4. **ChromeDriver**: Install ChromeDriver to allow Selenium to interact with Chrome.
5. **Google Chrome**: Make sure Chrome is installed.

## Installation Instructions

1. **Install Selenium**

   Open your WSL terminal and run the following command:
   ```bash
   pip install selenium
   ```

2. **Install ChromeDriver**

   Install ChromeDriver to allow Selenium to interact with the Chrome browser:
   ```bash
   sudo apt-get update
   sudo apt-get install chromium-chromedriver
   ```

3. **Verify Paths**

   Ensure that ChromeDriver is correctly located in `/usr/bin`. To verify:
   ```bash
   which chromedriver
   ```

4. **Add ChromeDriver to PATH** (Optional)

   Add ChromeDriver to your PATH to make sure Selenium can access it:
   ```bash
   echo 'export PATH=$PATH:/usr/bin' >> ~/.bashrc
   source ~/.bashrc
   ```

## Usage Instructions

1. **Run the Script**

   To run the script, open your WSL terminal and navigate to the directory containing the script. Then execute:
   ```bash
   python3 main.py
   ```

2. **Script Features**

   - The script will:
     1. Set up the Chrome WebDriver.
     2. Open the specified URL (currently set to `https://captivation.agency/`).
     3. Wait for the page to fully load.
     4. Scroll slowly from the top to the bottom of the page to ensure all elements load.
     5. Take a screenshot of the page, saving it in the format: `url-timestamp.png`.

3. **Screenshot Filename Format**

   The screenshot will be saved in the current working directory with a filename that includes the URL (without `https://` and `/`) and a timestamp, e.g., `captivation.agency-2024-11-15_12-30-45.png`.

## Troubleshooting

1. **Chrome in Mobile View**: If the page loads in mobile view instead of desktop view, ensure that:
   - The user-agent is correctly set to a desktop version in the script.
   - The window size is set to desktop resolution (`1920x10000`) to capture the entire page.

2. **Dependencies Missing**: Ensure all dependencies are installed, including:
   - `libnss3`, `libgconf-2-4`, `libasound2`, `libxss1`
   ```bash
   sudo apt-get install -y libnss3 libgconf-2-4 libasound2 libxss1
   ```

## Customizing the Script

- **URL**: To change the URL that the script opens, update the `url` variable in the script.
- **Scroll Speed**: Adjust the `time.sleep(0.5)` value to control the scroll speed.
- **Screenshot Format**: Modify the `screenshot_filename` to adjust the naming convention.

## Notes

- The script runs in **headless mode** by default, which means Chrome runs without a GUI. This is useful for environments without a display, like WSL.
- Ensure your ChromeDriver version matches your Chrome browser version to avoid compatibility issues.

## Contact
For any questions or issues, feel free to reach out to the developer team or create an issue in the repository.

Happy automating!


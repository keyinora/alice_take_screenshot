import asyncio
from pyppeteer import launch

async def main():
    print("[Step 2] setup browser")
    #browser = await launch()
    browser = await launch(headless=True, args=['--no-sandbox', '--disable-setuid-sandbox'])

    print(browser)
    page = await browser.newPage()
    await page.goto('https://captivation.agency/')
    print('[Step 3] take screenshot')
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()

print("[Step 1] call async script main")
asyncio.get_event_loop().run_until_complete(main())
import asyncio
from playwright.async_api import async_playwright
import os

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Load the local file
        path = os.path.abspath("index.html")
        await page.goto(f"file://{path}")

        # Desktop Dark (Default)
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.screenshot(path="final_desktop_dark.png", full_page=True)

        # Desktop Light
        await page.click("#theme-toggle")
        await asyncio.sleep(0.5) # Wait for transition
        await page.screenshot(path="final_desktop_light.png", full_page=True)

        # Mobile Light
        await page.set_viewport_size({"width": 375, "height": 667})
        await page.screenshot(path="final_mobile_light.png", full_page=True)

        # Mobile Dark
        await page.click("#theme-toggle")
        await asyncio.sleep(0.5)
        await page.screenshot(path="final_mobile_dark.png", full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

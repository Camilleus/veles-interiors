import asyncio
from playwright.async_api import async_playwright
import os

async def verify_spa():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={'width': 1440, 'height': 900})

        # Load the local HTML file
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # Wait for initial load and animations
        await page.wait_for_timeout(1000)

        # 1. Verify Home Page
        print("Verifying Home Page...")
        await page.screenshot(path='spa_home_light.png', full_page=True)

        # 2. Verify Theme Switch
        print("Verifying Theme Switch...")
        await page.click('#theme-toggle')
        await page.wait_for_timeout(500)
        await page.screenshot(path='spa_home_dark.png', full_page=True)

        # 3. Verify Routing - Career
        print("Verifying Career Page...")
        await page.click('#hamburger')
        await page.wait_for_timeout(1000)
        await page.click('#full-menu a[href="#/kariera"]')

        await page.wait_for_timeout(1000)
        await page.screenshot(path='spa_career_dark.png', full_page=True)

        # 4. Verify Routing - Contact
        print("Verifying Contact Page...")
        await page.goto(file_path + "#/kontakt") # Direct hash navigation
        await page.wait_for_timeout(1000)
        await page.screenshot(path='spa_contact_dark.png', full_page=True)

        # 5. Verify Mobile View
        print("Verifying Mobile View...")
        await page.set_viewport_size({'width': 375, 'height': 812})
        await page.goto(file_path + "#/")
        await page.wait_for_timeout(1000)
        await page.screenshot(path='spa_home_mobile.png', full_page=True)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(verify_spa())

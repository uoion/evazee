from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://0.0.0.0:8000", timeout=60000)
        page.screenshot(path="jules-scratch/verification/screenshot.png")
        browser.close()

run()

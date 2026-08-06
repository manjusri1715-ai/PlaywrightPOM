
from playwright.sync_api import sync_playwright, expect, Page
#Page, Context, Browser, Playwright

def test_validateThePageComponents(page: Page, navigateToAmazon):
        expect(page).to_have_title("Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
        expect(page).to_have_url("https://www.amazon.in/")
        page.wait_for_timeout(2000)


def test_validateTheHeaders(page:Page, navigateToAmazon):
        # page.locator("input#twotabsearchtextbox")
        expect(page.locator("input#twotabsearchtextbox")).to_be_visible()

        
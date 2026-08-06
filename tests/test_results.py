from playwright.sync_api import sync_playwright, expect, Page

def test_validateTheResultsTitle(page: Page, navigateToAmazon):
    page.locator("input#twotabsearchtextbox").fill("iphone")
    page.locator("#nav-search-submit-button").click()
    page.locator("//h2[text()='Results']").wait_for(state="visible")
    expect(page).to_have_title("Amazon.in : iphone")

from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.results import resultsPage

@pytest.mark.smoke
def test_validateTheResultsTitle(page: Page, navigateToAmazon):
    resultsPageObj = resultsPage(page)
    page.locator("input#twotabsearchtextbox").fill("iphone")
    page.locator("#nav-search-submit-button").click()
    page.locator("//h2[text()='Results']").wait_for(state="visible")
    expect(page).to_have_title("Amazon.in : iphone")
    page.wait_for_timeout(5000)
    resultsPageObj.clickOnAddToCart("iPhone Air")
    page.wait_for_timeout(5000)


def test_search_results_only_show_iphone_products(page: Page, navigateToAmazon):
    resultsPageObj = resultsPage(page)
    resultsPageObj.searchForProduct("iphone")
    resultsPageObj.verify_search_results_have_keyword("iphone")
    

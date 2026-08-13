import allure
from playwright.sync_api import expect

class resultsPage:
    def __init__(self, page):
        self.page = page
        self.searchInput = page.locator("input#twotabsearchtextbox")
        self.searchButton = page.locator("#nav-search-submit-button")
        self.resultTitles = page.locator("//span[@class='a-size-medium a-color-base a-text-normal']")
        self.addTcart = lambda product: page.locator(f"(//h2[contains(@aria-label,'{product}')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//*[@aria-label='Add to cart'])[1]")
        self.addTcart_iphoneAir = page.locator("(//h2[contains(@aria-label,'iPhone Air')]/ancestor::div[@class='a-section a-spacing-small a-spacing-top-small']//*[@aria-label='Add to cart'])[1]")

    @allure.step("searchForProduct")
    def searchForProduct(self, product: str):
        self.searchInput.fill(product)
        self.searchButton.click()
        self.resultTitles.first.wait_for(state="visible", timeout=15000)

    @allure.step("get_result_titles")
    def get_result_titles(self):
        return self.resultTitles.all_inner_texts()

    @allure.step("verify_search_results_have_keyword")
    def verify_search_results_have_keyword(self, keyword: str):
        titles = self.get_result_titles()
        assert titles, "No search results were found for the product."
        mismatches = [title for title in titles if keyword.lower() not in title.lower()]
        assert not mismatches, f"Found search results without '{keyword}': {mismatches[:5]}"

    @allure.step("clickOnAddToCart")
    def clickOnAddToCart(self, product):
        self.addTcart(product).click()

    
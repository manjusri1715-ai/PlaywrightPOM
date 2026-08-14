import allure
from playwright.sync_api import expect

class homePage:
    # accountsNdListBtn ='[aria-controls="nav-flyout-accountList"]'
    def __init__(self, page):
        self.page = page
        self.accountsNdListBtn = page.locator('[aria-controls="nav-flyout-accountList"]')
        self.signOutLink = page.locator("a#nav-item-signout, a:has-text('Sign Out')")
        self.signedOutIndicator = page.locator("#nav-link-accountList-nav-line-1")

    @allure.step("clickOnAccountsNdlist")
    def clickOnAccountsNdlist(self):
       self.accountsNdListBtn.click()

    @allure.step("validateThevisibilityOfAccountsNdList")
    def validateThevisibilityOfAccountsNdList(self):
        expect(self.accountsNdListBtn).to_be_visible()

    @allure.step("clickOnSignOut")
    def clickOnSignOut(self):
        self.signOutLink.click()

    @allure.step("verifySignedOut")
    def verifySignedOut(self):
        expect(self.signedOutIndicator).to_contain_text("Hello, sign in")

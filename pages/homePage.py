from playwright.sync_api import expect

class homePage:
    # accountsNdListBtn ='[aria-controls="nav-flyout-accountList"]'
    def __init__(self, page):
        self.accountsNdListBtn = page.locator('[aria-controls="nav-flyout-accountList"]')

    def clickOnAccountsNdlist(self):
       self.accountsNdListBtn.click()

    def validateThevisibilityOfAccountsNdList(self):
        expect(self.accountsNdListBtn).to_be_visible()

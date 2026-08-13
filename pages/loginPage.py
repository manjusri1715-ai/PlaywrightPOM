import allure
from playwright.sync_api import expect

class loginPage:
    
    def __init__(self, page):
        self.page = page
        self.emailtextBox = page.locator("//input[@type='email']")
        self.continueBtn = page.locator("//input[@type='submit']")
        self.passwordTxt = page.locator("//input[@type='password']")
        self.signInBtn = page.get_by_role("button", name="Sign in")
        self.invalidPasswordError = page.get_by_text("Your password is incorrect")

    @allure.step("enterEmail")
    def enterEmail(self, emailID):
       self.emailtextBox.fill(emailID)

    @allure.step("clickOnContinueBtn")
    def clickOnContinueBtn(self):
         self.continueBtn.click()

    @allure.step("enterPw")
    def enterPw(self, pw):
         self.passwordTxt.fill(pw)

    @allure.step("clickOnSignInBtn")
    def clickOnSignInBtn(self):
         self.signInBtn.click()

    @allure.step("verifyInvalidPasswordError")
    def verifyInvalidPasswordError(self):
         expect(self.invalidPasswordError).to_be_visible()

    @allure.step("login")
    def login(self, email, pw):
        self.enterEmail(email)
        self.clickOnContinueBtn()
        self.enterPw(pw)
        self.clickOnSignInBtn()

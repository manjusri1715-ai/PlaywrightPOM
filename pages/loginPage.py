
class loginPage:
    
    def __init__(self, page):
        self.emailtextBox = page.locator("//input[@type='email']")
        self.continueBtn = page.locator("//input[@type='submit']")
        self.passwordTxt = page.locator("//input[@type='password']")

    def enterEmail(self, emailID):
       self.emailtextBox.fill(emailID)

    def clickOnContinueBtn(self):
         self.continueBtn.click()

    def enterPw(self, pw):
         self.passwordTxt.fill(pw)

    def login(self, email,pw):
        self.enterEmail(email)
        self.clickOnContinueBtn()
        self.passwordTxt(pw)
        self.clickOnContinueBtn()

from playwright.sync_api import expect

from pages.homePage import homePage
from pages.loginPage import loginPage
 
 
 
def test_loginpage(navigateToAmazon,page):
    homePageObj = homePage(page)
    homePageObj.validateThevisibilityOfAccountsNdList()
    homePageObj.clickOnAccountsNdlist()
    loginPageObj = loginPage(page)
    loginPageObj.emailtextBox("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@04")
    loginPageObj.clickOnContinueBtn()
    expect(page.locator("//span[@id='nav-link-accountList-nav-line-1']")).to_be_visible()
 
 
# def test_invalidloginpage(navigateToAmazon,page):
#     homePageObj = homePage()
#     homePageObj.clickOnAccountsNdlist()
#     page.locator("//input[@type='email']").fill("trainingplaywright@gmail.com")
#     page.locator("//input[@type='submit']").click()
#     page.locator("//input[@type='password']").fill("1234566")
#     page.wait_for_timeout(2000)
#     page.locator("//input[@type='submit']").click()
#     page.wait_for_timeout(2000)
#     assert page.get_by_text('There was a problem').is_visible()
 
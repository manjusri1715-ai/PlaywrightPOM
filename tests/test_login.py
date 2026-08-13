import allure
from playwright.sync_api import expect
import pytest

from pages.homePage import homePage
from pages.loginPage import loginPage
 
 
@pytest.mark.smoke
@pytest.mark.order(1)
@allure.title("Login Test")
@allure.description("This test validates the login functionality of the application.")
def test_loginpage(navigateToAmazon,page):
    homePageObj = homePage(page)
    homePageObj.validateThevisibilityOfAccountsNdList()
    homePageObj.clickOnAccountsNdlist()
    loginPageObj = loginPage(page)
    loginPageObj.enterEmail("trainingplaywright@gmail.com")
    # page.pause()
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@05")
    loginPageObj.clickOnContinueBtn()
    expect(page.locator("//span[@id='nav-link-accountList-nav-line-1']")).to_be_visible()


def test_negative_login(navigateToAmazon, page):
    homePageObj = homePage(page)
    homePageObj.validateThevisibilityOfAccountsNdList()
    homePageObj.clickOnAccountsNdlist()

    loginPageObj = loginPage(page)
    loginPageObj.enterEmail("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("12343545")
    loginPageObj.clickOnSignInBtn()
    loginPageObj.verifyInvalidPasswordError()


def test_sign_out(navigateToAmazon, page):
    homePageObj = homePage(page)
    homePageObj.validateThevisibilityOfAccountsNdList()
    homePageObj.clickOnAccountsNdlist()

    loginPageObj = loginPage(page)
    loginPageObj.enterEmail("trainingplaywright@gmail.com")
    loginPageObj.clickOnContinueBtn()
    loginPageObj.enterPw("Welcome@05")
    loginPageObj.clickOnContinueBtn()

    expect(page.locator("//span[@id='nav-link-accountList-nav-line-1']")).to_be_visible()

    homePageObj.clickOnAccountsNdlist()
    homePageObj.clickOnSignOut()
    homePageObj.verifySignedOut()
 
 

 
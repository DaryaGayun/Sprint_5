from conftest import *

class TestProfile:
    
    def test_go_to_personal_account(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        assert "account" in browser.current_url
    
    def test_exit_from_account(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
        browser.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
        assert "login" in browser.current_url
    
    def test_go_to_constructor_from_profile(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"
    
    def test_go_to_main_from_profile_by_logo(self, login_user):
        browser = login_user
        browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
        browser.find_element(*Locators.LOGO).click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
        assert browser.current_url == BASE_URL + "/"

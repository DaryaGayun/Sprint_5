import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators

BASE_URL = "https://stellarburgers.education-services.ru"

# class TestProfile:
    
#     def test_go_to_personal_account(self, login_user):
#         browser = login_user
#         browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
#         assert "account" in browser.current_url
    
#     def test_exit_from_account(self, login_user):
#         browser = login_user
#         browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGOUT_BUTTON))
#         browser.find_element(*Locators.LOGOUT_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON))
#         assert "login" in browser.current_url
    
#     def test_go_to_constructor_from_profile(self, login_user):
#         browser = login_user
#         browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
#         browser.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
#         assert browser.current_url == BASE_URL + "/"
    
#     def test_go_to_main_from_profile_by_logo(self, login_user):
#         browser = login_user
#         browser.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EMAIL))
#         browser.find_element(*Locators.LOGO).click()
#         WebDriverWait(browser, 5).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
#         assert browser.current_url == BASE_URL + "/"

class TestConstructor:

    def test_buns_section_active_and_clickable(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.BUNS_SECTION))
        browser.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Соусы"))
        browser.find_element(*Locators.BUNS_SECTION).click()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Булки"))
        active_tab = browser.find_element(*Locators.ACTIVE_TAB)
        assert active_tab.text == "Булки"

    def test_sauces_section_clickable(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.SAUCES_SECTION))
        browser.find_element(*Locators.SAUCES_SECTION).click()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Соусы"))
        active_tab = browser.find_element(*Locators.ACTIVE_TAB)
        assert browser.find_element(*Locators.ACTIVE_TAB).text == "Соусы"
    
    def test_fillings_section_clickable(self, browser):
        browser.get(BASE_URL)
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.FILLINGS_SECTION))
        browser.find_element(*Locators.FILLINGS_SECTION).click()
        WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element(Locators.ACTIVE_TAB, "Начинки"))
        active_tab = browser.find_element(*Locators.ACTIVE_TAB)
        assert browser.find_element(*Locators.ACTIVE_TAB).text == "Начинки"

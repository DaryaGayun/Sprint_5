import sys
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators as Locators
from helpers.user_generator import *

BASE_URL = "https://stellarburgers.education-services.ru"

# webdriver-manager не требуется в новых версиях Selenium (ниже ссылка на доку)
# https://www.selenium.dev/selenium/docs/api/py/index.html#drivers
# ...
# In older versions of Selenium, it was necessary to install and manage these drivers yourself.
# ...
# Modern versions of Selenium handle browser and driver installation for you with Selenium Manager.
# ....

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        options = Options()
        driver = webdriver.Chrome(options=options)
    else:
        driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def user_data():
    return {
        "email": generate_unique_email(),
        "password": generate_password(),
        "name": generate_name()
    }

@pytest.fixture
def register_user(browser, user_data):
    browser.get(f"{BASE_URL}/register")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.NAME_INPUT))
    browser.find_element(*Locators.NAME_INPUT).send_keys(user_data["name"])
    browser.find_element(*Locators.EMAIL_INPUT).send_keys(user_data["email"])
    browser.find_element(*Locators.PASSWORD_INPUT).send_keys(user_data["password"])
    browser.find_element(*Locators.REGISTER_BUTTON).click()
    return user_data

@pytest.fixture
def login_user(browser, register_user):
    browser.get(f"{BASE_URL}/login")
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.EMAIL_INPUT_LOGIN))
    browser.find_element(*Locators.EMAIL_INPUT_LOGIN).send_keys(register_user["email"])
    browser.find_element(*Locators.PASSWORD_INPUT_LOGIN).send_keys(register_user["password"])
    browser.find_element(*Locators.LOGIN_BUTTON).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located(Locators.PLACE_ORDER_BUTTON))
    return browser

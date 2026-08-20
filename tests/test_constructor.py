from conftest import *

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

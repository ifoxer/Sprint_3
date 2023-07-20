import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators

#переход на форму авторизации
def test_transition_login_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

def test_authorization_login_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_COLLECT_ORDER)))
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
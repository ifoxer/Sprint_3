import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators

def test_account_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.LINK_FOR_PROFILE)))
    driver.find_element(*TestLocators.LINK_FOR_PROFILE).click()
    text = driver.find_element(*TestLocators.INPUT_ACCOUNT_LOGIN).get_attribute('value')
    assert text == 'testfox@ya.ru'
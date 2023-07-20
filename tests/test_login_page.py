import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators

#вход по кнопке «Войти в аккаунт» на главной
def test_login_accros_button_enter_account(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ENTER_IN_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_COLLECT_ORDER)))
    button_text = driver.find_element(*TestLocators.BUTTON_COLLECT_ORDER).text
    assert button_text == 'Оформить заказ'
#вход через кнопку «Личный кабинет»
def test_login_accros_account(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_COLLECT_ORDER)))
    button_text = driver.find_element(*TestLocators.BUTTON_COLLECT_ORDER).text
    assert button_text == 'Оформить заказ'
#вход через кнопку в форме регистрации
def test_login_accros_registration_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_FOR_REGISTRATION).click()
    driver.find_element(*TestLocators.LINK_FOR_ENTER).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_COLLECT_ORDER)))
    button_text = driver.find_element(*TestLocators.BUTTON_COLLECT_ORDER).text
    assert button_text == 'Оформить заказ'
#вход через кнопку в форме восстановления пароля
def test_login_accros_recovery_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ENTER_IN_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ENTER_IN_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_FOR_RECOVERY).click()
    driver.find_element(*TestLocators.LINK_FOR_ENTER).click()
    driver.find_element(*TestLocators.INPUT_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
    driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
    driver.find_element(*TestLocators.BUTTON_ENTER).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_COLLECT_ORDER)))
    button_text = driver.find_element(*TestLocators.BUTTON_COLLECT_ORDER).text
    assert button_text == 'Оформить заказ'
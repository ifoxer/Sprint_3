from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators

#проверка перехода на страницу регистрации через форму логина
def test_registration_page(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_FOR_REGISTRATION).click()
    header = driver.find_element(*TestLocators.REGISTRATION_HEADER).text
    assert header == 'Регистрация'

def test_successful_registration(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_FOR_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_NEW_NAME).clear()
    driver.find_element(*TestLocators.INPUT_NEW_NAME).send_keys('Frodo')
    driver.find_element(*TestLocators.INPUT_NEW_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_NEW_LOGIN).send_keys('fbaggins3@ya.ru')
    driver.find_element(*TestLocators.INPUT_NEW_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_NEW_PASSWORD).send_keys('qa123456')
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.LOGIN_HEADER_PAGE)))
    header = driver.find_element(*TestLocators.LOGIN_HEADER_PAGE).text
    assert header == 'Вход'

def test_error_registration(driver):
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((TestLocators.BUTTON_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
    driver.find_element(*TestLocators.LINK_FOR_REGISTRATION).click()
    driver.find_element(*TestLocators.INPUT_NEW_NAME).clear()
    driver.find_element(*TestLocators.INPUT_NEW_NAME).send_keys('Frodo')
    driver.find_element(*TestLocators.INPUT_NEW_LOGIN).clear()
    driver.find_element(*TestLocators.INPUT_NEW_LOGIN).send_keys('fbaggins3@ya.ru')
    driver.find_element(*TestLocators.INPUT_NEW_PASSWORD).clear()
    driver.find_element(*TestLocators.INPUT_NEW_PASSWORD).send_keys('qa123')
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    error = driver.find_element(*TestLocators.ERROR_PASSWORD).text
    assert error == 'Некорректный пароль'
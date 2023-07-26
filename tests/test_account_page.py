from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestAccountPage:

    def test_account_page(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_LOGIN).clear()
        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.LINK_FOR_PROFILE)))
        driver.find_element(*TestLocators.LINK_FOR_PROFILE).click()
        text = driver.find_element(*TestLocators.INPUT_ACCOUNT_LOGIN).get_attribute('value')
        assert text == 'testfox@ya.ru'

    def test_account_page_in_constructor(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_LOGIN).clear()
        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        header = driver.find_element(*TestLocators.TABLE_HEADER).text
        assert header == 'Соберите бургер'

    def test_account_page_in_baner(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_LOGIN).clear()
        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.HEADER_BANNER)))
        driver.find_element(*TestLocators.HEADER_BANNER).click()
        header = driver.find_element(*TestLocators.TABLE_HEADER).text
        assert header == 'Соберите бургер'

    def test_exit_account(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        driver.find_element(*TestLocators.INPUT_LOGIN).clear()
        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys('testFox@ya.ru')
        driver.find_element(*TestLocators.INPUT_PASSWORD).clear()
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys('testtest0101')
        driver.find_element(*TestLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_EXIT)))
        driver.find_element(*TestLocators.BUTTON_EXIT).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.LOGIN_HEADER_PAGE)))
        header = driver.find_element(*TestLocators.LOGIN_HEADER_PAGE).text
        assert header == 'Вход'

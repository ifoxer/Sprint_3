from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_locators import TestLocators


class TestMainPage:

    def test_main_page_chapter_bun(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.CHAPTER_BUN)))
        driver.find_element(*TestLocators.CHAPTER_SAUCE).click()
        driver.find_element(*TestLocators.CHAPTER_BUN).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUN_FIRST)))
        bun = driver.find_element(*TestLocators.BUN_FIRST).text
        assert bun == 'Флюоресцентная булка R2-D3'

    def test_main_page_chapter_sauce(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.CHAPTER_SAUCE)))
        driver.find_element(*TestLocators.CHAPTER_SAUCE).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.SAUCE_FIRST)))
        sauce = driver.find_element(*TestLocators.SAUCE_FIRST).text
        assert sauce == 'Соус Spicy-X'

    def test_main_page_chapter_topping(self, driver):
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.CHAPTER_TOPPING)))
        driver.find_element(*TestLocators.CHAPTER_TOPPING).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((TestLocators.TOPPING_FIRST)))
        topping = driver.find_element(*TestLocators.TOPPING_FIRST).text
        assert topping == 'Мясо бессмертных моллюсков Protostomia'

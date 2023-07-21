from faker import Faker
import pytest
from selenium import webdriver

fake = Faker()

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def fake_name():
    return fake.name()

@pytest.fixture(scope='function')
def fake_email():
    return fake.email()
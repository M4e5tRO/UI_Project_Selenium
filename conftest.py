import pytest
from selenium import webdriver

from .pages.create_account import CreateAccount
from .pages.eco_friendly import EcoFriendly
from .pages.sale import Sale


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.set_window_size(3840, 2160)
    yield chrome_driver
    chrome_driver.close()


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale(driver):
    return Sale(driver)

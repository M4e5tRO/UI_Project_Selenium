import pytest
import os
import allure
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from .pages.create_account import CreateAccount
from .pages.eco_friendly import EcoFriendly
from .pages.sale import Sale


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.set_window_size(3840, 2160)
    yield chrome_driver
    chrome_driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            screenshot_name = f'{datetime.now().strftime('%Y%m%d_%H%M%S')}_{item.name}.png'
            screenshot_path = f"screenshots/{screenshot_name}"
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")

            allure.attach(
                open(screenshot_path, "rb").read(),
                f'screenshot - {screenshot_name}',
                allure.attachment_type.PNG
            )


@pytest.fixture()
def create_account(driver):
    return CreateAccount(driver)


@pytest.fixture()
def eco_friendly(driver):
    return EcoFriendly(driver)


@pytest.fixture()
def sale(driver):
    return Sale(driver)

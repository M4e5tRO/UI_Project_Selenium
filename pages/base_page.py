from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select

from ..pages.locators import base_locators as loc


class BasePage:
    BASE_URL = 'https://magento.softwaretestingboard.com'
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.PAGE_URL:
            self.driver.get(f'{self.BASE_URL}{self.PAGE_URL}')
        else:
            raise NotImplementedError('Page can not be opened for this page class')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def sort_by(self, sort_by_value):
        select = self.find(loc.sort_by_loc)
        dd = Select(select)
        dd.select_by_value(f'{sort_by_value}')

    def switch_asc(self):
        switch_asc = self.find(loc.switch_asc_loc)
        switch_asc.click()

    def switch_desc(self):
        switch_desc = self.find(loc.switch_desc_loc)
        switch_desc.click()

import random
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from ..pages.base_page import BasePage
from ..pages.locators import eco_friendly_locators as loc


def paging_names(func):

    def wrapper(self):
        items_before = self.find_all(loc.item_name_loc)
        items_before_names = list(map(lambda item: item.text, items_before))

        func(self)

        items_after = self.find_all(loc.item_name_loc)
        items_after_names = list(map(lambda item: item.text, items_after))
        assert items_before_names != items_after_names, (
            f'Items before: {items_before_names}, Items after: {items_after_names}'
        )

    return wrapper


class EcoFriendly(BasePage):
    PAGE_URL = '/collections/eco-friendly.html'

    def check_sort_by_product_name_asc(self):
        items = self.find_all(loc.item_name_loc)
        items_names = list(map(lambda item: item.text, items))
        python_sort_asc = sorted(items_names)
        assert items_names == python_sort_asc, (
            f'Sorting "Product Name" is NOT ASC - Expected: {python_sort_asc}, Actual: {items_names}'
        )

    def check_sort_by_product_name_desc(self):
        items = self.find_all(loc.item_name_loc)
        items_names = list(map(lambda item: item.text, items))
        python_sort_desc = sorted(items_names, reverse=True)
        assert items_names == python_sort_desc, (
            f'Sorting "Product Name" in NOT DESC - Expected: {python_sort_desc}, Actual: {items_names}'
        )

    def check_sort_by_price_asc(self):
        prices = self.find_all(loc.item_price_loc)
        prices_text = list(map(lambda price: price.text, prices))
        python_sort_asc = sorted(prices_text)
        assert prices_text == python_sort_asc, (
            f'Sorting "Price" in NOT ASC - Expected: {prices_text}, Actual: {python_sort_asc}'
        )

    def check_sort_by_price_desc(self):
        prices = self.find_all(loc.item_price_loc)
        prices_text = list(map(lambda price: price.text, prices))
        python_sort_desc = sorted(prices_text, reverse=True)
        assert prices_text == python_sort_desc, (
            f'Sorting "Price" in NOT DESC - Expected: {prices_text}, Actual: {python_sort_desc}'
        )

    @paging_names
    def check_paging_next(self):
        paging_next = self.find(loc.paging_next_loc)
        paging_next.click()

    @paging_names
    def check_paging_prev(self):
        paging_prev = self.find(loc.paging_prev_loc)
        paging_prev.click()

    @paging_names
    def check_paging_item(self):
        items = self.find_all(loc.paging_item_loc)
        item: WebElement = random.choice(items)
        item.click()

    def check_limiter(self, limiter):

        current_url = self.driver.current_url

        select = self.find(loc.limiter_loc)
        dd = Select(select)
        dd.select_by_value(f'{limiter}')

        wait = WebDriverWait(self.driver, 15)
        wait.until(ec.url_changes(current_url))

        selected_value = self.find(loc.selected_limiter_loc).text

        assert limiter == selected_value, f'Expected limiter: {limiter}, Selected limiter: {selected_value}'

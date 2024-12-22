from ..pages.base_page import BasePage
from ..pages.locators import sale_locators as loc


class Sale(BasePage):
    PAGE_URL = '/sale.html'

    def check_main_sale_title(self, title):
        block_title = self.find(loc.main_sale_title_loc).text
        assert title == block_title, f'Expected result: {title}, Actual result: {block_title}'

    def check_main_sale_text(self, text):
        block_text = self.find(loc.main_sale_text_loc).text
        assert text == block_text, f'Expected result: {text}, Actual result: {block_text}'

    def check_main_sale_button_text(self, button_text):
        block_button_text = self.find(loc.main_sale_button_text_loc).text
        assert button_text == block_button_text, f'Expected result: {button_text}, Actual result: {block_button_text}'

    def check_main_block_link(self):
        block_link = self.find(loc.main_sale_loc)
        link_text = block_link.get_attribute("href")
        block_link.click()
        current_url = self.driver.current_url
        assert link_text == current_url, f'Expected result: {link_text}, Actual result: {current_url}'

    def check_men_sale_title(self, title):
        block_title = self.find(loc.men_sale_title_loc).text
        assert title == block_title, f'Expected result: {title}, Actual result: {block_title}'

    def check_men_sale_text(self, text):
        block_text = self.find(loc.men_sale_text_loc).text
        assert text == block_text, f'Expected result: {text}, Actual result: {block_text}'

    def check_men_sale_link_text(self, button_text):
        block_link_text = self.find(loc.men_sale_link_text_loc).text
        assert button_text == block_link_text, f'Expected result: {button_text}, Actual result: {block_link_text}'

    def check_men_block_link(self):
        block_link = self.find(loc.men_sale_loc)
        link_text = block_link.get_attribute("href")
        block_link.click()
        current_url = self.driver.current_url
        assert link_text == current_url, f'Expected result: {link_text}, Actual result: {current_url}'

    def check_women_sale_title(self, title):
        block_title = self.find(loc.women_sale_title_loc).text
        assert title == block_title, f'Expected result: {title}, Actual result: {block_title}'

    def check_women_sale_text(self, text):
        block_text = self.find(loc.women_sale_text_loc).text
        assert text == block_text, f'Expected result: {text}, Actual result: {block_text}'

    def check_women_sale_link_text(self, button_text):
        block_link_text = self.find(loc.women_sale_link_text_loc).text
        assert button_text == block_link_text, f'Expected result: {button_text}, Actual result: {block_link_text}'

    def check_women_block_link(self):
        block_link = self.find(loc.women_sale_loc)
        link_text = block_link.get_attribute("href")
        block_link.click()
        current_url = self.driver.current_url
        assert link_text == current_url, f'Expected result: {link_text}, Actual result: {current_url}'

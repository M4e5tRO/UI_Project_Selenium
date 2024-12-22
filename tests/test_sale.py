import allure

from ..test_data import data_list as dl


@allure.feature('Sale Page')
class TestSalePage:

    @allure.story('Test MAIN sale block')
    def test_main_sale_block(self, sale):
        sale.open_page()
        sale.check_main_sale_title(dl.main_sale_title)
        sale.check_main_sale_text(dl.main_sale_text)
        sale.check_main_sale_button_text(dl.main_sale_button_text)
        sale.check_main_block_link()

    @allure.story('Test MEN sale block')
    def test_men_sale_block(self, sale):
        sale.open_page()
        sale.check_men_sale_title(dl.men_sale_title)
        sale.check_men_sale_text(dl.men_sale_text)
        sale.check_men_sale_link_text(dl.men_sale_link_text)
        sale.check_men_block_link()

    @allure.story('Test WOMEN sale block')
    def test_women_sale_block(self, sale):
        sale.open_page()
        sale.check_women_sale_title(dl.women_sale_title)
        sale.check_women_sale_text(dl.women_sale_text)
        sale.check_women_sale_link_text(dl.women_sale_link_text)
        sale.check_women_block_link()

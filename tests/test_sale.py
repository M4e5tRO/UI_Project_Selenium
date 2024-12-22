from ..test_data import data_list as dl


def test_main_sale_block(sale):
    sale.open_page()
    sale.check_main_sale_title(dl.main_sale_title)
    sale.check_main_sale_text(dl.main_sale_text)
    sale.check_main_sale_button_text(dl.main_sale_button_text)
    sale.check_main_block_link()


def test_men_sale_block(sale):
    sale.open_page()
    sale.check_men_sale_title(dl.men_sale_title)
    sale.check_men_sale_text(dl.men_sale_text)
    sale.check_men_sale_link_text(dl.men_sale_link_text)
    sale.check_men_block_link()


def test_women_sale_block(sale):
    sale.open_page()
    sale.check_women_sale_title(dl.women_sale_title)
    sale.check_women_sale_text(dl.women_sale_text)
    sale.check_women_sale_link_text(dl.women_sale_link_text)
    sale.check_women_block_link()

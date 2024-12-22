from ..test_data import data_list as dl


def test_sort_by(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.sort_by(dl.sort_by_product_name_value)
    eco_friendly.switch_desc()
    eco_friendly.check_sort_by_product_name_desc()
    eco_friendly.switch_asc()
    eco_friendly.check_sort_by_product_name_asc()
    eco_friendly.sort_by(dl.sort_by_price_value)
    eco_friendly.switch_desc()
    eco_friendly.check_sort_by_price_desc()
    eco_friendly.switch_asc()
    eco_friendly.check_sort_by_price_asc()


def test_paging(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.check_paging_next()
    eco_friendly.check_paging_prev()
    eco_friendly.check_paging_item()


def test_limiter(eco_friendly):
    eco_friendly.open_page()
    eco_friendly.check_limiter(dl.limiter_24)
    eco_friendly.check_limiter(dl.limiter_36)
    eco_friendly.check_limiter(dl.limiter_12)

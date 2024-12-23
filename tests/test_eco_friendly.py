import allure
import pytest

from ..test_data import data_list as dl


@allure.feature('Eco Friendly')
class TestEcoFriendly:

    @pytest.mark.smoke
    @allure.story('Test Sorting')
    def test_sort_by(self, eco_friendly):
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

    @pytest.mark.regression
    @allure.story('Test Paging')
    def test_paging(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.check_paging_next()
        eco_friendly.check_paging_prev()
        eco_friendly.check_paging_item()

    @pytest.mark.extended
    @allure.story('Test Limiter')
    def test_limiter(self, eco_friendly):
        eco_friendly.open_page()
        eco_friendly.check_limiter(dl.limiter_24)
        eco_friendly.check_limiter(dl.limiter_36)
        eco_friendly.check_limiter(dl.limiter_12)

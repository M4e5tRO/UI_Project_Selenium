from selenium.webdriver.common.by import By


main_sale_loc = (By.CSS_SELECTOR, '.sale-main')
main_sale_title_loc = (By.XPATH, '//*[contains(@class, "sale-main")]/descendant::*[@class="info"]')
main_sale_text_loc = (By.XPATH, '//*[contains(@class, "sale-main")]/descendant::*[@class="title"]')
main_sale_button_text_loc = (By.XPATH, '//*[contains(@class, "sale-main")]/descendant::*[@class="more button"]')

men_sale_loc = (By.CSS_SELECTOR, '.sale-mens')
men_sale_title_loc = (By.XPATH, '//*[contains(@class, "sale-mens")]/descendant::*[@class="title"]')
men_sale_text_loc = (By.XPATH, '//*[contains(@class, "sale-mens")]/descendant::*[@class="info"]')
men_sale_link_text_loc = (By.XPATH, '//*[contains(@class, "sale-mens")]/descendant::*[@class="more icon"]')

women_sale_loc = (By.CSS_SELECTOR, '.sale-women')
women_sale_title_loc = (By.XPATH, '//*[contains(@class, "sale-women")]/descendant::*[@class="title"]')
women_sale_text_loc = (By.XPATH, '//*[contains(@class, "sale-women")]/descendant::*[@class="info"]')
women_sale_link_text_loc = (By.XPATH, '//*[contains(@class, "sale-women")]/descendant::*[@class="more icon"]')

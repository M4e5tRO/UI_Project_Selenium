from selenium.webdriver.common.by import By


item_name_loc = (By.CLASS_NAME, 'product-item-link')
item_price_loc = (By.CLASS_NAME, 'price-wrapper ')

paging_next_loc = (By.XPATH, '(//a[contains(@class, "next")])[2]')
paging_prev_loc = (By.XPATH, '(//a[contains(@class, "previous")])[2]')
paging_item_loc = (By.XPATH, '(//li[@class="item current"])[2]/following-sibling::li[@class="item"]/a')

limiter_loc = (By.XPATH, '(//select[@id="limiter"])[2]')
selected_limiter_loc = (By.XPATH, '(//select[@id="limiter"])[2]/child::*[@selected="selected"]')

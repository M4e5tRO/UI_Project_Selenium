from selenium.webdriver.common.by import By


item_name_loc = (By.CSS_SELECTOR, '.product-image-photo')
item_price_loc = (By.XPATH, '//*[@class="price-wrapper "]/child::*[@class="price"]')

paging_next_loc = (By.XPATH, '(//a[contains(@class, "next")])[2]')
paging_prev_loc = (By.XPATH, '(//a[contains(@class, "previous")])[2]')
paging_item_loc = (By.XPATH, '(//li[@class="item current"])[2]/following-sibling::li[@class="item"]/a')

limiter_loc = (By.XPATH, '(//select[@id="limiter"])[2]')
selected_limiter_loc = (By.XPATH, '(//select[@id="limiter"])[2]/child::*[@selected="selected"]')

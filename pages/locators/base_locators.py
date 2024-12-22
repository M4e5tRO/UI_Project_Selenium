from selenium.webdriver.common.by import By


sort_by_loc = (By.XPATH, '(//select[@id="sorter"])[1]')
switch_asc_loc = (By.XPATH, '(//a[contains(@class, "sort-desc")])[1]')
switch_desc_loc = (By.XPATH, '(//a[contains(@class, "sort-asc")])[1]')

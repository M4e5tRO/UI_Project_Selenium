from selenium.webdriver.common.by import By


first_name_loc = (By.ID, 'firstname')
last_name_loc = (By.ID, 'lastname')
email_loc = (By.ID, 'email_address')
password_loc = (By.ID, 'password')
conf_password_loc = (By.ID, 'password-confirmation')
create_btn_loc = (By.CSS_SELECTOR, '.action.submit')

success_message_loc = (By.CSS_SELECTOR, '.page.messages')
contact_info_loc = (By.XPATH, '//*[contains(@class, "box-information")]/descendant::p')

first_name_error_loc = (By.ID, 'firstname-error')
last_name_error_loc = (By.ID, 'lastname-error')
email_error_loc = (By.ID, 'email_address-error')
password_error_loc = (By.ID, 'password-error')
conf_password_error_loc = (By.ID, 'password-confirmation-error')

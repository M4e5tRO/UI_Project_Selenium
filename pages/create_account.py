from ..pages.base_page import BasePage
from ..pages.locators import create_account_locators as loc


class CreateAccount(BasePage):
    PAGE_URL = '/customer/account/create/'

    def fill_in_form(self, first_name, last_name, email, password, conf_password):

        fist_name_field = self.find(loc.first_name_loc)
        last_name_field = self.find(loc.last_name_loc)
        email_field = self.find(loc.email_loc)
        password_field = self.find(loc.password_loc)
        conf_password_field = self.find(loc.conf_password_loc)
        create_btn = self.find(loc.create_btn_loc)

        fist_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        password_field.send_keys(password)
        conf_password_field.send_keys(conf_password)

        create_btn.click()

    def check_redirection_page_url(self, account_url):
        url = self.driver.current_url
        assert account_url == url, f'Expected result: {account_url}, Actual result: {url}'

    def check_success_message(self, message):
        page_message = self.find(loc.success_message_loc)
        message_text = page_message.text
        assert message == message_text, f'Expected result: {message}, Actual result: {message_text}'

    def check_contact_info(self, first_name, last_name, email):
        full_name = f'{first_name} {last_name}'

        contact_info = self.find(loc.contact_info_loc)
        contact_text = contact_info.text.split("\n")
        full_name_text = contact_text[0]
        email_text = contact_text[1]
        assert full_name == full_name_text, f'Expected result: {full_name}, Actual result: {full_name_text}'
        assert email == email_text, f'Expected result: {email}, Actual result: {email_text}'

    def check_inline_error_for_required_fields(self, inline_error):
        create_btn = self.find(loc.create_btn_loc)
        create_btn.click()

        first_name_error_text = self.find(loc.first_name_error_loc).text
        last_name_error_text = self.find(loc.last_name_error_loc).text
        password_error_text = self.find(loc.password_error_loc).text
        conf_password_error_text = self.find(loc.conf_password_error_loc).text
        assert inline_error == first_name_error_text, (
            f'Expected result: {inline_error}, Actual result: {first_name_error_text}'
        )
        assert inline_error == last_name_error_text, (
            f'Expected result: {inline_error}, Actual result: {last_name_error_text}'
        )
        assert inline_error == password_error_text, (
            f'Expected result: {inline_error}, Actual result: {password_error_text}'
        )
        assert inline_error == conf_password_error_text, (
            f'Expected result: {inline_error}, Actual result: {conf_password_error_text}'
        )

    def check_password_errors(self, invalid_pass_length, pass_error):

        password_field = self.find(loc.password_loc)
        password_field.send_keys(invalid_pass_length)

        create_btn = self.find(loc.create_btn_loc)
        create_btn.click()

        password_error_text = self.find(loc.password_error_loc).text
        assert pass_error == password_error_text, f'Expected result: {pass_error}, Actual result: {password_error_text}'

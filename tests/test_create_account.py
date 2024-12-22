from ..test_data import data_list as dl


def test_create_account(create_account):
    create_account.open_page()
    create_account.fill_in_form(dl.first_name, dl.last_name, dl.email, dl.password, dl.conf_password)
    create_account.check_redirection_page_url(dl.account_url)
    create_account.check_success_message(dl.success_message)
    create_account.check_contact_info(dl.first_name, dl.last_name, dl.email)


def test_inline_error_for_required_fields(create_account):
    create_account.open_page()
    create_account.check_inline_error_for_required_fields(dl.req_field_inline_error)


def test_invalid_password_length(create_account):
    create_account.open_page()
    create_account.check_password_errors(dl.invalid_pass_length, dl.pass_inline_error_length)

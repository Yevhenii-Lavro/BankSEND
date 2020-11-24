from pages.sign_in_page import SignInPage
import pytest

link = "https://test.banksend.com/admin/sign-in"


@pytest.mark.regression
class TestLoginPage:

    def test_should_be_sign_in_page(self, browser):
        page = SignInPage(browser, link)
        page.open()
        page.should_be_sign_in_page()

    def test_login(self, browser):
        page = SignInPage(browser, link)
        page.open()
        page.enter_username()
        page.enter_password()
        page.click_sign_in_button()
        page.user_logged()

    def test_wrong_credential(self, browser):
        page = SignInPage(browser, link)
        page.open()
        page.enter_wrong_username()
        page.enter_wrong_password()
        page.click_sign_in_button()
        page.should_be_error_text()
        page.error_text_according_to_requirements()

    def test_login_as_merchant(self, browser):
        page = SignInPage(browser, self)
        page.login_as_merchant()

    def test_login_as_superadmin(self, browser):
        page = SignInPage(browser, self)
        page.login_as_superadmin()

    def test_empty_field_message(self, browser):
        page = SignInPage(browser, link)
        page.open()
        page.enter_username()
        page.enter_wrong_password()
        page.clear_password()
        page.should_be_message_for_empty_field_password()

    def test_title_of_sign_in_page(self, browser):
        page = SignInPage(browser, link)
        page.open()
        page.title_of_sign_in_page()

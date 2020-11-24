from selenium.webdriver.common.keys import Keys
from .locators import SignInPageLocators
from .locators import LoggedPageLocators
from .base_page import BasePage


class SignInPage(BasePage):
    def should_be_sign_in_page(self):
        self.should_be_login_field()
        self.should_be_login_password()
        self.should_be_login_button()

    def should_be_login_field(self):
        assert self.is_element_present(*SignInPageLocators.LOGIN_USERNAME)

    def should_be_login_password(self):
        assert self.is_element_present(*SignInPageLocators.LOGIN_PASSWORD)

    def should_be_login_button(self):
        assert self.is_element_present(*SignInPageLocators.LOGIN_BUTTON)

    def user_logged(self):
        self.is_element_present(*LoggedPageLocators.USER_LOGGED)
        assert "dashboard" in self.browser.current_url, "User isn't logged"

    def enter_username(self):
        username = self.browser.find_element(*SignInPageLocators.LOGIN_USERNAME)
        username.send_keys("manager-test@banksend.com")

    def enter_password(self):
        password = self.browser.find_element(*SignInPageLocators.LOGIN_PASSWORD)
        password.send_keys("12345678")

    def clear_password(self):
        password = self.browser.find_element(*SignInPageLocators.LOGIN_PASSWORD)
        password.send_keys(Keys.BACKSPACE)

    def click_sign_in_button(self):
        button = self.browser.find_element(*SignInPageLocators.LOGIN_BUTTON)
        button.click()

    def should_be_error_text(self):
        assert self.is_element_present(*SignInPageLocators.ERROR_MESSAGE)

    def error_text_according_to_requirements(self):
        assert self.browser.find_element(
            *SignInPageLocators.ERROR_MESSAGE).text == "The email or password you entered is incorrect",\
            "Not correct massage about error type"

    def enter_wrong_username(self):
        wrongusername = self.browser.find_element(*SignInPageLocators.LOGIN_USERNAME)
        wrongusername.send_keys("superadmin-test@banksend.comm")

    def enter_wrong_password(self):
        wrongpassword = self.browser.find_element(*SignInPageLocators.LOGIN_PASSWORD)
        wrongpassword.send_keys("1")

    def should_be_message_for_empty_field_password(self):
        assert self.is_element_present(*SignInPageLocators.EMPTY_FIELD)

    def title_of_sign_in_page(self):
        print(self.browser.title)
        assert self.browser.title == "Merchant admin tools. Sign-In | BankSEND®", "Wrong title for Sign in page"

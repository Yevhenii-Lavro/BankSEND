from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from .locators import SignInPageLocators
from .locators import LoggedPageLocators


class BasePage:
    def __init__(self, browser: webdriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=2):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def login_as_merchant(self):
        self.link = "https://test.banksend.com/admin/sign-in"
        self.browser.get(self.link)
        usermail = self.browser.find_element(*SignInPageLocators.LOGIN_USERNAME)
        userpassword = self.browser.find_element(*SignInPageLocators.LOGIN_PASSWORD)
        sign_in_button = self.browser.find_element(*SignInPageLocators.LOGIN_BUTTON)
        usermail.send_keys("owner-test-ca-autotest@banksend.com")
        userpassword.send_keys("12345678")
        sign_in_button.click()
        self.is_element_present(*LoggedPageLocators.USER_LOGGED)
        assert "dashboard" in self.browser.current_url, "User isn't logged"

    def login_as_superadmin(self):
        self.link = "https://test.banksend.com/admin/sign-in"
        self.browser.get(self.link)
        usermail = self.browser.find_element(*SignInPageLocators.LOGIN_USERNAME)
        userpassword = self.browser.find_element(*SignInPageLocators.LOGIN_PASSWORD)
        sign_in_button = self.browser.find_element(*SignInPageLocators.LOGIN_BUTTON)
        usermail.send_keys("superadmin-test@banksend.com")
        userpassword.send_keys("12345678")
        sign_in_button.click()
        self.is_element_present(*LoggedPageLocators.USER_LOGGED)
        assert "dashboard" in self.browser.current_url, "User isn't logged"

    def logout(self):
        logout_button = self.browser.find_element(*LoggedPageLocators.LOGOUT_BUTTON)
        logout_button.click()
        assert self.is_element_present(*SignInPageLocators.LOGIN_USERNAME)

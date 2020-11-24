from .base_page import BasePage
from .locators import DashboardPageLocators
from selenium.webdriver.common.action_chains import ActionChains
import datetime


class DashboardPage(BasePage):
    def should_be_dashboard_page(self):
        self.should_be_dashboard()
        self.should_be_daily_summary_button()
        self.should_be_transactions_button()

    def should_be_transactions_button(self):
        assert self.is_element_present(*DashboardPageLocators.TRANSACTIONS_BOARD_BUTTON)

    def should_be_daily_summary_button(self):
        assert self.is_element_present(*DashboardPageLocators.DAILY_SUMMARY_BUTTON)

    def should_be_dashboard(self):
        assert self.is_element_present(*DashboardPageLocators.DASHBOARD)

    def shoud_be_dashboard_in_url(self):
        assert "dashboard" in self.browser.current_url, "User is on dashboard page"

    def transaction_board_displayed_by_default(self):
        self.browser.execute_script("window.scrollBy(0, 90);")
        assert self.browser.find_element(*DashboardPageLocators.TRANSACTIONS_BOARD_BUTTON).get_attribute(
            "class") == "nav-link active", "Transaction tab not displayed by default"

    def change_tab_on_dashboard(self):
        if self.browser.find_element(*DashboardPageLocators.TRANSACTIONS_BOARD_BUTTON).get_attribute(
                "class") == "nav-link active":
            self.browser.find_element(*DashboardPageLocators.DAILY_SUMMARY_BUTTON).click()
            print("Tab is changed to Daily Summary")
        elif self.browser.find_element(DashboardPageLocators.DAILY_SUMMARY_BUTTON).get_attribute(
                "class") == "nav-link active":
            self.browser.find_element(*DashboardPageLocators.TRANSACTIONS_BOARD_BUTTON).click()
            print("Tab is changed to Transaction")
        else:
            return print("No one button is active")

    def should_be_tab_title_daily_summary(self):
        assert self.browser.find_element(
            *DashboardPageLocators.DASHBOARD_DAILY_SUMMARY_TITLE).text == "Daily summary by transaction type", \
            "It's not tab Daily summary"

    def changing_date_filter_from(self):
        filter_from = self.browser.find_element(*DashboardPageLocators.FILTER_FROM)
        assert filter_from.get_attribute("placeholder") == "yyyy-mm-dd", "Wrong placeholder for FROM field"
        ActionChains(self.browser).double_click(filter_from)
        filter_from.clear()
        filter_from.send_keys("2020-09-18")
        assert filter_from.get_attribute("value") == "2020-09-18", "Value for 'date from' doesn't changed"

    def changing_date_filter_to(self):
        filter_to = self.browser.find_element(*DashboardPageLocators.FILTER_TO)
        assert filter_to.get_attribute("placeholder") == "yyyy-mm-dd", "Wrong placeholder for TO field"
        ActionChains(self.browser).double_click(filter_to)
        filter_to.clear()
        filter_to.send_keys("2020-10-18")
        assert filter_to.get_attribute("value") == "2020-10-18", "Value for 'date to' doesn't changed"

    def should_be_reset_button(self):
        assert self.is_element_present(*DashboardPageLocators.RESET_BUTTON)

    def reset_button_works(self):
        reset_button = self.browser.find_element(*DashboardPageLocators.RESET_BUTTON)
        reset_button.click()
        self.is_disappeared(*DashboardPageLocators.RESET_BUTTON)
        date_today = str(datetime.datetime.today().date())
        filter_to = self.browser.find_element(*DashboardPageLocators.FILTER_TO)
        assert filter_to.get_attribute("value") == date_today, "Reset button doesn't work"

    def title_of_dashboard_page(self):
        print(self.browser.title)
        assert self.browser.title == "Dashboard | Canada Autotest Company | BankSEND®"

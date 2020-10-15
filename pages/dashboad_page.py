from .base_page import BasePage
from .locators import DashboardPageLocators

class DashboardPage(BasePage):
    def should_be_dashboard_page(self):
        self.should_be_dashboard()
        self.should_be_daily_summary_button()
        self.should_be_transactions_button()


    def should_be_transactions_button(self):
        assert self.is_element_present(*DashboardPageLocators.TRANSACTIONS)

    def should_be_daily_summary_button(self):
        assert self.is_element_present(*DashboardPageLocators.DAILY_SUMMARY)

    def should_be_dashboard(self):
        assert self.is_element_present(*DashboardPageLocators.DASHBOARD)

    def shoud_be_dashboard_in_url(self):
        assert "dashboard" in self.browser.current_url, "User is on dashboard page"




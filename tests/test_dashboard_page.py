from pages.dashboad_page import DashboardPage
import pytest

link = "https://test.banksend.com/admin/dashboard"


class TestDashboardPage:

    @pytest.mark.regression
    def test_is_it_dashboard(self, browser):
        page = DashboardPage(browser, link)
        page.login_as_merchant()
        page.should_be_dashboard_page()
        page.shoud_be_dashboard_in_url()

    @pytest.mark.regression
    def test_transaction_board_displayed_by_default(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.transaction_board_displayed_by_default()

    @pytest.mark.regression
    def test_changing_tab_to_daily_summary(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.change_tab_on_dashboard()
        page.should_be_tab_title_daily_summary()

    @pytest.mark.regression
    def test_reset_button_after_changing_filter_from(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.changing_date_filter_from()
        page.should_be_reset_button()

    @pytest.mark.regression
    def test_reset_button_after_changing_filter_to(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.changing_date_filter_to()
        page.should_be_reset_button()

    @pytest.mark.regression
    def test_reset_button_work(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.changing_date_filter_to()
        page.reset_button_works()

    @pytest.mark.regression
    def test_title_of_dashboard_page(self, browser):
        page = DashboardPage(browser, self)
        page.login_as_merchant()
        page.title_of_dashboard_page()

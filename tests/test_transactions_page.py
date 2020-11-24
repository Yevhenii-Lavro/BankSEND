from pages.transactions_page import TransactionsPage
import pytest
import time

link = "https://test.banksend.com/admin/transactions"


@pytest.mark.regression
class TestTransactionsPage:

    def test_redirect_to_transaction_page(self, browser):
        page = TransactionsPage(browser, link)
        page.login_as_merchant()
        page.click_to_menu_button_transactions()
        page.should_be_page_name()

    def test_title_of_page(self, browser):
        page = TransactionsPage(browser, link)
        page.login_as_merchant()
        page.open()
        page.title_of_the_page()

    def test_elements_is_present_in_page_for_merchant(self, browser):
        page = TransactionsPage(browser, link)
        page.login_as_merchant()
        page.open()
        page.should_be_merchant_income()
        page.find_needed_customer()
        page.current_page()

    def test_elements_is_present_in_page_for_superadmin(self, browser):
        page = TransactionsPage(browser, link)
        page.login_as_superadmin()
        page.redirect_to_admin_dashboard()
        page.chose_ca_autotest_company()
        page.open()
        page.should_be_banksend_income()
        time.sleep(3)
        page.should_be_clear_filter_button()

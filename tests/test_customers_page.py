from pages.customers_page import CustomerPage
import pytest
import time


@pytest.mark.regression
class TestCustomerPage:

    def test_redirect_to_customer_page_by_admin(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_superadmin()
        page.should_be_customer_menu_button()
        page.go_to_customer_page()
        page.should_be_customer_page()
        page.should_be_merchant_column()
        page.should_be_id_column()
        page.should_be_name_column()
        page.should_be_registered_column()
        page.should_be_last_transaction_column()
        page.should_be_in_column()
        page.should_be_in_trx_column()
        page.should_be_out_v_column()
        page.should_be_out_v_trx_column()
        page.should_be_out_nv_column()
        page.should_be_out_nv_trx_column()
        page.should_be_out_cd_column()
        page.should_be_out_cd_trx_column()
        page.should_be_currency_column()
        page.should_be_status_column()

    def test_dropdown_filter_by(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_superadmin()
        page.go_to_customer_page()
        page.select_registered_filter()
        time.sleep(2)
        page.select_last_transaction_filter()
        time.sleep(2)

    def test_reset_button(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.select_registered_filter()
        page.enter_date_from()
        page.enter_date_to()
        page.click_reset_button()

    def test_show_entries(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.show_list_dropdown()

    def test_login_as_merchant_to_customers_page(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.should_be_balance_for_merchant()
        page.not_displayed_merchant_column()
        page.should_be_transfer_button()

    def test_search_date(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.should_be_balance_for_merchant()
        page.should_be_search_field()
        page.enter_text_in_search_field()
        time.sleep(1)
        page.should_be_customer_profile_link()
        page.should_be_last_transaction()
        page.last_transaction_date()

    def test_search_currency(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.should_be_balance_for_merchant()
        page.should_be_search_field()
        page.enter_usd_into_search()  # for CA company autotest - where search can't find this currency
        time.sleep(1)
        page.entered_currency_is_not_present()

    def test_title_for_customers_page(self, browser):
        page = CustomerPage(browser, self)
        page.login_as_merchant()
        page.go_to_customer_page()
        page.title_of_customer_page()

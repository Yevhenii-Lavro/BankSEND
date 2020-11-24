from pages.customer_profile_page import CustomerProfilePage
import pytest
import time

link = "https://test.banksend.com/admin/customer-profile?customerId=2&merchantId=5"


@pytest.mark.regression
class TestCustomerProfilePage:
    def test_redirect_to_customer_profile(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.should_be_customer_profile_page()

    def test_title_of_customer_profile_page(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.title_of_customer_profile_page()

    def test_elements_is_present_on_the_customer_profile_page(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.browser.maximize_window()
        page.browser.set_window_size(2500, 1800)
        page.balance_is_present()
        page.should_be_present_customer_block_and_his_details()
        page.should_be_transactions_list_and_his_attributes()
        page.should_be_table_with_transactions_summary()
        page.changing_tab_summary_or_payment_method()
        page.should_be_table_with_payment_methods()
        page.changing_tab_summary_or_payment_method()
        page.should_be_table_with_transactions_summary()

    def test_block_the_customer(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.check_active_status()
        page.block_the_customer()
        page.check_blocked_status()
        page.block_the_customer()  # activate customer

    def test_block_the_incoming_transaction_for_customer(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.block_the_incoming_transaction_for_customer()
        page.check_blocked_status_for_incoming()
        page.block_the_incoming_transaction_for_customer()
        page.check_active_status_for_incoming()

    def test_block_the_outgoing_to_verified_for_customer(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.block_the_outgoing_verified_transaction()
        page.check_blocked_status_for_outgoing_verified()
        page.block_the_outgoing_verified_transaction()
        page.check_active_status_for_outgoing_verified()

    def test_block_the_outgoing_to_not_verified_for_customer(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.block_the_outgoing_not_verified_transaction()
        page.check_blocked_status_for_outgoing_not_verified()
        page.block_the_outgoing_not_verified_transaction()
        page.check_active_status_for_outgoing_not_verified()

    def test_block_the_outgoing_to_customer_defined_for_customer(self, browser):
        page = CustomerProfilePage(browser, link)
        page.login_as_merchant()
        page.open()
        page.block_the_outgoing_to_customer_defined_transaction()
        page.check_blocked_status_for_outgoing_customer_defined()
        page.block_the_outgoing_to_customer_defined_transaction()
        page.check_active_status_for_outgoing_customer_defined()

    def test_get_balance_button(self, browser):
        page = CustomerProfilePage(browser, link)
        page.check_count_of_get_balance()
        page.login_as_merchant()
        page.open()
        page.changing_tab_summary_or_payment_method()
        page.balance_button_click()
        page.check_second_time_count_of_get_balance()

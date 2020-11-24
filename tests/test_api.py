from pages.api import Api, ReturnBasePage
import pytest
import time

link = "https://test.banksend.com"


@pytest.mark.smoke
class TestApiMerchantBalanceController:
    @pytest.mark.parametrize('currency', ['CAD', 'USD'])
    def test_get_balance(self, currency):
        api = Api(link)
        api.get_balance(currency)


@pytest.mark.smoke
@pytest.mark.parametrize('currency', ['CAD', 'USD'])
class TestApiMerchantTransactionController:
    def test_transaction_list(self, currency):
        api = Api(link)
        api.transaction_list(currency)


@pytest.mark.smoke
class TestAuthenticationController:
    def test_login(self):
        api = Api(link)
        password = "12345678"
        username = "superadmin-test@banksend.com"
        api.login(password, username)


@pytest.mark.smoke
@pytest.mark.parametrize('currency', ['CAD', 'USD'])
class TestFees:
    @pytest.mark.smoke
    def test_fee_for_send_to_verified(self, currency, browser):
        self.test_fee_for_incoming_repeat(currency, browser)
        api = Api(link)
        api.settled_transaction()
        elements = api.action_list_to_verified(currency)["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        typ = "OUTGOING_VERIFIED"
        assert all(elem in result for elem in
                   api.output_fee_from_settings(settings, typ,
                                                currency)), \
            f"Fee calculation for send to verified in {currency}isn't correct!"

    @pytest.mark.smoke
    def test_fee_for_send_to_not_verified(self, currency, browser):
        self.test_fee_for_incoming_repeat(currency, browser)
        api = Api(link)
        api.settled_transaction()
        elements = api.action_list_to_not_verified(currency)["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        typ = "OUTGOING_NOT_VERIFIED"
        assert all(elem in result for elem in
                   api.output_fee_from_settings(settings, typ,
                                                currency)), \
            f"Fee calculation for send to not verified in {currency} isn't correct!"

    def test_fee_for_incoming_repeat(self, currency, browser):
        api = Api(link)
        self.link = api.payment_form_repeat(currency)[0]
        page = ReturnBasePage(browser, self.link)
        page.open()
        page.should_be_bank_header()
        page.chose_radiobutton()
        time.sleep(3)
        page.chose_accept_button_for_income()
        elements = api.action_list_incoming()["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        assert all(elem in result for elem in
                   api.output_fee_for_income_repeat(settings,
                                                    currency)), \
            f"Fee calculation for income repeat in {currency} transactions not correct"

    def test_fee_for_incoming_first_time(self, currency, browser):
        api = Api(link)
        self.link = api.payment_form_first_time(currency)[0]
        page = ReturnBasePage(browser, self.link)
        page.open()
        time.sleep(5)
    #    page.scroll_iframe()
        browser.switch_to.frame(0)
    #    page.scroll_second_iframe()
        browser.switch_to.frame(0)
        page.should_be_continue_button()
    #    browser.maximize_window()
    #    browser.set_window_size(4096, 3112)
        page.scroll_to_view_continue_button()
        page.click_continue()
        page.select_bank_account()
        page.enter_username()
        page.enter_password()
        page.click_sumbit_button()
        browser.switch_to.default_content()
        page.should_be_card_header()
        page.chose_radiobutton_first_time(currency)
        time.sleep(1)
        page.chose_accept_button_for_income()
        time.sleep(1)
        page.should_be_successfully_message()
        elements = api.action_list_incoming()["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        assert all(elem in result for elem in
                   api.output_fee_for_income_first_time(settings,
                                                        currency)), \
            f"Fee calculation for income first time in {currency} transaction not correctly"

    def test_fee_send_to_customer_defined_first_time(self, currency, browser):
        self.test_fee_for_incoming_repeat(currency, browser)
        api = Api(link)
        api.settled_transaction()
        api.send_to_customer_defined_first_time(currency)
        #        self.link = api.send_to_customer_defined_first_time(currency)
        #        browser.get(self.link)
        self.link = "https://mail.simplepin.com"
        page = ReturnBasePage(browser, self.link)
        page.open()
        time.sleep(1)
        page.enter_username_email()
        page.enter_password_email()
        page.select_dropdown_email()
        page.click_submit_email()
        time.sleep(10)
        page.refresh_page()
        page.found_unread_email()
        page.scroll_the_page()
        page.switch_to_iframe_email()
        page.should_be_elements_in_email(currency)
        page.should_be_transaction_id_in_email()
        page.click_accept_button_in_email()
        page.switch_window()
        page.should_be_elements_on_activate_page(currency)
        page.should_be_default_language_and_additional()
        page.should_be_logos_on_activate_page()
        page.input_sms_code()
        page.click_activate_button()
        time.sleep(5)
    #    page.should_be_first_frame()
        print(browser.window_handles)
        print(browser.current_window_handle)
        time.sleep(3)
        browser.switch_to.frame(0)
        #    page.should_be_frame()
        browser.switch_to.frame(0)  # plaid-link-iframe-1
        page.scroll_to_view_continue_button()
        page.click_continue()
        page.select_bank_account()
        page.enter_username()
        page.enter_password()
        page.click_sumbit_button()
        browser.switch_to.default_content()
        page.should_be_card_header()
        page.chose_radiobutton_first_time_customer_defined()
        time.sleep(1)
        page.chose_accept_button()
        time.sleep(1)
        page.should_be_successfully_message()
        elements = api.action_list_to_customer_defined(currency)["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        assert all(elem in result for elem in api.output_fee_for_to_customer_defined_first_time(settings, currency)), \
            f"Fee calculation for 'to customer defined first time' in {currency} transaction not correctly"

    def test_fee_send_to_customer_defined_repeat(self, currency, browser):
        self.test_fee_for_incoming_repeat(currency, browser)
        api = Api(link)
        api.settled_transaction()
        api.send_to_customer_defined_repeat(currency)
        self.link = "https://mail.simplepin.com"
        page = ReturnBasePage(browser, self.link)
        page.open()
        page.enter_username_email()
        page.enter_password_email()
        page.select_dropdown_email()
        page.click_submit_email()
        time.sleep(10)
        page.refresh_page()
        page.found_unread_email()
        page.scroll_the_page()
        page.switch_to_iframe_email()
        page.should_be_elements_in_email(currency)
        page.should_be_transaction_id_in_email()
        page.click_accept_button_in_email()
        page.switch_window()
        page.input_sms_code()
        page.click_activate_button()
        page.should_be_bank_header()
        page.chose_radiobutton()
        page.chose_accept_button()
        elements = api.action_list_to_customer_defined(currency)["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        assert all(elem in result for elem in api.output_fee_for_to_customer_defined_repeat(settings, currency)), \
            f"Fee calculation for 'to customer defined repeat' in {currency} transaction not correctly"

    @pytest.mark.test
    def test_transfer_after_income_transaction(self, browser, currency):
        api = Api(link)
        self.test_fee_for_incoming_first_time(currency, browser)
        api.settled_transaction()
        api.initiate_transfer(currency)
        elements = api.action_list_for_transfer()["content"]
        result = []
        for element in elements:
            result.append(element["amount"])
        print(result)
        settings = api.fee_settings(currency)
        assert all(elem in result for elem in api.output_fee_for_transfer(settings, currency)), \
            f"Fee calculation for transfer in {currency} not correctly"
        api.get_balance(currency)
    #    page = ReturnBasePage(browser, link)
    #    page.login_as_merchant()
    #    page.check_merchant_balance_in_ui()




import itertools
import random
import requests
from .locators import CustomersPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from pages.locators import PaymentFormLocators
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import psycopg2
import math

global customer_id
customer_id = 17
global uuid
global iid
global merchant_id
global transfer_id


class Api:
    _s = requests.session()
    link = None

    def __init__(self, link):
        self.link = link

    @staticmethod
    def headers(currency):
        usa_headers = {"MerchantToken": "goodtry", "MerchantID": "Merchant-US-Autotest"}
        canada_headers = {"MerchantToken": "goodtry", "MerchantID": "Merchant-CA-Autotest"}
        if currency == "CAD":
            return canada_headers
        elif currency == "USD":
            return usa_headers

    def login(self, password, username):
        data = {"password": password, "username": username}
        response = self._s.post(self.link + "/api/v1/auth/sign_in", json=data)
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Unable to log in"
        return response

    def authorize(self, username, password):
        res = self.login(username, password)
        if res.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        session_token = res.headers.get("Authorization")
        new_headers = {"Authorization": f"Bearer {session_token}"}
        return new_headers

    #        cookie = requests.cookies.create_cookie("Authorization", "Bearer" + str(session_token))
    #        self._s.cookies.set_cookie(cookie)

    def get_balance(self, currency):
        response = requests.get(self.link + "/api/v1/balance", headers=self.headers(currency))
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Status code for Get Balance form != 200"
        body = response.json()
        print(body[0]["available_amount"])
        amount = body[0]["available_amount"]
        return amount

    #    print(response.json()["available_amount"])

    def payment_form_first_time(self, currency):
        global uuid
        global iid
        response = requests.post(self.link + "/api/v1/transactions/incoming/payment_form",
                                 headers=self.headers(currency), json=self.payment_from_json_first_time(currency))
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for payment form != 200"
        print(response.json()["payment_form"].split("/")[5])
        uuid = response.json()["payment_form"].split("/")[5]
        url = response.json()["payment_form"]
        print(url)
        self.find_transaction(currency)
        print(iid)
        return [url, uuid, iid]

    def payment_form_repeat(self, currency):
        global iid
        global uuid
        response = requests.post(self.link + "/api/v1/transactions/incoming/payment_form",
                                 headers=self.headers(currency), json=self.payment_from_json_repeat(currency))
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for payment form != 200"
        uuid = response.json()["payment_form"].split("/")[5]
        url = response.json()["payment_form"]
        print(url)
        self.find_transaction(currency)
        print(iid)
        return [url, uuid, iid]

    def transaction_list(self, currency):
        response = requests.get(self.link + "/api/v1/transactions/list", headers=self.headers(currency))
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Transaction list not available"

    def send_to_customer_defined_first_time(self, currency):
        response = requests.post(self.link + "/api/v1/transactions/outgoing/send_to_customer_defined",
                                 headers=self.headers(currency),
                                 json=self.send_to_customer_defined_json_first_time(currency))
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for customer defined != 200"

    #        return response.json()["payment_form_url"]

    def send_to_customer_defined_repeat(self, currency):
        response = requests.post(self.link + "/api/v1/transactions/outgoing/send_to_customer_defined",
                                 headers=self.headers(currency),
                                 json=self.send_to_customer_defined_json_repeat(currency))
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for customer defined != 200"

    def send_to_not_verified(self, currency):
        response = requests.post(self.link + "/api/v1/transactions/outgoing/send_to_not_verified",
                                 headers=self.headers(currency), json=self.send_to_not_verified_json(currency))
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Status code for not verified != 200"
        return response

    def send_to_verified(self, currency):
        response = requests.post(self.link + "/api/v1/transactions/outgoing/send_to_verified",
                                 headers=self.headers(currency),
                                 json=self.send_to_verified_json(currency))
        print(f"\n{response.status_code}")
        print(response.text)
        assert response.status_code == 200, "Status code for to verified != 200"
        return response

    def transaction_id_to_verified(self, currency):
        response_body = self.send_to_verified(currency).json()
        transaction_id = response_body["api_transaction_id"]
        return transaction_id

    def transaction_id_to_not_verified(self, currency):
        response_body = self.send_to_not_verified(currency).json()
        transaction_id = response_body["api_transaction_id"]
        return transaction_id

    def transaction_id_to_customer_defined_first_time(self, currency):
        response_body = self.send_to_customer_defined_first_time(currency).json()
        transaction_id = response_body["api_transaction_id"]
        global randomy
        print(f"{randomy}")
        print(transaction_id)
        return randomy

    def action_list_incoming(self):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        global randomy
        r = requests.post(self.link + "/api/v1/merchants/banksend_action_list",
                          headers=self.authorize(password, username),
                          json=self.check_fee_for_transaction_json(randomy))
        print(f"\n{r.status_code}")
        assert r.status_code == 200, "Action list response != 200"
        r_body = r.json()
        return r_body

    def action_list_to_verified(self, currency):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        r = requests.post(self.link + "/api/v1/merchants/banksend_action_list",
                          headers=self.authorize(password, username),
                          json=self.check_fee_for_transaction_json(self.transaction_id_to_verified(currency)))
        print(f"\n{r.status_code}")
        assert r.status_code == 200, "Action list response != 200"
        r_body = r.json()
        return r_body

    def action_list_to_not_verified(self, currency):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        r = requests.post(self.link + "/api/v1/merchants/banksend_action_list",
                          headers=self.authorize(password, username),
                          json=self.check_fee_for_transaction_json(self.transaction_id_to_not_verified(currency)))
        print(f"\n{r.status_code}")
        assert r.status_code == 200, "Action list response != 200"
        r_body = r.json()
        return r_body

    def action_list_to_customer_defined(self, currency):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        global randomy
        r = requests.post(self.link + "/api/v1/merchants/banksend_action_list",
                          headers=self.authorize(password, username),
                          json=self.check_fee_for_transaction_json(randomy))
        print(f"\n{r.status_code}")
        assert r.status_code == 200, "Action list response != 200"
        r_body = r.json()
        return r_body

    def fee_settings(self, currency):  # select which merchant fee we needed
        if currency == 'CAD':
            merchant_id = 5
        else:
            merchant_id = 6  # USD
        add_link = f"/api/v1/merchants/{merchant_id}/fee_settings"
        password = "12345678"
        username = "superadmin-test@banksend.com"
        response = requests.get(self.link + add_link, headers=self.authorize(password, username))
        response2_body = response.json()
        assert response.status_code == 200, "Fee settings request status !=200"
        return response2_body

    @staticmethod
    def output_fee_from_settings(fee_settings_for, typ, currency):
        # typ == OUTGOING , OUTGING Verified, OUTGING send to not verified, OUTGOING TO CUSTOMER DEFINED
        result = []
        for element in fee_settings_for:
            if element["type"] == f"{typ}" or element["type"] == "OUTGOING":
                if element["income"] == True and element["currency"] == f"{currency}":
                    result.append(element["amount"])
                elif element["income"] == False:
                    result.append(element["amount"])
        print(result)
        return result

    @staticmethod
    def output_fee_for_income_repeat(fee_settings_for, currency):
        result = []
        for element in fee_settings_for:
            if element["type"] == "INCOMING" or element["type"] == "INCOMING_BANK_ACCOUNT_BALANCE":
                if element["income"] == True and element["currency"] == f"{currency}" and \
                        element["transaction_count"] > 0:
                    result.append(element["amount"])
                elif element["income"] == False:
                    result.append(element["amount"])
        print(result)
        return result

    @staticmethod
    def output_fee_for_income_first_time(fee_settings_for, currency):
        result = []
        for element in fee_settings_for:
            if element["type"] == "INCOMING" or element["type"] == "INCOMING_BANK_ACCOUNT_CONNECTED":
                if element["income"] == True and element["currency"] == f"{currency}" and \
                        element["transaction_count"] < 1:
                    result.append(element["amount"])
                elif element["income"] is False:
                    result.append(element["amount"])
        print(result)
        return result

    @staticmethod
    def output_fee_for_to_customer_defined_first_time(fee_settings_for, currency):
        result = []
        for element in fee_settings_for:
            if element["type"] == "OUTGOING_CUSTOMER_DEFINED_BANK_ACCOUNT_CONNECTED" or element["type"] == "OUTGOING" \
                    or element["type"] == "OUTGOING_CUSTOMER_DEFINED" or element["type"] == \
                    "OUTGOING_CUSTOMER_DEFINED_SMS":
                if element["income"] == True and element["currency"] == f"{currency}" and \
                        element["transaction_count"] < 1:
                    result.append(element["amount"])
                elif element["income"] == False:
                    result.append(element["amount"])
        print(result)
        return result

    @staticmethod
    def output_fee_for_to_customer_defined_repeat(fee_settings_for, currency):
        result = []
        for element in fee_settings_for:
            if element["type"] == "OUTGOING" or element["type"] == "OUTGOING_CUSTOMER_DEFINED" or \
                    element["type"] == "OUTGOING_CUSTOMER_DEFINED_SMS":
                if element["income"] == True and element["currency"] == f"{currency}" and \
                        element["transaction_count"] > 0:
                    result.append(element["amount"])
                elif element["income"] == False:
                    result.append(element["amount"])
        print(result)
        return result

    randomy = 0

    @staticmethod
    def randome():
        global randomy
        randomy = random.random()
        return randomy

    def payment_from_json_repeat(self, currency):
        json = {
            "amount": 100,
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": "autotest",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "+380969245002",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def payment_from_json_first_time(self, currency):
        global randomy
        json = {
            "amount": 100,
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": f"{self.randome()}",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "+380969245002",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_customer_defined_json_repeat(self, currency):
        json = {
            "amount": 100,
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": "autotest",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "ylavro@simplepin.com",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "+380969245002",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "notification_type": "EMAIL",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_customer_defined_json_first_time(self, currency):
        json = {
            "amount": 100,
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": f"{self.randome()}",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "ylavro@simplepin.com",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "+380969245002",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "notification_type": "EMAIL",
            "params": [
                "string"
            ],
            "redirect_url": {
                "failed_url": "string",
                "success_url": "string"
            },
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_not_verified_json(self, currency):
        json = {
            "amount": 100,
            "bank_account": {
                "account_branch": "00012",
                "account_institution": "343",
                "account_number": "string",
                "account_routing": "string"
            },
            "country_code": "CA",
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": "autotest",
            "customer_profile": {
                "address_a": "string",
                "address_b": "string",
                "city": "string",
                "country": "string",
                "date_of_birth": "string",
                "email": "string",
                "first_name": "string",
                "id": 0,
                "last_name": "string",
                "phone": "+380969245002",
                "postal_code": "string",
                "province": "string",
                "sin": "string"
            },
            "locale": "NA",
            "params": [
                "string"
            ],
            "transaction_id": f"{self.randome()}"
        }
        return json

    def send_to_verified_json(self, currency):
        json = {
            "amount": 100,
            "currency_code": f"{currency}",
            "customer_fee_percent": 100,
            "customer_id": "autotest",
            "locale": "NA",
            "params": [
                "string"
            ],
            "transaction_id": f"{self.randome()}"
        }
        return json

    @staticmethod
    def check_fee_for_transaction_json(transaction_id):
        json = {"search_text": f"{transaction_id}",
                "entity_types": ["CUSTOMER_TRANSACTION", "CUSTOMER_TRANSACTION_FEE", "TRANSFER_FEE", "MERCHANT_FEE",
                                 "INCOME", "PROFIT"], "timezone": "Europe/Kiev"}
        return json

    @staticmethod
    def check_fee_for_transfer():
        global transfer_id
        json = {"transfer_id": f"{transfer_id}",
                "entity_types": ["TRANSFER_FEE"], "timezone": "Europe/Kiev"}
        return json

    def find_transaction(self, currency):
        global uuid
        global iid
        data = "?customer_transaction_uuid=" + uuid
        response = requests.get(self.link + "/api/v1/transactions" + data, headers=self.headers(currency))
        print(f"\n{response.status_code}")
        print(uuid)
        print(response.text)
        assert response.status_code == 200, "Transaction not found"
        iid = response.json()["id"]
        print(iid)
        return iid

    def settled_transaction(self):
        global iid
        password = "12345678"
        username = "superadmin-test@banksend.com"
        url = f"/api/v1/transactions/{iid}/settled"
        response = requests.post(self.link + url, headers=self.authorize(password, username))
        assert response.status_code == 200, "Transaction not settled"

    def initiate_transfer(self, currency):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        global merchant_id, transfer_id
        if currency == "CAD":
            merchant_id = 5
        else:
            merchant_id = 6
        response = requests.post(self.link +
                                 f"/api/v1/merchants/{merchant_id}/transfers/create?currency={currency}&type=INCOME&user_id=1",
                                 headers=self.authorize(password, username))
        print(response.text)
        print(response.json()["transfer_id"])
        transfer_id = response.json()["transfer_id"]
        assert response.status_code == 200, "Transfer not initiated"
        return transfer_id

    def initiate_transfer_with_zero_amount(self, currency):
        password = "12345678"
        username = "superadmin-test@banksend.com"
        global merchant_id, transfer_id
        if currency == "CAD":
            merchant_id = 5
        else:
            merchant_id = 6
        response = requests.post(
            self.link + f"/api/v1/merchants/{merchant_id}/transfers/create?currency={currency}&type=INCOME&user_id=1",
            headers=self.authorize(password, username))
        if response.status_code != 400:
            itertools.repeat(response, 1)
            print(response.json())
        elif response.status_code == 400:
            return True

    def action_list_for_transfer(self):
        global transfer_id
        password = "12345678"
        username = "superadmin-test@banksend.com"
        r = requests.post(self.link + "/api/v1/merchants/banksend_action_list",
                          headers=self.authorize(password, username),
                          json=self.check_fee_for_transfer())
        print(f"\n{r.status_code}")
        assert r.status_code == 200, "Action list response != 200"
        r_body = r.json()
        return r_body

    @staticmethod
    def output_fee_for_transfer(fee_settings_for, currency):
        result = []
        for element in fee_settings_for:
            if element["type"] == "TRANSFER" or element["type"] == "TRANSFER_INCOME":
                if element["income"] is True and element["currency"] == f"{currency}":
                    result.append(element["amount"])
                elif element["income"] is False:
                    result.append(element["amount"])
        print(result)
        return result

    def calculation_income_transfer_fees(self, fee_settings, currency, amount):
        sum = 0
        result = []
        for elem in fee_settings:
            if (elem["type"] == "TRANSFER" or elem["type"] == "TRANSFER_INCOME") and elem["income"] is True and \
                    elem["currency"] == f"{currency}":
                if elem["amount_type"] == "FIXED":
                    sum += elem["amount"]
                    result.append(elem["amount"])
                else:
                    sum += (amount * elem["amount"]) / 100
                    result.append((amount * elem["amount"]) / 100)
        return [sum, result]

        # Massive of types - with Oleksii

    def calculation_expense_transfer_fees(self, fee_setting, currency, amount, result_array):
        sum = 0
        for elem in fee_setting:
            if (elem["type"] == "TRANSFER" or elem["type"] == "TRANSFER_INCOME") and elem["income"] is False:
                if elem["amount_type"] == "FIXED":
                    if elem["currency"] == currency:
                        sum += elem["amount"]
                        result_array.append(elem["amount"])
                    else:
                        if currency == "USD":
                            sum += elem["amount"] / 1.31
                            result_array.append(elem["amount"] / 1.31)
                        else:
                            sum += elem["amount"] * 1.31
                            result_array.appen(elem["amount"] * 1.31)
                else:
                    sum += (amount * elem["amount"]) / 100
                    result_array.append(round((amount * elem["amount"]) / 100, 5))
        return [sum, result_array]


class ReturnBasePage(BasePage):
    def return_base_page(self):
        pass

    def chose_radiobutton(self):
        self.browser.find_element(*PaymentFormLocators.RADIO_BUTTON).click()

    def chose_radiobutton_first_time(self, currency):
        self.browser.find_element(*PaymentFormLocators.RADIO_BUTTON).click()
        if currency == "CAD":
            self.browser.find_element(*PaymentFormLocators.AGREE_AND_SIGN_BUTTON).click()

    def chose_radiobutton_first_time_customer_defined(self):
        self.browser.find_element(*PaymentFormLocators.RADIO_BUTTON).click()

    def chose_accept_button(self):
        self.browser.find_element(*PaymentFormLocators.ACCEPT_BUTTON).click()

    def chose_accept_button_for_income(self):
        self.browser.find_element(*PaymentFormLocators.ACCEPT_BUTTON_FOR_INCOME).click()

    def should_be_bank_header(self):
        self.is_element_present(*PaymentFormLocators.BANK_HEADER)

    def click_continue(self):
        self.browser.find_element(*PaymentFormLocators.CONTINUE_BUTTON).click()

    def select_bank_account(self):
        self.browser.find_element(*PaymentFormLocators.SELECT_BANK).click()

    def enter_username(self):
        self.browser.find_element(*PaymentFormLocators.USERNAME).send_keys("user_good")

    def enter_password(self):
        self.browser.find_element(*PaymentFormLocators.PASSWORD).send_keys("pass_good")

    def click_sumbit_button(self):
        self.browser.find_element(*PaymentFormLocators.SUBMIT_BUTTON).click()

    def should_be_card_header(self):
        self.is_element_present(*PaymentFormLocators.CARD_HEADER)

    def click_sign_button(self):
        self.browser.find_element(*PaymentFormLocators.AGREE_AND_SIGN_BUTTON).click()

    def should_be_continue_button(self):
        assert self.is_element_present(*PaymentFormLocators.CONTINUE_BUTTON), "Continue button not present on the page"

    def iframe(self):
        self.browser.find_element(*PaymentFormLocators.IFRAME)

    def pressing_tab(self):
        self.browser.find_element(*PaymentFormLocators.CONTINUE_BUTTON).send_keys(Keys.TAB)

    def pressing_enter(self):
        self.browser.find_element(*PaymentFormLocators.CONTINUE_BUTTON).send_keys(Keys.ENTER)

    def should_be_frame(self):
        assert self.is_element_present(*PaymentFormLocators.IFRAME), "Iframe not present on page"

    def should_be_policy(self):
        assert self.is_element_present(*PaymentFormLocators.POLICY), "Policy is not present"

    def frames(self):
        self.browser.find_elements(*PaymentFormLocators.FRAMES)

    def should_be_first_frame(self):
        self.is_element_present(*PaymentFormLocators.FIRST_FRAME)

    def first_frame(self):
        self.browser.find_element(*PaymentFormLocators.FIRST_FRAME)

    def second_frame(self):
        self.browser.find_element(*PaymentFormLocators.SECOND_FRAME)

    def should_be_successfully_message(self):
        self.is_element_present(*PaymentFormLocators.SUCCESSFULLY_MESSAGE)

    def enter_username_email(self):
        username = "ylavro@simplepin.com"
        self.browser.find_element(*PaymentFormLocators.EMAIL_USERNAME_FIELD).send_keys(username)

    def enter_password_email(self):
        password = "Lgaf45#09!"
        self.browser.find_element(*PaymentFormLocators.EMAIL_PASSWORD_FIELD).send_keys(password)

    def click_submit_email(self):
        self.browser.find_element(*PaymentFormLocators.EMAIL_SUBMIT_BUTTON).click()

    def found_unread_email(self):
        first_email = self.browser.find_element(*PaymentFormLocators.MAIL_LAST_UNREAD_MESSAGE)
        if self.is_not_element_present(*PaymentFormLocators.WINDOW_IN_EMAIL):
            first_email.click()
        elif self.browser.find_element(*PaymentFormLocators.WINDOW_IN_EMAIL).is_displayed():
            self.browser.find_element(*PaymentFormLocators.YES_BUTTON).click() and first_email.click()
        else:
            first_email.click()

    #   elements = self.browser.find_elements(*PaymentFormLocators.MESSAGES)

    #       if first_email.get_attribute("class") == "ZmRowDoubleHeader Unread":
    #           first_email.click()
    #       else:
    #           for element in elements:
    #               if element.get_attribute("class") == "ZmRowDoubleHeader Unread":
    #                   element.click()
    #               else:
    #                   element.send_keys(Keys.F5)

    def should_be_elements_in_email(self, currency):
        assert self.is_element_present(*PaymentFormLocators.COMPANY_LOGO_IN_EMAIL) is True, \
            "Company logo in mail not available"
        assert self.browser.find_element(*PaymentFormLocators.AMOUNT_IN_EMAIL).text == f"$100.00 {currency}", \
            "Wrong amount displayed or currency"
        assert self.browser.find_element(*PaymentFormLocators.POWERED_BY).text == "Powered by", \
            "Wrong text for POWERED BY"
        assert self.is_element_present(*PaymentFormLocators.BANKSEND_LOGO) is True, \
            "BankSend LOGO IS NOT present in mail"
        assert self.is_element_present(*PaymentFormLocators.ACCEPT_BUTTON_EMAIL) is True, "Accept button not present"
        accept_button_link = self.browser.find_element(*PaymentFormLocators.ACCEPT_BUTTON_EMAIL).get_attribute("href")
        assert "outgoing_form" in accept_button_link, "In url not displayed Outgoing_form/"

    def should_be_transaction_id_in_email(self):
        global randomy
        transaction_id = self.browser.find_element(*PaymentFormLocators.TRANSACTION_ID_IN_EMAIL).text
        assert transaction_id == f"Payout #{randomy}", "Wrong transaction id in email"

    def click_accept_button_in_email(self):
        self.browser.find_element(*PaymentFormLocators.ACCEPT_BUTTON_EMAIL).click()

    #        alert = self.browser.switch_to.alert
    #        alert.accept()
    #        print(alert.text)

    def should_be_elements_on_activate_page(self, currency):
        print(self.browser.find_element(*PaymentFormLocators.TRANSACTION_AMOUNT_IN_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.TRANSACTION_AMOUNT_IN_ACTIVATE_PAGE).text == "$100.00", \
            "Wrong amount displayed on activate page"
        print(self.browser.find_element(*PaymentFormLocators.TRANSACTION_CURRENCY_IN_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.TRANSACTION_CURRENCY_IN_ACTIVATE_PAGE).text == \
               f"{currency}", "Wrong currency dislayed in ACTIVATE PAGE"
        print(self.browser.find_element(*PaymentFormLocators.FROM_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.FROM_ON_ACTIVATE_PAGE).text == "From:", \
            "From paragraph is not present on ACTIVATE PAGE"
        print(self.browser.find_element(*PaymentFormLocators.TO_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.TO_ON_ACTIVATE_PAGE).text == "To :", \
            "To paragraph is not present on ACTIVATE PAGE"
        print(self.browser.find_element(*PaymentFormLocators.DESCRIPTIONS_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.DESCRIPTIONS_ON_ACTIVATE_PAGE).text == \
               "To activate your account, please enter a 6 digit code which we sent to the following phone number" \
               " +380XX XXX-XX02", "Something wrong with desctiption on ACTIVATE PAGE"
        print(self.browser.find_element(*PaymentFormLocators.POWERED_BY_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.POWERED_BY_ON_ACTIVATE_PAGE).text == "Powered by", \
            "text Powered by is on present on ACTIVATE PAGE"

    def should_be_default_language_and_additional(self):
        print(self.browser.find_element(*PaymentFormLocators.DEFAULT_LANGUAGE_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.DEFAULT_LANGUAGE_ON_ACTIVATE_PAGE).text == "English", \
            "Wrong default language"
        self.browser.find_element(*PaymentFormLocators.DEFAULT_LANGUAGE_ON_ACTIVATE_PAGE).click()
        print(self.browser.find_element(*PaymentFormLocators.FIRST_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text)
        #    assert self.browser.find_element(*PaymentFormLocators.FIRST_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text == \
        #           "English", "Wrong first language in drop-down"
        print(self.browser.find_element(*PaymentFormLocators.SECOND_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.SECOND_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text == \
               "Français", "Second language is not french"
        print(self.browser.find_element(*PaymentFormLocators.THIRD_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text)
        assert self.browser.find_element(*PaymentFormLocators.THIRD_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE).text == \
               "Español", "Third language is not spain"

    def should_be_logos_on_activate_page(self):
        self.is_element_present(*PaymentFormLocators.COMPANY_LOGO_IN_ACTIVATE_PAGE)
        self.is_element_present(*PaymentFormLocators.BANKSEND_LOGO_ON_ACTIVATE_PAGE)

    def refresh_page(self):
        print(self.browser.current_url)
        self.browser.get(self.browser.current_url)

    def go_to_sms_form(self):
        self.browser.get(self.browser.find_element(*PaymentFormLocators.ACCEPT_BUTTON_EMAIL).get_attribute("href"))

    def scroll_the_page(self):
        self.browser.execute_script("window.scrollBy(0, 200);")

    def scroll_iframe(self):
        iframe = self.browser.find_element(*PaymentFormLocators.FIRST_FRAME)
        self.browser.execute_script("window.scrollBy(0, 200);", iframe)

    def scroll_second_iframe(self):
        iframe = self.browser.find_element(*PaymentFormLocators.SECOND_FRAME)
        self.browser.execute_script("window.scrollBy(0, 200);", iframe)

    def scroll_to_view_continue_button(self):
        continue_button = self.browser.find_element(*PaymentFormLocators.CONTINUE_BUTTON)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", continue_button)

    def switch_to_iframe_email(self):
        iframe = self.browser.find_element(*PaymentFormLocators.IFRAME_EMAIL)
        self.browser.switch_to.frame(iframe)

    def select_dropdown_email(self):
        select = Select(self.browser.find_element(*PaymentFormLocators.DROP_DOWN_EMAIL))
        select.select_by_value("standard")

    @staticmethod
    def get_sms_pin():
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=3)
        cursor = conn.cursor()
        cursor.execute("select body from notification where receiver = '+380969245002' "
                       " order by created_time desc limit 1 ")
        records = cursor.fetchall()
        lst = list(records[0])
        result = lst[0].split(" ")[2]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    def input_sms_code(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        sms_field = self.browser.find_element(*PaymentFormLocators.INPUT_SMS_CODE)
        sms_field.clear()
        sms_field.send_keys(self.get_sms_pin())

    def click_activate_button(self):
        self.browser.find_element(*PaymentFormLocators.ACTIVATE_BUTTON_VIA_EMAIL).click()

    def switch_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def switch_window_second(self):
        new_window = self.browser.window_handles[2]
        self.browser.switch_to.window(new_window)

    def check_merchant_balance_in_ui(self):
        print(self.browser.find_element(*CustomersPageLocators.BALANCE_MERCHANT).text)
        self.browser.find_element(*CustomersPageLocators.BALANCE_MERCHANT)

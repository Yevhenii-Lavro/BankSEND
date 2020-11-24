import requests
from selenium.webdriver.common.by import By
from .locators import CustomerProfilePageLocators
from .base_page import BasePage
import psycopg2
import pytest

global customer_id
customer_id = 2


class CustomerProfilePage(BasePage):

    def should_be_customer_profile_page(self):
        assert self.browser.find_element(*CustomerProfilePageLocators.PAGE_NAME).text == "Customer details", \
            "It's not a customer details page"

    def title_of_customer_profile_page(self):
        print(self.browser.title)
        assert self.browser.title == f"Customer {customer_id} | Canada Autotest Company | BankSEND®", \
            "Wrong title for customer profile page"

    def balance_is_present(self):
        assert self.is_element_present(*CustomerProfilePageLocators.BALANCE_WINDOW) is True, \
            "Balance is not present for merchant on customer details"

    def should_be_present_customer_block_and_his_details(self):
        assert self.is_element_present(*CustomerProfilePageLocators.BLOCK_WITH_DETAILS) is True, \
            "Block with details not present"
        assert self.is_element_present(*CustomerProfilePageLocators.NAME) is True, "Name is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.NAME).text == "Name:", "Missing title for  a name"
        assert self.is_element_present(*CustomerProfilePageLocators.REGISTERED) is True, "Registered is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.REGISTERED).text == "Registered:", \
            "Missing title for registered"
        assert self.is_element_present(*CustomerProfilePageLocators.DATE_OF_BIRTH) is True, \
            "Date of birth is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.DATE_OF_BIRTH).text == "Date of birth:", \
            "Missing title for a 'Date of birth'"
        assert self.is_element_present(*CustomerProfilePageLocators.ADDRESS) is True, "Address is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.ADDRESS).text == "Address:", \
            "Missing title for a Address"
        assert self.is_element_present(*CustomerProfilePageLocators.PHONE_NUMBER) is True, "Phone number is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.PHONE_NUMBER).text == "Phone number:", \
            "Missing title for phone number"
        assert self.is_element_present(*CustomerProfilePageLocators.EMAIL) is True, "Email is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.EMAIL).text == "Email:", "Wrong title for Email"
        assert self.is_element_present(*CustomerProfilePageLocators.CUSTOMER_BLOCK_BUTTON) is True, \
            "Block button for customer profile is not present"

    def should_be_transactions_list_and_his_attributes(self):
        assert self.is_element_present(*CustomerProfilePageLocators.TRANSACTION_LIST) is True, \
            "Transaction list is not present"
        assert self.is_element_present(*CustomerProfilePageLocators.SEARCH) is True, "Search field is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.SEARCH).get_attribute("placeholder") == \
               "Type text", "Wrong placeholed for search field"
        assert self.is_element_present(*CustomerProfilePageLocators.FILTER_FROM) is True, "From filter field is present"
        assert self.browser.find_element(*CustomerProfilePageLocators.FILTER_FROM).get_attribute("placeholder") == \
               "From", "Wrong placeholder for filter FROM field"
        assert self.is_element_present(*CustomerProfilePageLocators.FILTER_TO) is True, "Filter to field is present"
        assert self.browser.find_element(*CustomerProfilePageLocators.FILTER_TO).get_attribute("placeholder") == "To", \
            "Wrong placeholder for filter TO field"
        assert self.is_element_present(*CustomerProfilePageLocators.SHOW_FEES) is True, \
            "Show fees check box is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.SHOW_FEES).text == "Show details", \
            "Wrong text for show fees check box"
        assert self.is_element_present(*CustomerProfilePageLocators.DROP_DOWN_SHOW_ENTRIES) is True, \
            "Show entries drop down is not present"
        assert self.is_element_present(*CustomerProfilePageLocators.DATE_TIME) is True, "Column date time is present"
        assert self.browser.find_element(*CustomerProfilePageLocators.DATE_TIME).text == "DATE/TIME", \
            "Wrong name of Date/Time column"
        assert self.is_element_present(*CustomerProfilePageLocators.TRANSACTION_ID) is True, \
            "Transaction ID column is present"
        assert self.browser.find_element(*CustomerProfilePageLocators.TRANSACTION_ID).text == "TRANSACTION ID", \
            "Wrong name of column TRAnsaction ID"
        assert self.is_element_present(*CustomerProfilePageLocators.DEPOSIT) is True, "Column Deposit is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.DEPOSIT).text == "TRANSFER ID", \
            "Wrong name of column Deposit"
        assert self.is_element_present(*CustomerProfilePageLocators.DESCRIPTION) is True, \
            "Column DESCRIPTION is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.DESCRIPTION).text == "DESCRIPTION", \
            "Wrong name for Description column"
        assert self.is_element_present(*CustomerProfilePageLocators.AMOUNT) is True, "Amount column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.AMOUNT).text == "AMOUNT", \
            "Wrong column name for AMOUNT"
        assert self.is_element_present(*CustomerProfilePageLocators.CURRENCY) is True, "Currency column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.CURRENCY).text == "CURRENCY", \
            "Wrong name for CURRENCY column"
        assert self.is_element_present(*CustomerProfilePageLocators.STATUS) is True, "Status column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.STATUS).text == "STATUS", \
            "Wrong name for status column"

    def should_be_table_with_transactions_summary(self):
        assert self.is_element_present(*CustomerProfilePageLocators.SUMMARY_AND_PAYMENT_METHODS_TABLE) is True, \
            "Table with transactions results is not present"
        assert self.is_element_present(*CustomerProfilePageLocators.SUMMARY_BUTTON) is True, \
            "Summary button is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.SUMMARY_BUTTON).text == "Summary", \
            "Wrong name of button Summary"
        assert self.is_element_present(*CustomerProfilePageLocators.PAYMENT_METHOD_BUTTON) is True, \
            "Payment method button is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.PAYMENT_METHOD_BUTTON).text == "Payment methods", \
            "Wrong name of payment methods button"
        assert self.browser.find_element(*CustomerProfilePageLocators.INCOMING).text == "INCOMING", \
            "Wrong text for INCOMING transaction in table "
        assert self.browser.find_element(*CustomerProfilePageLocators.ACTIONS_COLUMN).text == "ACTIONS", \
            "Wrong name of actions column or column not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.PREPARED_COLUMN).text == "PREPARED", \
            "Column Prepared is not present, or wrong name of column"
        assert self.browser.find_element(*CustomerProfilePageLocators.PENDING_COLUMN).text == "PENDING", \
            "PENDING column is not present, or wrong name for the column"
        assert self.browser.find_element(*CustomerProfilePageLocators.SETTLED_COLUMN).text == "SETTLED", \
            "SETTLED COLUMN IS NOT PRESENT, or wrong name of column"
        assert self.browser.find_element(*CustomerProfilePageLocators.TOTAL_COLUMN).text == "TOTAL", \
            "Wrong name of TOTAL column or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.CURRENCY_COLUMN).text == "CURRENCY", \
            "Wrong name of CURRENCY column, or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.OUTGOING_CUSTOMER_DEFINED).text == \
               "OUTGOING_CUSTOMER_DEFINED", "Wrong text for CUSTOMER DEFINED line or line is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.OUTGOING_NOT_VERIFIED).text == \
               "OUTGOING_NOT_VERIFIED", "Wrong name for line OUTGOING NOT VERIFIED, or Line is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.OUTGOING_VERIFIED).text == "OUTGOING_VERIFIED", \
            "Wrong name for line OUTGOING VERIFIED, or line not present"

    def should_be_table_with_payment_methods(self):
        assert self.browser.find_element(*CustomerProfilePageLocators.BANK).text == "BANK", \
            "Wrong name for column BANK or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.ACCOUNT_NAME).text == "ACCOUNT NAME", \
            "Wrong name for a column ACCOUNT NAME, or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.ENDS_WITH).text == "ENDS WITH", \
            "Wrong name for column 'ENDS WITH', or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.REGISTERED_COLUMN_IN_PAYMENT_TAB).text == \
               "REGISTERED", "Wrong name of column REGISTERED, or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.PRE_AUTORIZED).text == "PRE-AUTHORIZED", \
            "Wrong name of column PRE-AUTHORIZED, or column not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.VERIFIED_COLUMN).text == "VERIFIED", \
            "Wrong name for VERIFIED Column, or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.LAST_BALANCE).text == "LAST BALANCE", \
            "Wrong name for LAST BALANCE, or column is not present"
        assert self.browser.find_element(*CustomerProfilePageLocators.ACTIONS_COLUMN_IN_PAYMENT_TAB).text == "ACTIONS", \
            "Wrong name of ACTIONS column, or column is not present"

    def changing_tab_summary_or_payment_method(self):
        if self.browser.find_element(*CustomerProfilePageLocators.SUMMARY_BUTTON).get_attribute(
                "class") == "nav-link active":
            self.browser.find_element(*CustomerProfilePageLocators.PAYMENT_METHOD_BUTTON).click()
        else:
            self.browser.find_element(*CustomerProfilePageLocators.SUMMARY_BUTTON).click()

    def block_the_customer(self):
        block = self.browser.find_element(*CustomerProfilePageLocators.CUSTOMER_BLOCK_BUTTON)
        block.click()

    @staticmethod
    def status_of_customer():
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=3)
        cursor = conn.cursor()
        cursor.execute("select state from customer where api_customer_id = 'autotest' and merchant_id = '5'")
        records = cursor.fetchall()
        lst = list(records[0])
        result = lst[0].split(" ")[0]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    def check_active_status(self):
        assert self.status_of_customer() == "ACTIVE", "Customer is blocked before started test case"

    def check_blocked_status(self):
        assert self.status_of_customer() == "BLOCKED", "Blocking - doesn't work in UI"

    @staticmethod
    def give_a_block_status_of_customer_incoming():
        global customer_id
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=5)
        cursor = conn.cursor()
        cursor.execute(f"select state from customer_transaction_restriction where "
                       f"customer_id = '{customer_id}' and type = 'INCOMING' order by created_time desc limit 1")
        records = cursor.fetchall()
        print(list(records[0]))
        lst = list(records[0])
        result = lst[0].split(" ")[0]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    @staticmethod
    def give_a_block_status_of_customer_outgoing_verified():
        global customer_id
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=5)
        cursor = conn.cursor()
        cursor.execute(f"select state from customer_transaction_restriction "
                       f"where customer_id = '{customer_id}' and type = 'OUTGOING_VERIFIED' order by created_time desc limit 1")
        records = cursor.fetchall()
        print(list(records[0]))
        lst = list(records[0])
        result = lst[0].split(" ")[0]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    @staticmethod
    def give_a_block_status_of_customer_outgoing_not_verified():
        global customer_id
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=5)
        cursor = conn.cursor()
        cursor.execute(f"select state from customer_transaction_restriction "
                       f"where customer_id = '{customer_id}' and type = 'OUTGOING_NOT_VERIFIED' order by created_time desc limit 1")
        records = cursor.fetchall()
        lst = list(records[0])
        result = lst[0].split(" ")[0]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    @staticmethod
    def give_a_block_status_of_customer_outgoing_to_customer_defined():
        global customer_id
        print("\nDB connection")
        conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=5)
        cursor = conn.cursor()
        cursor.execute(f"select state from customer_transaction_restriction "
                       f"where customer_id = '{customer_id}' and"
                       " type = 'OUTGOING_CUSTOMER_DEFINED' order by created_time desc limit 1")
        records = cursor.fetchall()
        lst = list(records[0])
        result = lst[0].split(" ")[0]
        print(result)
        conn.close()
        print("\nConnection DB closed")
        return str(result)

    def check_active_status_for_incoming(self):
        assert self.give_a_block_status_of_customer_incoming() == "UNBLOCK", \
            "Status not UNBLOCK for INCOMING after testing"

    def check_blocked_status_for_incoming(self):
        assert self.give_a_block_status_of_customer_incoming() == "BLOCK", \
            "Status not BLOCKED FOR INCOMING, button doesn't work"

    def check_active_status_for_outgoing_verified(self):
        assert self.give_a_block_status_of_customer_outgoing_verified() == "UNBLOCK", \
            "Status not UNBLOCK for OUTGOING VERIFIED after testing"

    def check_blocked_status_for_outgoing_verified(self):
        assert self.give_a_block_status_of_customer_outgoing_verified() == "BLOCK", \
            "Wrong state of transaction for OUTGOING VERIFIED, button block doesn't work"

    def check_active_status_for_outgoing_not_verified(self):
        assert self.give_a_block_status_of_customer_outgoing_not_verified() == "UNBLOCK", \
            "State not UNBLOCK for OUTGOING NOT VERIFIED after testing"

    def check_blocked_status_for_outgoing_not_verified(self):
        assert self.give_a_block_status_of_customer_outgoing_not_verified() == "BLOCK", \
            "Wrong state of transaction for OUTGOING NOT VERIFIED, button blocked in UI doesn't work"

    def check_active_status_for_outgoing_customer_defined(self):
        assert self.give_a_block_status_of_customer_outgoing_to_customer_defined() == "UNBLOCK", \
            "Status not UNBLOCK for CUSTOMER DEFINED after testing"

    def check_blocked_status_for_outgoing_customer_defined(self):
        assert self.give_a_block_status_of_customer_outgoing_to_customer_defined() == "BLOCK", \
            "State not blocked for CUSTOMER DEFINED. Button in UI doesn't work"

    def block_the_incoming_transaction_for_customer(self):
        self.browser.find_element(*CustomerProfilePageLocators.BLOCK_BUTTON_FOR_INCOMING).click()

    def block_the_outgoing_verified_transaction(self):
        self.browser.find_element(*CustomerProfilePageLocators.BLOCK_BUTTON_FOR_VERIFIED).click()

    def block_the_outgoing_not_verified_transaction(self):
        self.browser.find_element(*CustomerProfilePageLocators.BLOCK_BUTTON_FOR_NOT_VERIFIED).click()

    def block_the_outgoing_to_customer_defined_transaction(self):
        self.browser.find_element(*CustomerProfilePageLocators.BLOCK_BUTTON_FOR_CUSTOMER_DEFINED).click()

    @staticmethod
    def authorize():
        _s = requests.session()
        data = {"password": "12345678", "username": "owner-test-ca-autotest@banksend.com"}
        response = _s.post("https://test.banksend.com/api/v1/auth/sign_in", json=data)
        print(f"\n{response.status_code}")
        assert response.status_code == 200, "Unable to log in"
        if response.status_code != 200:
            raise Exception("Unable to authorize using given credentials")
        session_token = response.headers.get("Authorization")
        new_headers = {"Authorization": f"Bearer {session_token}"}
        return new_headers

    def find_a_bank_accounts(self):
        global customer_id
        response = requests.get(f"https://test.banksend.com/api/v1/customers/{customer_id}/bank_accounts",
                                headers=self.authorize())
        assert response.status_code == 200, "Bank accounts not founded - wrong request"
        return response.json()

    def find_verified_bank_id(self):
        result = []
        for elem in self.find_a_bank_accounts():
            if elem['verified'] is True:
                result.append(elem['id'])
        return result[0]

    #   GET_BALANCE_BUTTON = (By.CSS_SELECTOR, f"#getBalanceButton_{find_verified_bank_id()}")

    def balance_button_click(self):
        print(self.browser.find_element_by_css_selector(f"#getBalanceButton_{self.find_verified_bank_id()}")
              .get_attribute("id"))
        self.browser.find_element_by_css_selector(f"#getBalanceButton_{self.find_verified_bank_id()}").click()

    global result

    def check_count_of_get_balance(self):
        global conn, result
        try:
            print("\nDB connection")
            conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                    password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=3)
            cursor = conn.cursor()
            cursor.execute(f"select count(*) from bank_account_balance "
                           f"where bank_account_id ='{self.find_verified_bank_id()}'")
            records = cursor.fetchall()
            lst = list(records[0])
            result = []
            for elem in lst:
                result.append(elem)
            return result[0]
        finally:
            conn.close()
            print("\nConnection DB closed")

    def check_second_time_count_of_get_balance(self):
        global conn, result
        try:
            print("\nDB connection")
            conn = psycopg2.connect(dbname='simpleeftha_testdb', user='simpleeft',
                                    password='qwerty123', host='192.168.160.250', port='5432', connect_timeout=3)
            cursor = conn.cursor()
            cursor.execute(f"select count(*) from bank_account_balance "
                           f"where bank_account_id ='{self.find_verified_bank_id()}'")
            records = cursor.fetchall()
            lst = list(records[0])
            result2 = []
            for elem in lst:
                result2.append(elem)
            assert result[0] + 1 == result2[0], "Get balance button doesn't work correctly"
            print(result, result[0] + 1, result2)
        finally:
            conn.close()
            print("\nConnection DB closed")

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from .locators import CustomersPageLocators
from .base_page import BasePage
import datetime


class CustomerPage(BasePage):

    def should_be_customer_menu_button(self):
        self.is_element_present(*CustomersPageLocators.MENU_BUTTON)

    def go_to_customer_page(self):
        self.browser.find_element(*CustomersPageLocators.MENU_BUTTON).click()

    def should_be_customer_page(self):
        self.is_element_present(*CustomersPageLocators.PAGE_NAME)
        print(self.browser.find_element(*CustomersPageLocators.PAGE_NAME).text)
        assert self.browser.find_element(
            *CustomersPageLocators.PAGE_NAME).text == "Customers A list of all your customers and their processed " \
                                                      "transactions", \
            "There is not a page 'Customers', may be wrong locator for redirect"

    def should_be_id_column(self):
        self.is_element_present(*CustomersPageLocators.ID_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.ID_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.ID_COLUMN).text == "ID", "Column ID doesn't found," \
                                                                                         " or had another text"

    def should_be_name_column(self):
        self.is_element_present(*CustomersPageLocators.NAME_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.NAME_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.NAME_COLUMN).text == "NAME", "Column NAME doesn't " \
                                                                                             "found," \
                                                                                             " or had another text"

    def should_be_registered_column(self):
        self.is_element_present(*CustomersPageLocators.REGISTERED_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.REGISTERED_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.REGISTERED_COLUMN).text == "REGISTERED", "Column " \
                                                                                                         "REGISTERED " \
                                                                                                         "doesn't " \
                                                                                                         "found, " \
                                                                                                         "or had " \
                                                                                                         "another text "

    def should_be_last_transaction_column(self):
        self.is_element_present(*CustomersPageLocators.LAST_TRANSACTION_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.LAST_TRANSACTION_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.LAST_TRANSACTION_COLUMN).text == "LAST TRANSACTION", \
            "Column 'LAST TRANSACTION' doesn't found"

    def should_be_merchant_column(self):
        self.is_element_present(*CustomersPageLocators.MERCHANT_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.MERCHANT_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.MERCHANT_COLUMN).text == "MERCHANT", \
            "Merchant column doesn't found"

    def should_be_in_column(self):
        self.is_element_present(*CustomersPageLocators.IN_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.IN_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.IN_COLUMN).text == "IN ($)", "IN column doesn't found"

    def should_be_in_trx_column(self):
        self.is_element_present(*CustomersPageLocators.IN_TRX_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.IN_TRX_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.IN_TRX_COLUMN).text == "IN (TRX.)", \
            "IN TRX column doesn't found"

    def should_be_out_v_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_V_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_V_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_V_COLUMN).text == "OUT. V ($)", \
            "OUT V column doesn't found"

    def should_be_out_v_trx_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_V_TRX_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_V_TRX_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_V_TRX_COLUMN).text == "OUT V(TRX.)", \
            "OUT V TRX Column not present"

    def should_be_out_nv_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_NV_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_NV_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_NV_COLUMN).text == "OUT. NV ($)", \
            "OUT NV column not present"

    def should_be_out_nv_trx_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_NV_TRX_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_NV_TRX_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_NV_TRX_COLUMN).text == "OUT NV(TRX.)", \
            "OUT NV TRX column not present"

    def should_be_out_cd_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_CD_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_CD_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_CD_COLUMN).text == "OUT. CD ($)", \
            "Column OUT CD is not present"

    def should_be_out_cd_trx_column(self):
        self.is_element_present(*CustomersPageLocators.OUT_CD_TRX_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.OUT_CD_TRX_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.OUT_CD_TRX_COLUMN).text == "OUT CD(TRX.)", \
            "Column OUT CD TRX is not present"

    def should_be_currency_column(self):
        self.is_element_present(*CustomersPageLocators.CURRENCY_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.CURRENCY_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.CURRENCY_COLUMN).text == "CURRENCY", \
            "Currency column is not present"

    def should_be_status_column(self):
        self.is_element_present(*CustomersPageLocators.STATUS_COLUMN)
        print(self.browser.find_element(*CustomersPageLocators.STATUS_COLUMN).text)
        assert self.browser.find_element(*CustomersPageLocators.STATUS_COLUMN).text == "STATUS", \
            "STATUS COLUMN NOT PRESENT"

    def select_registered_filter(self):
        select = Select(self.browser.find_element(*CustomersPageLocators.FILTER_BY))
        select.select_by_visible_text("Registered")
        assert self.is_element_present(*CustomersPageLocators.FROM) is True, "From field is not present"
        assert self.is_element_present(*CustomersPageLocators.TO) is True, "TO field is not present"
        assert self.browser.find_element(*CustomersPageLocators.FROM).get_attribute("placeholder") == "From", \
            "Wrong placeholder for FROM field"
        assert self.browser.find_element(*CustomersPageLocators.TO).get_attribute("placeholder") == "To", \
            "Wrong placeholder for 'TO' field"

    def select_last_transaction_filter(self):
        select = Select(self.browser.find_element(*CustomersPageLocators.FILTER_BY))
        select.select_by_visible_text("Last Transaction")
        self.is_element_present(*CustomersPageLocators.FROM)
        self.is_element_present(*CustomersPageLocators.TO)
        assert self.browser.find_element(*CustomersPageLocators.FROM).get_attribute("placeholder") == "From", \
            "Wrong placeholder for FROM field"
        assert self.browser.find_element(*CustomersPageLocators.TO).get_attribute("placeholder") == "To", \
            "Wrong placeholder for 'TO' field"

    def enter_date_from(self):
        filter_from = self.browser.find_element(*CustomersPageLocators.FROM)
        ActionChains(self.browser).double_click(filter_from)
        filter_from.send_keys("2020-10-18")
        assert filter_from.get_attribute("value") == "2020-10-18", "Data not entering in to date FROM"

    def enter_date_to(self):
        filter_to = self.browser.find_element(*CustomersPageLocators.TO)
        ActionChains(self.browser).double_click(filter_to)
        filter_to.send_keys("2020-10-18")
        assert filter_to.get_attribute("value") == "2020-10-18", "Data not entering in to date TO"

    def click_reset_button(self):
        self.browser.find_element(*CustomersPageLocators.RESET_BUTTON).click()
        assert self.is_not_element_present(*CustomersPageLocators.FROM) is True, "'Filter From' not Reseted"
        assert self.is_not_element_present(*CustomersPageLocators.TO) is True, "'Filter To' not Reseted"

    def show_list_dropdown(self):
        elements = self.browser.find_elements(*CustomersPageLocators.PAGES_IN_DROPDOWN)
        result = []
        for element in elements:
            result.append(element.text)
        print(result)
        result2 = ['5', '8', '20', '50', '100']
        print(result2)
        assert all(elem in result for elem in result2), "Show entries drop down is correct"

    def should_be_balance_for_merchant(self):
        assert self.is_element_present(*CustomersPageLocators.BALANCE_MERCHANT) is True,\
            "Balance for merchant isn't showing"

    def not_displayed_merchant_column(self):
        merchant_column = self.browser.find_element(*CustomersPageLocators.MERCHANT_COLUMN)
        print(merchant_column.text)
        assert merchant_column.text != "MERCHANT", "MERCHANT column is displayed for merchant"

    def should_be_transfer_button(self):
        assert self.is_element_present(*CustomersPageLocators.TRANSFER_BUTTON) is True, \
            "Transfer button is not available"

    def should_be_search_field(self):
        assert self.is_element_present(*CustomersPageLocators.SEARCH) is True, "Search field is not present"

    def enter_text_in_search_field(self):
        search = self.browser.find_element(*CustomersPageLocators.SEARCH)
        search.send_keys(f"{str(datetime.datetime.today().date())}")

    def should_be_customer_profile_link(self):
        assert self.is_element_present(*CustomersPageLocators.CUSTOMER_PROFILE_LINK) is True, "LINK is not present"

    def should_be_last_transaction(self):
        assert self.is_element_present(*CustomersPageLocators.LAST_TRANSACTION) is True, \
            "In column 'LAST TRANSACTION' not present any transactions"

    def last_transaction_date(self):
        last_transaction = self.browser.find_element(*CustomersPageLocators.LAST_TRANSACTION)
        assert str(datetime.datetime.today().date()) in last_transaction.text, "Wrong last_transaction date"

    def enter_usd_into_search(self):
        self.browser.find_element(*CustomersPageLocators.SEARCH).send_keys("USD")

    def entered_currency_is_not_present(self):
        assert self.is_not_element_present(*CustomersPageLocators.TABLE_ENTRY_CURRENCY) is True,\
            "For CA company search is found USD currency"

    def title_of_customer_page(self):
        print(self.browser.title)
        assert self.browser.title == "Customers | Canada Autotest Company | BankSEND®", "Wrong title for Customers page"


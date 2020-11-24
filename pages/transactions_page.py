from .base_page import BasePage
from .locators import TransactionsPageLocators
import time

global customer_id
customer_id = 2


class TransactionsPage(BasePage):

    def should_be_page_name(self):
        print(self.browser.find_element(*TransactionsPageLocators.TITLE_OF_TRANSACTIONS_PAGE).text)
        assert self.browser.find_element(*TransactionsPageLocators.TITLE_OF_TRANSACTIONS_PAGE).text == \
               "Transactions A list of all processed transactions", "Wrong name of TRANSACTIONS page"

    def click_to_menu_button_transactions(self):
        self.browser.find_element(*TransactionsPageLocators.TRANSACTIONS_MENU_BUTTON).click()

    def should_be_merchant_income(self):
        if self.browser.find_element(*TransactionsPageLocators.MERCHANT_INCOME).is_displayed() is True:
            return True
            #assert self.is_element_present(*TransactionsPageLocators.MERCHANT_INCOME)
        else:
            return False

    def title_of_the_page(self):
        print(self.browser.title)
        assert self.browser.title == "Transactions | Canada Autotest Company | BankSEND®", \
            "Wrong title for transactions page"

    def redirect_to_admin_dashboard(self):
        self.browser.find_element(*TransactionsPageLocators.ADMIN_DASHBOARD).click()

    def chose_ca_autotest_company(self):
        self.browser.find_element(*TransactionsPageLocators.COMPANY_ON_DASHBOARD_CA_AUTOTEST).click()

    def should_be_banksend_income(self):
        if self.browser.find_element(*TransactionsPageLocators.BANKSEND_INCOME).is_displayed():
            return True
        else:
            return False

    def should_be_clear_filter_button(self):
        assert self.browser.find_element(*TransactionsPageLocators.CLEAR_FILTER).is_displayed() is True, \
            "Clear filter button not displayed"

    def find_needed_customer(self):
        global customer_id
        elements = self.browser.find_elements(*TransactionsPageLocators.LINKS_ON_TRANSACTIONS_PAGE)
        for elem in elements:
            #print(elem.get_attribute("href"))
            if elem.get_attribute("href") == \
                    f"https://test.banksend.com/admin/customer-profile?customerId={customer_id}&merchantId=5" and \
                    elem.text == "autotest":
                print(elem.get_attribute("href"))
                print(elem.text)
                self.browser.execute_script("return arguments[0].scrollIntoView(true);", elem)
                elem.click()
                break
            #    link = elem.get_attribute("href")
            #    self.browser.execute_script("window.open('" + link +"');")

    def current_page(self):
        assert self.browser.current_url == f"https://test.banksend.com/admin/customer-profile?" \
                                           f"customerId={customer_id}&merchantId=5", \
            "Button, on transactions page dashboard not redirected correctly"



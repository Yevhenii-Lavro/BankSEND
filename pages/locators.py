from selenium.webdriver.common.by import By

global customer_id
customer_id = 7


class SignInPageLocators:
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn-name")
    BANKSEND_LOGO = (By.CSS_SELECTOR, "img.logo")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".text-danger")
    EMPTY_FIELD = (By.CSS_SELECTOR, "div.invalid-feedback.animated.fadeInDown > div")


class LoggedPageLocators:
    USER_LOGGED = (By.CSS_SELECTOR, ".chartjs-render-monitor[width]")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".si.si-logout")


class DashboardPageLocators:
    DASHBOARD = (By.CSS_SELECTOR, ".chartjs-render-monitor[width]")
    TRANSACTIONS_BOARD_BUTTON = (By.CSS_SELECTOR, "tabset > ul > li:nth-child(1) > a")
    DAILY_SUMMARY_BUTTON = (By.CSS_SELECTOR, "#main-container ul > li:nth-child(2) > a")
    SUPERADMIN_DASHBOARD = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(2) > a")
    SUPERADMIN_REPORTS = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(3) > a")
    SUPERADMIN_SETTINGS = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(4) > a")
    SUPERADMIN_COMPLIANCE = (By.CSS_SELECTOR, "div:nth-child(3) > ul:nth-child(2) > li:nth-child(5) > a")
    DASHBOARD_TRANSACTION_LIST_TITLE = (By.CSS_SELECTOR, "div > div.block > div > h3")
    DASHBOARD_DAILY_SUMMARY_TITLE = (By.CSS_SELECTOR, "app-daily-summary-datatable > div > div > h3")
    FILTER_FROM = (By.CSS_SELECTOR, "#filterFrom")
    FILTER_TO = (By.CSS_SELECTOR, "#filterTo")
    RESET_BUTTON = (By.CSS_SELECTOR, ".ml-10.btn")


class PaymentFormLocators:
    BANK_HEADER = (By.CSS_SELECTOR, "#bank0-header")
    RADIO_BUTTON = (By.CSS_SELECTOR, "#bank0 > div > div:nth-child(1) > label > span > i")
    ACCEPT_BUTTON = (By.TAG_NAME, "app-to-customer-defined > div > div > button")
    ACCEPT_BUTTON_FOR_INCOME = (By.CSS_SELECTOR, "div > div > div > button")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "div > #aut-continue-button")
    SELECT_BANK = (By.CSS_SELECTOR, "ul > li:nth-child(1) > button")
    USERNAME = (By.CSS_SELECTOR, "#username")  # for old plaid .Input__field#username
    PASSWORD = (By.CSS_SELECTOR, "#password")  # for old plaid .Input__field#password
    CARD_HEADER = (By.CSS_SELECTOR, ".card-header")
    AGREE_AND_SIGN_BUTTON = (By.CSS_SELECTOR, "div.w-100.mt-3 > button")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#aut-submit-button")  # for old plaid button.Button
    IFRAME = (By.CSS_SELECTOR, "#plaid-link-iframe-1")
    POLICY = (By.CSS_SELECTOR,
              "body > reach-portal > div:nth-child(3) >"
              " div > div > div > div > div.Overlay > div > div >"
              " div.Pane.PrivacyInterstitialPane.Pane--is-plaid-branded >"
              " div.PaneActions.PaneActions--no-padding-top >"
              " div > button.TextButton.TextButton--is-action.TextButton--is-plaid-branded.TextButton--no-margin")
    FRAMES = (By.TAG_NAME, "iframe")
    FIRST_FRAME = (
        By.CSS_SELECTOR, "body > app-root > app-payment-form > div > div > div.container > div.row.pt-4 > iframe")
    SECOND_FRAME = (By.CSS_SELECTOR, "#plaid-link-iframe-1")
    SUCCESSFULLY_MESSAGE = (By.CSS_SELECTOR, ".avenir-medium.text-gray-middle")
    MAIL_LAST_UNREAD_MESSAGE = (By.CSS_SELECTOR, "#R0 > td:nth-child(3)")
    MESSAGES = (By.CSS_SELECTOR, "tr > td > ul > li")
    EMAIL_USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    EMAIL_PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    EMAIL_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".ZLoginButton")
    COMPANY_LOGO_IN_EMAIL = (By.CSS_SELECTOR,
                             "#background_table > tbody > tr:nth-child(1) > td > table > tbody > tr > td > img")
    CURRENCY_IN_EMAIL = (By.CSS_SELECTOR,
                         "body > div > div > table:nth-child(4) > tbody >"
                         " tr > td > table > tbody > tr:nth-child(2) > td > span")
    AMOUNT_IN_EMAIL = (By.CSS_SELECTOR,
                       "table:nth-child(2) > "
                       "tbody > tr > td > table.body_table > tbody > tr:nth-child(2) > td:nth-child(1)")
    TRANSACTION_ID_IN_EMAIL = (By.CSS_SELECTOR,
                               "#background_table > tbody > tr:nth-child(2) >"
                               " td > table:nth-child(1) > tbody > tr:nth-child(2) > td")
    BANKSEND_LOGO = (By.CSS_SELECTOR, "#background_table_footer >"
                                      " tbody > tr > td > table:nth-child(2) > tbody >"
                                      " tr > td > table > tbody > tr > td:nth-child(2) > img")
    POWERED_BY = (By.CSS_SELECTOR,
                  "#background_table_footer > tbody > tr > td > table:nth-child(2) > "
                  "tbody > tr > td > table > tbody > tr > td:nth-child(1)")
    ACCEPT_BUTTON_EMAIL = (By.CSS_SELECTOR, "#background_table_footer > "
                                            "tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(6) > td > a")
    WINDOW_IN_EMAIL = (By.CSS_SELECTOR, ".WindowInnerContainer")
    YES_BUTTON = (By.CSS_SELECTOR, "#YesNoMsgDialog_button5_title")
    EMAIL_CONTENT = (By.CSS_SELECTOR, "#zv__CLV-main__CV")
    IFRAME_EMAIL = (By.CSS_SELECTOR, "#iframeBody > iframe")
    DROP_DOWN_EMAIL = (By.CSS_SELECTOR, "#client")
    INPUT_SMS_CODE = (By.CSS_SELECTOR, "#pin")
    ACTIVATE_BUTTON_VIA_EMAIL = (By.CSS_SELECTOR, "body >"
                                                  " app-root > app-to-customer-defined >"
                                                  " div > div > app-pin > div > form > section > div > button")
    SEARCH_FIELD_IN_EMAIL = (By.CSS_SELECTOR, "#searchField")
    COMPANY_LOGO_IN_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-company-logo > a > img")
    TRANSACTION_AMOUNT_IN_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-to-customer-defined > div > div > app-company-header "
                                                            "> section > div.w-100.text-center > "
                                                            "span > span:nth-child(1)")
    TRANSACTION_CURRENCY_IN_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-to-customer-defined > div > div > app-company-header"
                                                              " > section > div.w-100.text-center >"
                                                              " span > span:nth-child(2)")
    FROM_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "div.wrapper-invoice__from.d-flex.flex-wrap"
                                              " > span.from-to.avenir-heavy.d-inline-block")
    TO_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "span.from-to.avenir-heavy.d-inline-block.to.text-left.text-lg-right.pr-2")
    DEFAULT_LANGUAGE_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "#dropdownMenuButton")
    FIRST_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-drop-lang > div > div > span:nth-child(1)")
    SECOND_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-drop-lang > div > div > span:nth-child(2)")
    THIRD_LANGUAGE_FROM_LIST_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-drop-lang > div > div > span:nth-child(3)")
    DESCRIPTIONS_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-to-customer-defined >"
                                                      " div > div > app-pin > div > form > section > "
                                                      "div > div.style-form.text-center > h3")
    BANKSEND_LOGO_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "body > app-root > "
                                                       "app-to-customer-defined > div > footer > span > img")
    POWERED_BY_ON_ACTIVATE_PAGE = (By.CSS_SELECTOR, "app-to-customer-defined > div > footer > span")


class CustomersPageLocators:
    MENU_BUTTON = (By.CSS_SELECTOR, "#customers")
    PAGE_NAME = (By.CSS_SELECTOR, ".content-heading")
    MERCHANT_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(2)")
    ID_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(3)")
    NAME_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(4)")
    REGISTERED_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(5)")
    LAST_TRANSACTION_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(6)")
    IN_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(7)")
    IN_TRX_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(8)")
    OUT_V_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(9)")
    OUT_V_TRX_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(10)")
    OUT_NV_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(11)")
    OUT_NV_TRX_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(12)")
    OUT_CD_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(13)")
    OUT_CD_TRX_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(14)")
    CURRENCY_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(15)")
    STATUS_COLUMN = (By.CSS_SELECTOR, "thead > tr > th:nth-child(16)")
    FILTER_BY = (By.CSS_SELECTOR, "#topToolbarForm > label > select")
    RESET_BUTTON = (By.CSS_SELECTOR, "#resetBtn")
    FROM = (By.CSS_SELECTOR, "div > span:nth-child(1) > input")
    TO = (By.CSS_SELECTOR, "div > span:nth-child(3) > input")
    SHOWS_DROPDOWN = (By.CSS_SELECTOR, "#DataTables_Table_1_length > label > select")
    PAGES_IN_DROPDOWN = (By.CSS_SELECTOR, "#DataTables_Table_1_length > label > select > option")
    PAGES_SHOWING = (By.CSS_SELECTOR, "#datatable_info")
    BALANCE_MERCHANT = (By.CSS_SELECTOR, ".merchant-incoming")
    TRANSFER_BUTTON = (By.CSS_SELECTOR, "li > div > button:nth-child(3)")
    SEARCH = (By.CSS_SELECTOR, "#search")
    CUSTOMER_PROFILE_LINK = (By.CSS_SELECTOR, "#datatable > tbody > tr:nth-child(1) > td:nth-child(2) > a")
    LAST_TRANSACTION = (By.CSS_SELECTOR, "#datatable > tbody > tr:nth-child(1) > td:nth-child(5)")
    TABLE_ENTRY_CURRENCY = (By.CSS_SELECTOR, "#datatable > tbody > tr:nth-child(1) > td:nth-child(14)")


class CustomerProfilePageLocators:
    PAGE_NAME = (By.CSS_SELECTOR, ".content-heading")
    BALANCE_WINDOW = (By.CSS_SELECTOR, ".merchant-incoming")
    ID = (By.CSS_SELECTOR, "div > div.block-header.block-header-default.text-nowrap > h3")
    CUSTOMER_ID = (By.CSS_SELECTOR, "div > div.block-header.block-header-default.text-nowrap > h3 > span")
    BLOCK_WITH_DETAILS = (By.CSS_SELECTOR, "div.col.flex-md-grow-0.flex-shrink-0 > div > div.block-content")
    NAME = (By.CSS_SELECTOR, "h6:nth-child(1) > span:nth-child(1)")
    REGISTERED = (By.CSS_SELECTOR, "h6:nth-child(2) > span:nth-child(1)")
    DATE_OF_BIRTH = (By.CSS_SELECTOR, "h6:nth-child(3) > span:nth-child(1)")
    ADDRESS = (By.CSS_SELECTOR, "h6:nth-child(4) > span:nth-child(1)")
    PHONE_NUMBER = (By.CSS_SELECTOR, "h6:nth-child(5) > span:nth-child(1)")
    EMAIL = (By.CSS_SELECTOR, "h6:nth-child(6) > span:nth-child(1)")
    CUSTOMER_BLOCK_BUTTON = (By.CSS_SELECTOR, "div.text-center.mb-15 > button")
    TRANSACTION_LIST = (By.CSS_SELECTOR, "div:nth-child(3) > div > div > div.block-content")
    SEARCH = (By.CSS_SELECTOR, "#search")
    FILTER_FROM = (By.CSS_SELECTOR, "#filterFrom")
    FILTER_TO = (By.CSS_SELECTOR, "span:nth-child(3) > input")
    SHOW_FEES = (By.CSS_SELECTOR, "div.form-group.d-sm-mb-0.form-group-mobile-checkbox > label")
    DROP_DOWN_SHOW_ENTRIES = (By.CSS_SELECTOR, "label > select")
    DATE_TIME = (By.CSS_SELECTOR, "tr > th:nth-child(2)")
    TRANSACTION_ID = (By.CSS_SELECTOR, "tr > th:nth-child(3)")
    DEPOSIT = (By.CSS_SELECTOR, "tr > th:nth-child(4)")
    DESCRIPTION = (By.CSS_SELECTOR, "tr > th:nth-child(5)")
    AMOUNT = (By.CSS_SELECTOR, "tr > th:nth-child(6)")
    CURRENCY = (By.CSS_SELECTOR, "tr > th:nth-child(7)")
    STATUS = (By.CSS_SELECTOR, "tr > th:nth-child(8)")
    SUMMARY_AND_PAYMENT_METHODS_TABLE = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div")
    SUMMARY_BUTTON = (By.CSS_SELECTOR, "div > tabset > ul > li:nth-child(1) > a")
    PAYMENT_METHOD_BUTTON = (By.CSS_SELECTOR, "div > tabset > ul > li:nth-child(2) > a")
    INCOMING = (By.CSS_SELECTOR, "tab.active.tab-pane > div >"
                                 " div > div > table > tbody > tr:nth-child(1) > td:nth-child(1)")
    BLOCK_BUTTON_FOR_INCOMING = (By.CSS_SELECTOR, "tab.active.tab-pane"
                                                  " > div > div > div > table > tbody > tr:nth-child(1) "
                                                  "> td:nth-child(2)")
    ACTIONS_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(2)")
    PREPARED_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(3)")
    PENDING_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(5)")
    SETTLED_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(7)")
    TOTAL_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(9)")
    CURRENCY_COLUMN = (By.CSS_SELECTOR, "tab.active.tab-pane > div > div > div > table > thead > th:nth-child(11)")
    OUTGOING_CUSTOMER_DEFINED = (By.CSS_SELECTOR, "tab.active.tab-pane >"
                                                  " div > div > div > table > tbody >"
                                                  " tr:nth-child(2) > td:nth-child(1)")
    OUTGOING_NOT_VERIFIED = (By.CSS_SELECTOR, "tab.active.tab-pane >"
                                              " div > div > div > table > tbody > tr:nth-child(3) > td:nth-child(1)")
    OUTGOING_VERIFIED = (By.CSS_SELECTOR, "tab.active.tab-pane >"
                                          " div > div > div > table > tbody > tr:nth-child(4) > td:nth-child(1)")
    BLOCK_BUTTON_FOR_VERIFIED = (By.CSS_SELECTOR, "tab.active.tab-pane >"
                                                  " div > div > div > table > tbody"
                                                  " > tr:nth-child(4) > td:nth-child(2)")
    BLOCK_BUTTON_FOR_NOT_VERIFIED = (By.CSS_SELECTOR, "tab.active.tab-pane >"
                                                      " div > div > div >"
                                                      " table > tbody > tr:nth-child(3) > td:nth-child(2)")
    BLOCK_BUTTON_FOR_CUSTOMER_DEFINED = (By.CSS_SELECTOR, "tab.active.tab-pane"
                                                          " > div > div > div >"
                                                          " table > tbody > tr:nth-child(2) > td:nth-child(2)")
    BANK = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(1)")
    ACCOUNT_NAME = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(2)")
    ENDS_WITH = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(3)")
    REGISTERED_COLUMN_IN_PAYMENT_TAB = (By.CSS_SELECTOR, "tab.tab-pane.active "
                                                         "> div > div > div > table > thead > th:nth-child(4)")
    PRE_AUTORIZED = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(5)")
    VERIFIED_COLUMN = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(6)")
    LAST_BALANCE = (By.CSS_SELECTOR, "tab.tab-pane.active > div > div > div > table > thead > th:nth-child(7)")
    ACTIONS_COLUMN_IN_PAYMENT_TAB = (By.CSS_SELECTOR, "tab.tab-pane.active"
                                                      " > div > div > div > table > thead > th:nth-child(8)")


class TransactionsPageLocators:
    TRANSACTIONS_MENU_BUTTON = (By.CSS_SELECTOR, "#transactions")
    TITLE_OF_TRANSACTIONS_PAGE = (By.CSS_SELECTOR, "#page-container > app-transactions > div > h2")
    MERCHANT_INCOME = (By.CSS_SELECTOR, "div.wrap-balance-block-wrapper.bg-white.d-flex > div.merchant-incoming")
    ADMIN_DASHBOARD = (By.CSS_SELECTOR, "#adminDashboard")
    COMPANY_ON_DASHBOARD_CA_AUTOTEST = (By.CSS_SELECTOR, "#datatable > tbody > tr:nth-child(5) > td:nth-child(3) > a")
    BANKSEND_INCOME = (By.CSS_SELECTOR, "#page-header > div > div >"
                                        " div.wrap-balance-block-wrapper.bg-white.d-flex >"
                                        " div.text-center.banksend-incoming > div")
    CLEAR_FILTER = (By.CSS_SELECTOR, "#id208 > div > button")
    CUSTOMER = (By.LINK_TEXT, f"https://test.banksend.com/admin/customer-profile?customerId={customer_id}&merchantId=5")
    LINKS_ON_TRANSACTIONS_PAGE = (By.CSS_SELECTOR, "td > a[href]")

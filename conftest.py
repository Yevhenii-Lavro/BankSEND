import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Chose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Chose language: en, fr, ru, es, etc...")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    #    browser = None
    #   op = webdriver.ChromeOptions()
    #   op.add_argument('headless')
    #   driver = webdriver.Chrome(options=op)
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    #    options.add_argument('headless')  # starting headless browser
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(10)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



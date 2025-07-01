import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
import time
import uuid

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")

@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def setup_user(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    email = f"{uuid.uuid4()}@fakemail.org"
    password = str(time.time())
    page.register_new_user(email, password)
    page.should_be_authorized_user()

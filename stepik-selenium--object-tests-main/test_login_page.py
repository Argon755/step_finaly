import pytest
from pages.login_page import LoginPage

def test_login_page_has_login_form(browser):
    page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/")
    page.open()
    page.should_be_login_form()
    page.should_be_register_form()
    page.should_be_login_url()

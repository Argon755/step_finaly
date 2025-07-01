import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_added_to_basket()

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser, setup_user):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_added_to_basket()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty()
    basket.should_be_empty_message_present()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()

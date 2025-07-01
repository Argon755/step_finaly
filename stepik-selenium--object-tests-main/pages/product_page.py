from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators
import time

class ProductPage(BasePage):
    
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        super().solve_quiz_and_get_code()

    def should_be_added_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.ADDED_MESSAGE).text
        assert product_name in message_text, "Product name is not in the success message"

        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text.strip()
        assert product_price in basket_price, f"Expected price {product_price} to be in basket price {basket_price}"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not present"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

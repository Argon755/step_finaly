from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty"

    def should_be_empty_message_present(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Empty basket message is missing"

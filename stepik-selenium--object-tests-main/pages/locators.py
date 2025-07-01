from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")

class MainPageLocators():
    pass  # for future use

class LoginPageLocators():
    REGISTRATION_EMAIL = (By.NAME, "registration-email")
    REGISTRATION_PASSWORD = (By.NAME, "registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.NAME, "registration-password2")
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") 

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p") 


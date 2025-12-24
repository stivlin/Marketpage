from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success:nth-of-type(1) strong")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info:nth-of-type(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_TEXT = (By.CSS_SELECTOR, ".login_form h2")

    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")

class LoginPageLocators():
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTER_SUCCESS = (By.CSS_SELECTOR, ".alert-success .wicon")
    # assert Thanks for registering!
    EMAIL_ADDRESS = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
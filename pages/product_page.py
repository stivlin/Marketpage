from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_success_message_with_correct_product_name(self):
        name_on_page = self.get_product_name()
        name_in_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME).text
        assert name_on_page == name_in_message, f"Expected '{name_on_page}', got '{name_in_message}'"

    def should_be_basket_total_equal_to_product_price(self):
        price_on_page = self.get_product_price()
        price_in_message =  self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert price_on_page == price_in_message, f"Expected '{price_in_message}', got '{price_in_message}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME), \
            "Success message is presented, but should be"


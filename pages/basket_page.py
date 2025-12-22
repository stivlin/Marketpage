from pages.base_page import BasePage
from pages.locators import BasePageLocators

class BasketPage(BasePage):

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_BUTTON), \
            "Basket is not empty"

    def get_message_text(self):
        return self.browser.find_element(*BasePageLocators.EMPTY_BASKET)

    def empty_text_basket(self):
        empy_text = self.get_message_text().text
        assert empy_text == "Your basket is empty.", "Basket is not empty"

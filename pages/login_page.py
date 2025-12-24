from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self,email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_ADDRESS).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON).click()

    def should_be_account_successfully_created(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_SUCCESS), "unsuccessful register"

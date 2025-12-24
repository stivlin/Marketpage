import time
from time import sleep

from pages.login_page import LoginPage
from pages.product_page import ProductPage

# url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
EMAIL = str(time.time()) + "@fakemail.org"
PASSWORD = "StrongPass12345!"

class TestUserAddToBasketFromProductPage():

    def test_user_can_add_product_to_basket(self, browser, link, register_user):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message_with_correct_product_name()
        page.should_be_basket_total_equal_to_product_price()

    def test_user_cant_see_success_message(self, browser,link,register_user):
        page = ProductPage(browser,link)
        page.open()
        page.should_not_be_success_message()

class TestLoginPage():
    def test_user_registration(self, browser, link):
        page = LoginPage(browser,link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email=EMAIL, password=PASSWORD)
        page.should_be_authorized_user()
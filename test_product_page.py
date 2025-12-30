import time
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage

EMAIL = str(time.time()) + "@fakemail.org"
PASSWORD = "StrongPass12345!"


@pytest.mark.need_review
class TestUser():
    def test_user_can_add_product_to_basket(self, browser, link, register_user):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message_with_correct_product_name()
        page.should_be_basket_total_equal_to_product_price()

@pytest.mark.need_review
class TestGuest():
    def test_guest_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_success_message_with_correct_product_name()
        page.should_be_basket_total_equal_to_product_price()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self,browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_not_be_success_message()

    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser,link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_form()

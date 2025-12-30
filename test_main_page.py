import pytest
from pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self,browser,link):
        page = BasketPage(browser,link)
        page.open()
        page.go_to_basket_page()
        page.check_basket_is_empty()

    def test_guest_can_go_to_login_page(self, browser,link):
        page = BasketPage(browser,link)
        page.open()
        page.go_to_login_page()

    def test_guest_should_see_login_link(self, browser,link):
        page = BasketPage(browser,link)
        page.open()
        page.should_be_login_link()

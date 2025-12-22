from pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser,link):
    page = BasketPage(browser,link)
    page.open()
    page.go_to_basket_page()
    page.check_basket_is_empty()
    page.empty_text_basket()
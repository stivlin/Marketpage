import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

# url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


def test_guest_can_add_product_to_basket(browser, link):

    page = ProductPage(browser,link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message_with_correct_product_name()
    page.should_be_basket_total_equal_to_product_price()

def test_guest_cant_see_success_message(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link ='http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser,link):
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_form()


# Гость открывает страницу товара
# Переходит в корзину по кнопке в шапке
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста





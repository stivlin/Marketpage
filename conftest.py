import time
import pytest
from selenium import webdriver

from pages.login_page import LoginPage

BASE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser
    print('\nend chrome browser')
    browser.quit()

@pytest.fixture
def register_user(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()

    email = f"autotest_{time.time()}@fakemail.org"
    password = "StrongPass12345!"
    page.register_new_user(email, password)
    page.should_be_authorized_user()

    return {"email": email, "password": password}


@pytest.fixture(params=[
    pytest.param(
        f"{BASE_URL}?promo=offer{i}",
        marks=pytest.mark.xfail if i == 7 else ()
    )
    for i in range(1)
])
def link(request):
    return request.param
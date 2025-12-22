import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    browser = webdriver.Chrome()

    yield browser
    print('\nend chrome browser')
    browser.quit()

BASE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.fixture(params=[
    pytest.param(
        f"{BASE_URL}?promo=offer{i}",
        marks=pytest.mark.xfail if i == 7 else ()
    )
    for i in range(1)
])
def link(request):
    return request.param
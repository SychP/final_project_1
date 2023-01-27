from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
import pytest

#pytest -s test_main_page.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    cart_page = BasketPage(browser, link)
    cart_page.should_not_be_item_in_basket()
    cart_page.should_be_empty_basket_msg()

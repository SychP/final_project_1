from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .pages.product_page import MainPage

#pytest -s test_product_page.py

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_can_add_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_item_added_to_card_msg()
    page.cart_price_msg_equals_item_price()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()
        

def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_not_be_success_message()
 
 
def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = MainPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_of_success_message()


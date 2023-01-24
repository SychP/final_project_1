from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_ITEM_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ITEM_ADDED_TO_CART = (By.CSS_SELECTOR, ".alert-success strong")
    CART_TOTAL_PRICE = (By.CSS_SELECTOR, ".alert-info strong")
    
    


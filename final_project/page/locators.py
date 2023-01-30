from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,".col-sm-6 > h1" )
    PRODUCT_IN_BASKET  =(By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success> .alertinner") 
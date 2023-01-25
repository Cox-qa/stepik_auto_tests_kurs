from selenium.webdriver.common.by import By
import time



link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_basket_is_present(browser,):
    try:
        browser.get(link)
        browser.implicitly_wait(15)
        answer_locate = browser.find_element(By.ID, "add_to_basket_form")
        assert answer_locate, "Item to add to cart not found"
    finally:
        time.sleep(30)


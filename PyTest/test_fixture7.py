import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1", "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1", "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1", "https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
class TestLogin:
    def test_authorization(self, browser, links):
        x = str(math.log(int(time.time())))
        link = f"{links}"
        try:
            browser.get(link)
            button = browser.find_element(By.CLASS_NAME, "ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button")
            button.click()
            input1 = browser.find_element(By.CSS_SELECTOR,"#id_login_email")         
            input1.send_keys("login")
            input2 = browser.find_element(By.CSS_SELECTOR,"#id_login_password")    
            input2.send_keys("password")
            button = browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader")
            button.click()
            input1 = browser.find_element(By.TAG_NAME, "textarea")  #(By.CSS_SELECTOR, "class='ember-text-area.ember-view.textarea.string-quiz__textarea'")
            input1.send_keys(x)
            button = WebDriverWait(browser, 5).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "class='submit-submission'"))
                )
            button.click()
            answer = browser.find_element(By.CLASS_NAME,"smart-hints__hint")
            answer_text = answer.text
            assert answer_text == "Correct!", 'message is not "Correct!"'
        finally:
            time.sleep(5)
        
        

        
        
       


  
 #text_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
        #text_element_esli_pravilno = text_element.text
        #if text_element_esli_pravilno != "Correct!":
           # text_element_esli_nepravilno = text_element_esli_pravilno
            #print(text_element_esli_nepravilno)

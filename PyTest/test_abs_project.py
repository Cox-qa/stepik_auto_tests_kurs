from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)  
        input1 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.first_class input.first")         
        input1.send_keys("Semen")
        input2 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.second_class input.second")    
        input2.send_keys("Kohk")
        input3 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.third_class input.third")
        input3.send_keys("yaebaltvoyrot228@yandex.ru")      
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()    
        time.sleep(1) 
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")  
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")
        
    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.htm"
        browser = webdriver.Chrome()
        browser.get(link)  
        input1 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.first_class input.first")         
        input1.send_keys("Semen")
        input2 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.second_class input.second")    
        input2.send_keys("Kohk")
        input3 = browser.find_element(By.CSS_SELECTOR,"div.first_block div.third_class input.third")
        input3.send_keys("yaebaltvoyrot228@yandex.ru")      
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()    
        time.sleep(1) 
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")  
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration failed")

if __name__ == "__main__":
    unittest.main()
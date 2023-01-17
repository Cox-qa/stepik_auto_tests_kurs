from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
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

   
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    
    time.sleep(10)
    
    browser.quit()
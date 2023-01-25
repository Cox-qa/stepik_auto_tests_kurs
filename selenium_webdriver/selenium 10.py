from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Semen")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kohk")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("yaebaltvoyrot228@yandex.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, 'text.txt')
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")           
    element.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    
    time.sleep(15)
    
    browser.quit()
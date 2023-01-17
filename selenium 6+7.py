from selenium import webdriver
from selenium.webdriver.common.by import By
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #x_element = browser.find_element(By.CSS_SELECTOR, selector_value)
    #x = x_element.text
    #y = calc(x)
    x_element = browser.find_element(By.ID, "treasure")
    x_values = x_element.get_attribute("valuex")
    x = x_values
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']")
    option2.click()
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()


finally:
    
    time.sleep(15)
    
    browser.quit()

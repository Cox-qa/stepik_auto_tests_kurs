from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time



link1 = "https://suninjuly.github.io/selects1.html"
link2 = "https://suninjuly.github.io/selects2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link1)
    num1_element = browser.find_element(By.CSS_SELECTOR, "[id='num1']")
    num1 = num1_element.text
    num2_element = browser.find_element(By.CSS_SELECTOR, "[id='num2']")
    num2 = num2_element.text
    summma = int(num1_element.text)+int(num2_element.text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(summma))
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    

    
finally:
    
    time.sleep(5)

    browser.quit()
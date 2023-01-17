import time

from selenium import webdriver                              # webdriver это и есть набор команд для управления браузером

from selenium.webdriver.common.by import By                 # импортируем класс By, который позволяет выбрать способ поиска элемента

driver = webdriver.Chrome()                                 # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера

time.sleep(5)                                                 # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере

driver.get("https://suninjuly.github.io/text_input_task.html")  # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
time.sleep(5)

textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")  # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
                                                              # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
                                                              # Ищем поле для ввода текста
textarea.send_keys("get()")                                   # Напишем текст ответа в найденное поле
time.sleep(5)

submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission") # Найдем кнопку, которая отправляет введенное решение

submit_button.click()                                                  # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
time.sleep(5)

driver.quit()                                                           # После выполнения всех действий мы должны не забыть закрыть окно браузер

# 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html
# 2. Нажать на кнопку
# 3. Переключиться на новую вкладку
# 4. Пройти капчу для робота и получить число-ответ

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
    

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    # открытие браузера и переход по ссылке
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # нажать на кнопку
    button_magical_journey = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
    button_magical_journey.click()

    # переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # на новой странице
    # вычесление переменой x
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # ввод ответа в поле ввода
    
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    
    #нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    submit_button.click()
    
    
finally:
    time.sleep(20)
    browser.quit()
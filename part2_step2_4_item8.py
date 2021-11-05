# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # ожидает пока в элементе не появиться текст "$100"   
    text_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    # нажимаем кнопку book
    button_book = browser.find_element_by_id("book")
    button_book.click()
    
    # скролл страницы до кнопки submit
    button_submit = browser.find_element_by_id("solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    
    # вычесление переменой x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    # ввод ответа в поле ввода
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    
    #нажимаем кнопку Submit
    button_submit.click()   
finally:
    time.sleep(10)
    browser.quit()
    
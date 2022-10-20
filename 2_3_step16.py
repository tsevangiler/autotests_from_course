from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.trollface.btn')
    button.click()
    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

    browser.switch_to.window(browser.window_handles[1])    # или тоже самое с 2 строчками выше

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(2)
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = browser.find_element(By.TAG_NAME, 'button')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(2)
    browser.quit()

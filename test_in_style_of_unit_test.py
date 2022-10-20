from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import unittest

class TestAbs(unittest.TestCase):
    def test_regist1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group first_class']//input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']//input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group third_class']//input")
        input3.send_keys("aaaaaaaaaa@mail.ru")
        input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group first_class']//input")
        input4.send_keys("8900000000000")
        input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group second_class']//input")
        input5.send_keys("Moscow, Gruzinsky Val")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Congratulations! You have successfully registered!")

    def test_regist2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group first_class']//input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group second_class']//input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//div[@class='form-group third_class']//input")
        input3.send_keys("aaaaaaaaaa@mail.ru")
        input4 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group first_class']//input")
        input4.send_keys("8900000000000")
        input5 = browser.find_element(By.XPATH, "//div[@class='second_block']//div[@class='form-group second_class']//input")
        input5.send_keys("Moscow, Gruzinsky Val")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "FAILED")
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

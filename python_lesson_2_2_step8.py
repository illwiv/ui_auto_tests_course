from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']:required")
    first_name.send_keys("Roman")

    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']:required")
    last_name.send_keys("Remezov")

    email = browser.find_element(By.CSS_SELECTOR, "[name='email']:required")
    email.send_keys("email@example.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()

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

    click_to_new_link = browser.find_element(By.CSS_SELECTOR, "button.trollface")
    click_to_new_link.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button2.click()

finally:
    time.sleep(10)
    browser.quit()

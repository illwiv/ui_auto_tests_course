from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    price = WebDriverWait(browser, 5).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    b_button = browser.find_element(By.ID, "book")
    b_button.click()

    x = browser.find_element(By.ID, "input_value")
    x = x.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

finally:
    time.sleep(10)
    browser.quit()


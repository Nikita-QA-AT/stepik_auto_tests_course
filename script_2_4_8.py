from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")


try:

    # ждем пока цена не станет 100
    WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    # нажимаем кнопку Book
    button_Book = browser.find_element(By.ID, "book").click()



    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x) 


    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)  

    button = browser.find_element(By.ID, "solve").click()

    print(browser.switch_to.alert.text)

finally:
    time.sleep(10)
    browser.quit()


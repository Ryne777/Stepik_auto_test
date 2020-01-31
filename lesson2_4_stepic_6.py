from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    browser.get(link)
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book").click()

    text = int(browser.find_element_by_id(
        "input_value").text)
    input = browser.find_element_by_id("answer")
    input.send_keys(calc(text))
    browser.find_element_by_id('solve').click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.close()
    browser.quit()

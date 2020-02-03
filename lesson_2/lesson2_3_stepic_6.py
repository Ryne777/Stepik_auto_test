from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    browser.get(link)
    button = browser.find_element_by_class_name("btn-primary").click()
    time.sleep(1)
    browser.switch_to_window(browser.window_handles[1])
    
    text = int(browser.find_element_by_id(
        "input_value").text)
    input = browser.find_element_by_id("answer")
    input.send_keys(calc(text))
    button = browser.find_element_by_class_name("btn-primary")

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.close()
    browser.quit()

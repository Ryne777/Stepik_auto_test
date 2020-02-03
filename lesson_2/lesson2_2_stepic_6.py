from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    browser.get(link)

    text = int(browser.find_element_by_id(
        "input_value").text)
    input = browser.find_element_by_id("answer")
    input.send_keys(calc(text))
    button = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    button = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    button = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    # browser.close()
    browser.quit()

from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    browser.get(link)

    text = int(browser.find_element_by_id("treasure").get_attribute("valuex"))
    input = browser.find_element_by_id("answer")
    input.send_keys(calc(text))
    button = browser.find_element_by_id("robotCheckbox")
    button.click()
    button = browser.find_element_by_id("robotsRule")
    button.click()
    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    # browser.close()
    browser.quit()

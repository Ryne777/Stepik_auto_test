from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    browser.get(link)

    text = int(browser.find_element_by_id("num1").text)
    text1 = int(browser.find_element_by_id("num2").text)
    input = Select(browser.find_element_by_id(
        "dropdown")).select_by_visible_text(str(text+text1))
    
    button = browser.find_element_by_class_name("btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # browser.close()
    browser.quit()

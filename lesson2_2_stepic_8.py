from selenium import webdriver
import time

import os

# получаем путь к директории текущего исполняемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла
file_path = os.path.join(current_dir, 'file.txt')


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector(
        "[placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(
        "[placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(
        "[placeholder='Enter email']")
    input3.send_keys("Smolensk")
    input1 = browser.find_element_by_id("file").send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    



# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    
finally:
    time.sleep(10)
    browser.quit()

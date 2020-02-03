import pytest
from selenium import webdriver
import time
import math


def answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(
        executable_path=r"C:\chromedriver\chromedriver.exe")

    yield browser
    print("\nquit browser..")
    browser.quit()


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.mark.parametrize('links', links)
def test_guest_should_see_login_link(browser, links):
    link = f"{links}"
    browser.implicitly_wait(30)
    browser.get(link)
    browser.find_element_by_css_selector(
        "[placeholder='Напишите ваш ответ здесь...']").send_keys(str(answer()))
    browser.find_element_by_class_name("submit-submission").click()
    assert (browser.find_element_by_class_name(
        "smart-hints__hint").text == "Correct!")

import time

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("https://ya.ru/")

current_title = driver.title
print("Текущий заголовок: ", current_title)
driver.back()
assert current_title == "Яндекс", "Некорректный заголовок страницы"
driver.refresh()


#current_title = driver.title
#print("Текущий заголовок: ", current_title)
#assert current_title == "Wikipedia123", "Некорректный заголовок страницы"



time.sleep(3)


a = 82 // 3**2 % 7
print(a)
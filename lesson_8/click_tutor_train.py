import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

name_field = driver.find_element("xpath", "//input[@id ='userName']")
email_field = driver.find_element("xpath", "//input[@id ='userEmail']")
cur_address_field = driver.find_element("xpath", "//textarea[@id='currentAddress']")
per_address_field = driver.find_element("xpath", "//textarea[@id ='permanentAddress']")

name_field.click()
name_field.clear()
name_field.send_keys("Artem")
assert"Artem" in name_field.get_attribute("value")

time.sleep(3)

email_field.click()
email_field.clear()
email_field.send_keys("ahuzikau@gmail.com")
assert"ahuzikau@gmail.com" in email_field.get_attribute("value")


cur_address_field.click()
cur_address_field.clear()
cur_address_field.send_keys("Lenina")
assert"Lenina" in cur_address_field.get_attribute("value")

per_address_field.click()
per_address_field.clear()
per_address_field.send_keys("Dovatora")
assert"Dovatora" in per_address_field.get_attribute("value")


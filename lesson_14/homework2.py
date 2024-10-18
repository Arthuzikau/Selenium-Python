import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager(driver_version="122.0.6261.95").install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10, poll_frequency=1)

driver.get("https://ticket.railway.ge/Account/Login")

before = driver.get_cookies()
print(before)

driver.delete_cookie('__RequestVerificationToken')

after = driver.get_cookies()
print(after)
time.sleep(15)
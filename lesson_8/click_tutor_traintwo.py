import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://the-internet.herokuapp.com/status_codes")

code200 = driver.find_element("xpath", "//li/a").click()
time.sleep(5)
driver.back()
time.sleep(5)

code301 = driver.find_element("xpath", "//li[2]/a").click()
time.sleep(3)
driver.back()
time.sleep(5)

code404 = driver.find_element("xpath", "//li[3]/a").click()
time.sleep(3)
driver.back()
time.sleep(5)

code500 = driver.find_element("xpath", "//li[4]/a").click()
time.sleep(3)
driver.back()
time.sleep(5)



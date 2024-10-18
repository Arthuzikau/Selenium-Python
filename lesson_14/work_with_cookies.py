import os
import time
import pickle

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager(driver_version="122.0.6261.953").install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10, poll_frequency=1)

driver.get("https://freeconferencecall.com/en/us/login")

driver.delete_all_cookies()
cookies = pickle.load(open(os.getcwd()+"cookies/cookies.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

time.sleep(5)

driver.refresh

time.sleep(5)
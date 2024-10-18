import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager(version="122.0.6261.95").install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,10, poll_frequency=1)

driver.get("https://demoqa.com/alerts")

BUTTON_3 = ("xpath", "//button[@id='confirmBUTTON']")
wait.until(EC.element_to_be_clickable(BUTTON_3)).click()

alert=wait.until(EC.alert_is_present())

driver.switch_to.alert

time.sleep(3)

alert.dismiss()

time.sleep(3)

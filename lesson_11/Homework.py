import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver,15, poll_frequency=1)
driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")

CHANGE_TEXT_BUTTON = ("xpath", "//button[text()='Change Text to Selenium Webdriver']")
DISPLAY_BUTTON = ("xpath", "//button[text()='Display button after 10 seconds']")
ENABLE_BUTTON = ("xpath", "//button[text()='Enable button after 10 seconds']")

wait.until(EC.element_to_be_clickable(CHANGE_TEXT_BUTTON)).click()
time.sleep(15)
wait.until(EC.element_to_be_clickable(DISPLAY_BUTTON)).click()
time.sleep(15)
wait.until(EC.element_to_be_clickable(ENABLE_BUTTON)).click()
time.sleep(15)

try:
    # Найти кнопку "Click me, to Open an alert after 5 seconds" и кликнуть
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Click me, to Open an alert after 5 seconds']"))
    )
    button.click()

    # Дождаться появления алерта
    alert = WebDriverWait(driver, 15).until(EC.alert_is_present())

    # Вывести текст алерта
    print("Текст алерта:", alert.text)

    # Закрыть алерт
    alert.accept()

finally:
    # Закрыть браузер
    driver.quit()



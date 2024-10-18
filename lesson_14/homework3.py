from selenium import webdriver
import pickle
import time

# Опции для отключения WebDriver и изменения User-agent
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')

# Создаем экземпляр драйвера
driver = webdriver.Chrome(options=options)

# Открываем страницу интернет-магазина (например, Amazon)
driver.get("https://www.amazon.com")

# Добавляем товары в корзину (предполагаем, что есть какие-то действия пользователя)
# Например, поиск товаров и добавление их в корзину
# Здесь нужно вставить соответствующий код, который осуществляет добавление товаров в корзину

# Сохраняем куки в файл
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

# Удаляем все товары из корзины (предполагаем, что есть соответствующая кнопка или ссылка)
# Здесь нужно вставить соответствующий код, который осуществляет удаление товаров из корзины

# Очищаем куки и перезагружаем страницу
driver.delete_all_cookies()
driver.refresh()

# Восстанавливаем сессию путем загрузки ранее сохраненных куков
with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

# Перезагружаем страницу для применения куков
driver.refresh()

# Закрываем браузер
driver.quit()
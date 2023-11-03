from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Створюємо і запускаємо браузер Chrome
driver = Chrome()
driver.get('https://qfinterfaces.qnomy.com:10443/QfRougeQa/VL_3.1_62/#/start/Qflow/personalId/5c0179c7-9fba-4a24-8583-3b56de13ea7d')

# Зачекайте декілька секунд для завантаження сторінки
time.sleep(2)

driver.execute_script("window.devtools.open()")

time.sleep(2)
# Знаходимо і клікаємо на чекбокс
element_checkbox = driver.find_element(By.XPATH, '//*[@id="loginCheckbox"]')
element_checkbox.click()
time.sleep(2)

driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.F12)
time.sleep(3)

# Знаходимо і клікаємо на кнопку входу
login_button = driver.find_element(By.XPATH, '/html/body/app-root/main/div[1]/app-login/form/div/button')
login_button.click()
time.sleep(3)

# Знаходимо і клікаємо на кнопку реєстрації
checkin_button = driver.find_element(By.XPATH, '/html/body/app-root/main/div/app-check-in-page/div/div[2]/button')
checkin_button.click()
time.sleep(3)

# Відкриваємо DevTools (F12)


# Завершуємо браузер
time.sleep(3)
driver.quit()

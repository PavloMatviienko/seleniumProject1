from selenium import webdriver
import time
import pyautogui

# Створення драйвера Chrome
driver = webdriver.Chrome()

# Відкриття сторінки Google
driver.get('https://www.google.com/')

# Затримка на 3 секунди (можете змінити цей час на потрібний вам)
time.sleep(3)

# Відкриття DevTools
pyautogui.hotkey('f12')
time.sleep(2)

pyautogui.hotkey('ctrl', ']','ctrl', ']','ctrl', ']')
time.sleep(3)
"""pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')"""
time.sleep(5)


# Затримка на 5 секунд для перегляду DevTools (можете змінити цей час)
time.sleep(5)

# Закриття браузера
#driver.quit()

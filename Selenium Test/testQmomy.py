
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
import pyautogui

driver = Chrome()

driver.get(
        'https://qfinterfaces.qnomy.com:10443/QfRougeQa/VL_3.1_62/#/start/Qflow/personalId/dfb6cbfd-0bf0-472d-8561-49ab2fd9adf2')


time.sleep(2)

pyautogui.hotkey('f12')
time.sleep(3)

pyautogui.hotkey('ctrl',']','ctrl',']','ctrl',']')
time.sleep(5)

element_checkbox = driver.find_element(By.XPATH, '//*[@id="loginCheckbox"]')

element_checkbox.click()
time.sleep(2)

login_button = driver.find_element(By.XPATH, '/html/body/app-root/main/div[1]/app-login/form/div/button')
login_button.click()

time.sleep(3)
checkin_button = driver.find_element(By.XPATH, '/html/body/app-root/main/div/app-check-in-page/div/div[2]/button')
checkin_button.click()
time.sleep(3)

time.sleep(3)

#if element_checkbox is not None:
  #  element_checkbox.send_keys("Ваш текст для введення" + Keys.RETURN)
#else:
    #print("Елемент не знайдений")




driver.quit()
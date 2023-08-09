
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.ukr.net/')
username = browser.find_element('_2p19QPd0')



#browser.quit()
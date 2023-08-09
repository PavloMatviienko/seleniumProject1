
from selenium import webdriver
import scrapy
browser = webdriver.Chrome()
browser.get('https://www.ukr.net/')
username = browser.find_element('_2p19QPd0')

from selenium import webdriver

website = 'https://www.ukr.net/'
path = 'C:\Users\PavloMatviienko\PycharmProjects\seleniumProject1\Driver\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

#browser.quit()
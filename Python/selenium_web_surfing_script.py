import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PROXY = '18.220.20.81:8080'

chrome_options = webdriver.ChromeOptions()
chrome = webdriver.Chrome(executable_path=r"C:\Users\dhane\chromedriver.exe", chrome_options=chrome_options)
chrome.get("https://google.com")
time.sleep(2)

search_bar = chrome.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search_bar.click()
search_bar.send_keys("Python is super cool.")
search_bar.send_keys(Keys.ENTER)

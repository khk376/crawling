from selenium import webdriver
import time

driver=webdriver.Chrome("c:/driver/chromedriver.exe")
URL="http://127.0.0.1:5500/6.selenium/step03myHtml.html"
driver.get(URL)


tag=driver.find_element_by_id("btn")
tag.clear()

time.sleep(3)
driver.close()


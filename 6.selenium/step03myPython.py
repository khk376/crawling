from selenium import webdriver
import time

#step 01 : 네이버 사이트 실행하기
driver=webdriver.Chrome("c:/driver/chromedriver.exe")
URL="http://127.0.0.1:5500/6.selenium/step03myHtml.html"
driver.get(URL)

# 검색어 입력될 곳의 태그
tag=driver.find_element_by_id("btn")
tag.clear()

time.sleep(3)
driver.close()


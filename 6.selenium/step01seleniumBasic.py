from selenium import webdriver
import time

#step 01 : 네이버 사이트 실행하기
driver=webdriver.Chrome("c:/driver/chromedriver.exe")
driver.get("https://www.naver.com/")
tag=driver.find_element_by_name("query")
tag.clear()
tag.send_keys("오늘 날씨 어때")
tag.submit()

time.sleep(30)
driver.close()


from selenium import webdriver
import time

#step 01 : 네이버 사이트 실행하기
driver=webdriver.Chrome("c:/driver/chromedriver.exe")
URL="https://www.daum.net"
driver.get(URL)

# 검색어 입력될 곳의 태그
tag=driver.find_element_by_name("q")
tag.clear()

# 검색어 입력
tag.send_keys("모델 루카")

# 검색(enter)
tag.submit()

time.sleep(10)
driver.close()



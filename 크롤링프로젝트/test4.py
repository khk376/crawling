# danawa.py

import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver # selenium은 webdriver api를 통해 브라우저를 제어함
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

main_url = 'http://www.danawa.com/'
keyword =input("제품명 입력: ")
driver=webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)

driver.implicitly_wait(10)

# 입력란 찾기 #AKCSearch # id인지, name 인지 ㅎㅎㅎ 
search=driver.find_element_by_id("AKCSearch")
search.clear()
search.send_keys(keyword)
#search.send_keys(Keys.RETURN)
# search.submit()

# 검색 버튼 클릭
btn_search = driver.find_element_by_css_selector("button.btn_search_submit")
btn_search.click()

# driver.find_element_by_css_selector("flights-search-controls-root > div > div > form > div:nth-child(3) > button").click()

'''
try:
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "oTravelBox"))
    )
except Exception as e:
    print("검색 page 로드시 class 속성이 oTravelBox를 얻으려는 중 예외 발생 : ", e)
'''
# 목록 더보기 스크롤링 
# driver.find_element_by_css_selector("div.oTravelBox > ul > li.moreBtnWrap > button").click()
# 
#    <a href="#" onclick="getPage(1); return false;" class="snum now_spage click_log_page">1</a>

'''
가격 설정 : 200,000 ~ 500,000원
추천순 max
1~3 페이지의 기본 정보 가져오기 : 이미지, 가격, 상품명 등
'''
# 최소 가격 설정
minVal=int(input("시작가 :"))
maxVal=int(input("한도가 :"))
minPrice=driver.find_element_by_id("priceRangeMinPrice")
minPrice.clear()
minPrice.send_keys(minVal)


# 최대 가격 설정
maxPrice=driver.find_element_by_id("priceRangeMaxPrice")
maxPrice.clear()
maxPrice.send_keys(maxVal)

price_search = driver.find_element_by_css_selector("button.btn_search")
price_search.click()

try:
    
    for page in range(1, 2):
        driver.execute_script("getPage(%s); return false;" % page)

        
        time.sleep(3)
     
        print("%s 페이지로 이동!!!" % page)


        soup = BeautifulSoup(driver.page_source, "lxml" ) 

        ppItems = soup.select("div.prod_pricelist")
        

        for data in ppItems: 
            proPrice = data.select("p a")[0].text
            print('가격 :', proPrice)
        

except Exception as e:
    print("---페이지 파싱 에러", e)
    # finally:
    time.sleep(3)
    #driver.close()
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

main_url = "http://www.danawa.com/"
keyword = "맥북 에어"

driver = webdriver.Chrome("C:/driver/chromedriver.exe")
driver.get(main_url)
driver.implicitly_wait(10) # seconds

elem = driver.find_element_by_id("AKCSearch")
elem.clear()
elem.send_keys(keyword)
elem.send_keys(Keys.RETURN)

time.sleep(3)

driver.implicitly_wait(10)
btn_search = driver.find_element_by_css_selector('div > p > a')
btn_search.click()

btn = driver.find_element_by_id('#bookmark_product_information_item')
btn.click()  
#time.sleep(2)

driver.implicitly_wait(10) # seconds

#step04tourCrawler.py

'''
학습 방법
1. http://tour.interpark.com/ 사이트에서 '파리' 검색해 보기
2. 소스 실행후 분석하기
3. 정규 표현식을 반영해 보기
    - 팀단위로 하나만이라도 수정후에 제출
    C:\0.ITStudy\99.제출폴더\10.crawling\181203_정규표현식으로변환해보기
'''

try:
    for page in range(1, 6):
        print("============================== ", page)
        soup = BeautifulSoup(driver.page_source, "lxml" )

        boxItems = soup.select(".panelZone > .oTravelBox > .boxList > .boxItem")
        
        # print(boxItems)
        for boxItem in boxItems:           
            
            proTitle = boxItem.find("img")['alt']

            print("상품명=", proTitle)

except Exception as e:
    print("페이지 파싱 에러", e)
finally:
    time.sleep(3)
    driver.close()

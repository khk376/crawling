from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:\\/0.ITstudy/0.sw/chromedriver')
#driver.implicitly_wait(3)
URL = "https://www.skyscanner.co.kr/?" 


#드라이버 들어간 url 데이터를 가져오고
driver.get(URL)

# 목적지선택 및 입력
search=driver.find_element_by_name("destination-fsc-search")
time.sleep(3)
search.send_keys("오사카") #목적지명 입력
time.sleep(2)
search.send_keys(Keys.RETURN) # 첫번째 항목 선택
time.sleep(2)
#elem = driver.find_element_by_id("searchboxinput")
#elem.send_keys(SEARCH)
#path = driver.find_element_by_id("bpk-button-2YQI1 bpk-button--large-1Z1P5 SubmitButton-WxCV2")
path = driver.find_element_by_xpath('//*[@id="flights-search-controls-root"]/div/div/form/div[3]/button')
time.sleep(1)
path.click()
time.sleep(10)
path2 = driver.find_element_by_xpath('//*[@id="fqs-tabs"]/table/tbody/tr/td[2]')
path2.click()
'''
#그 페이지가 html xml인지뭔지 모르니끼 우리가 알아보기 쉽게
#html이라고 변수이름을 지정하고 .pagesourse가 크롬에서 검사 누르면 나오는
#모든 텍스트를 가져온거
html = driver.page_source
#print(html) 

#1차 정제
soup = BeautifulSoup(html, 'html.parser')


print("**************************************")
print("***2차정제- 원하는 태그만가져오기*****")
print("**************************************")
#2차 정제 원하는 태그만 가져오기 ex) 제목만 가져오기:title
result=soup.select('title')
print(result)'''
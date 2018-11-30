from bs4 import BeautifulSoup
from selenium import webdriver
import time
## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome('C:\\/0.ITstudy/0.sw/chromedriver')
#driver.implicitly_wait(3)
URL = "https://www.google.co.kr/maps" 


#드라이버 들어간 url 데이터를 가져오고
driver.get(URL)

search=driver.find_element_by_name("q")
search.send_keys("솔샘역")
search.submit()
#elem = driver.find_element_by_id("searchboxinput")
#elem.send_keys(SEARCH)
time.sleep(3)
path = driver.find_element_by_id("gb_70")
path.click()
time.sleep(3)

#id2=driver.find_element_by_name("#identifierId")
#id2.send_keys("hkkim376")

path2 = driver.find_element_by_id("RveJvd snByac")
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
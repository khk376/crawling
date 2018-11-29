'''
step01 단계 확장하기
- 향후 완결 로직 : main page에서 소개하는 모든 책들의 상세 page의 목차 스크래핑
- 권장 구조
    1. 로직별 개별 함수로 개발 권장
    2. 다수의 page를 스크래핑 해야 하는 관계로
        - 연속적인 크롤링. 따라서 세션이라는 객체가 필요
- 사고력 기르기  Session
    1. 연속적인 다수의 page 크롤링시 세션(Session)을 사용하는 사유?
        - 연결 유지
        - 서버의 리소스 자원을 절약할수 있게 하는 매너있는 자세

- 주요 API
    lxml.html : tree 기반의 html 문서를 다룰 수 있게 지원해주는 api

- 개발 방식
    1. process
        세션 객체 생성 -> 크롤링 -> lxml을 사용하여 html에서 데이터 추출
    2. 코드
        request.Session()
        get
        lxml.html.fromstring()

- 용어 정리
1. 세션
    - 로그인~로그아웃 할때까지 어떤 user인지 구분, 관리 - 상태유지
    - 상태 유지 기술
    - 세션 처리를 가장 예민 하게 관리 : 단연코 금융
2. 

'''
import requests
import lxml.html
import re
import time

def main():
    session = requests.Session()
    response = session.get("http://www.hanbit.co.kr/store/books/new_book_list.html")
    urls = scrape_list_page(response)

    for url in urls:
        time.sleep(1)
        response=session.get(url)
        bookINFO=scrape_detail_page(response)
        print(bookINFO)
        break

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('#container > div.new_book_list_wrap > div.sub_book_list_area > li:nth-child(1) > div > div > p.book_tit > a'):
        url = a.get('href')
        print("**1")
        yield url 


#상세 page에서 목차 정보 스크래핑 하는 함수
def scrape_detail_page(response):
    root = lxml.html.fromstring(response.content)
    bookINFO= {
        'url' : response.url,
        'title': root.cssselect(".store_product_info_box > h3")[0].text_content(),
        'price' : root.cssselect(".pbr del")[0].text_content(),
        'content' : [normalize_space(p.text_content()) for p in root.cssselect("#tabs_3 .hanbit_edit_view p")
                                        if normalize_space(p.text_content()) != '']
    }
    return bookINFO

'''
1.문자열 앞뒤에 잉여 여백 제거 : strip()
2. '' 무의미한 문자열 데이터 제거
    : if 조건식으로 필터링
        if(p.text_content()!='')
3. 문자열들 사이에 다수의 의미없는 여백이 존재할 경우 하나의 여백으로 가공 
    : re.sub(수정하고자하는 표현식, 변경할 표현식, 데이터)
      re.sub('\s+', ' ', 데이터)
'''

def normalize_space(s):
    return re.sub(r'\s+',' ',s).strip()

'''
    상세 정보는 dict 구조로 가공하기
    key - url, title, price, content(목차)
    value = cssselect()
                이 함수의 반환타입은 list
'''


if __name__ == "__main__":
    main()



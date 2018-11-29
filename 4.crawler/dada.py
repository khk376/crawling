'''
step01 단계 확장하기
- 향후 완결 로직 : main page에서 소개하는 모든 책들의 상세 page의 목차 스크래핑
- 권장 구조
    1. 로직별 개별 함수로 개발 권장
    2. 다수의 page를 스크래핑 해야 하는 관계로
        - 연속적인 크롤링. 따라서 세션이라는 객체가 필요
- 사고력 기르기
    1. 연속적인 다수의 page 크롤링시 세션을 사용하는 사유?
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

def main():
    session = requests.Session()
    response=session.get("http://www.hanbit.co.kr/store/books/new_book_list.html")
    urls=scrape_list_page(response)

    for url in urls:
        print(url)

def scrape_list_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    for a in root.cssselect('.view_box .book_tit a'):
        url = a.get('href')
        print("**1")
        yield url 

if __name__ == "__main__":
    main()
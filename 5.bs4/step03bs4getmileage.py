'''
1. 로직
    - 한빛사이트에서 로그인 후(상태 유지) user의 마일리지 점수 스크래핑

2. 필요한 url
    1. 필요한 url 갯수?
        1. 로그인 화면            
            http://www.hanbit.co.kr/member/login.html

        2. mileage
            -로그인 된 상태여야만 함
            http://www.hanbit.co.kr/myhanbit/myhanbit.html

    2. url
3. request API에는 다수의 요청을 유지하기 위한 세션 API 지원
'''
import requests
from bs4 import BeautifulSoup

user='machine'
upass='machine7'

session = requests.session()
login_info = {'m_id':user, 'm_passwd':upass}

# 로그인 입력 화면 skip 하고 입력된 데이터 값으로 바로 서버 프로그램 요청
# id/pw 값은 보안을 고려해서 서버에 전송 : post방식
# 검색어 처럼 브라우저 주소줄에 오픈되면서 서버에 전송: get방식

url_login='http://www.hanbit.co.kr/member/login.html'
#http 통신 규약인 post 즉 서버에 전송하는 데이터가 은닉되어 전송 및 요청
res=session.post(url_login, data=login_info)
res.raise_for_status()

print("로그인 정상")

url_mypage="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res=session.get(url_mypage)

# soup을 사용해서 마일리지 가져와서 출력해보기
soup = BeautifulSoup(res.text, "html.parser")
mileage=soup.select_one(".mileage_section1 span").string
ecoin = soup.select_one(".mileage_section2 span").string

print(mileage, '--',ecoin)

session.close()
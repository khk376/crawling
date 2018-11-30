'''
1. 로직
    - 한빛사이트에서 로그인 후 (상태유지) user의 마일리지 점수 스크래핑

2. 필요한 url
    1) 필요한 url 개수?
        - 로그인화면 
            http://www.hanbit.co.kr/member/login.html
            id/pw 필요한 정보
                -id값/pw값 구분해서 전송
                유효 : 진행
                무효 : 예외 발생
        - mileage
            로그인 된 상태여야만 함
            http://www.hanbit.co.kr/myhanbit/myhanbit.html
    2) url
3. requests API에는 다수의 요청을 유지하기 위한 세션 API 지원
'''

import requests
from bs4 import BeautifulSoup

user = 'encore7276'
password = 'encore7276'

session = requests.session()
login_info = {"m_id" : user,"m_passwd" : password}

# 로그인 입력 화면 skip하고 입력된 데이터 값으로 바로 서버 프로그램 요청
# id/pw값은 보안을 고려해서 서버에 전송 : post방식
# 검색어처럼 브라우저 주소줄에 오픈되면서 서버에 전송 : get방식
url_login = 'http://www.hanbit.co.kr/member/login_proc.php'

# http 통신 규약인 post 즉 서버에 전송하는 데이터가 은닉되어 전송 및 요청
res = session.post(url_login, data=login_info)

# 마이페이지에 접근하기
url_mypage ="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)

# soup 사용해서 마일리지, 이코인 가져와서 출력해보기
soup = BeautifulSoup(res.text, "html.parser")
print("마일리지 :", soup.select_one(".mileage_section1 span").string)
print("이코인 :", soup.select_one(".mileage_section2 span").string)

session.close()
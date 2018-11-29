#첫화면
#http://www.hanbit.co.kr/store/books/new_book_list.html

#해당 서적의 상세 page
#http://www.hanbit.co.kr/store/books/look.php?p_code=B2417558084

#해당 서적의 목차
#http://www.hanbit.co.kr/store/books/look.php?p_code=B2417558084
'''
<a href="javascript:;" class="ui-tabs-anchor" role="presentation" tabindex="-1" id="ui-id-5">저자소개</a>

<a href="javascript:;" class="ui-tabs-anchor" role="presentation" tabindex="-1" id="ui-id-7">목차</a>
'''

'''
1. 주제: 새로나온 책들의 전체 리스트 화면에서
책 마다의 상세 페이지에 존재하는 목차 부분만 스크래핑 하기
2. url 변천사
3. 화면에서 확인해야 할 항목
    1. 각 book별 상세 url값 확인
        <a href="상대경로값">
    2. 상세보기 화면상에서
'''
# 추가 설정: pip install cssselect

# 새로나온 책 화면에서 서적별 링크 url값 스크래핑
# 퍼머링크 출력하기

import requests
import lxml.html

response=requests.get("http://www.hanbit.co.kr/store/books/new_book_list.html")
#print(response) #<Response [200]>
root = lxml.html.fromstring(response.content)
#html도 tree구조. 즉 족보 형태(조상, 부모, 자식 관계를 표현)
#최상위 root = html tag(element)
#tag용어는 element라고도 함
#html tag 최상위 tag, 자식 자손 모두 다 관리 가능한 지존!!
#print(root) #<Element html at 0x20db5287bd8>

#크롤링한 문서 내용
# print(response.content)

root.make_links_absolute(response.url) #먼저 절대url로 전부 바꾼뒤 for문으로 돌려서 출력

for a in root.cssselect('.view_box .book_tit a'):
    url = a.get('href')
    print(url)

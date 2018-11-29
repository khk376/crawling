
import requests
import lxml.html

response=requests.get("http://www.hanbit.co.kr/store/books/new_book_list.html")
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
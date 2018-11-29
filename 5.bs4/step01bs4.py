from bs4 import BeautifulSoup

#        <div>                           # 대규모 영역을 논리적으로 나눔

html = '''
<html> # 최상위 구조
    <body>
        <h1>스크래핑이란?</h1>
            <p id = "one">웹페이지1</p>
            <p id = "two">웹페이지2</p>
        <span class = "redColor">                  #소규모 영역
            <p>웹페이지3</p>
        </span>
        <ui>
            <li> <a href = "www.naver.com 네이버> </li>
            <li> <b href = "www.daum.net 다음> </li>
        </ui>      
    </body>
</html>
'''

# 크롤링한 데이터와 사용할 parse로 객체 생성

            # 필수
soup = BeautifulSoup(html, "html.parser")
#print(soup.html)
            # 필수

print('=============step04 : 미션===============')
# select * 관련 함수 중에 list 반환이 아닌 단수 형태의 요소를 반환하는 함수
# <p id="two"> 웹페이지2 </p> 검색 및 text값 출력

print(soup.select_one('#two'))   # <p id="two">웹페이지2</p>
print(soup.select_one('#two').string)   # 웹페이지2    /    .select_one으로 가져왔기 때문에 list 인덱싱 안해도 됨
print(soup.select('#two')[0].string)    # 웹페이지2    /    .select으로 가져왔기 때문에 list 인덱싱 해야 함




'''
print('=============step03 : a 앵커[하이퍼링크, 링크] tag의 href 속성값 및 text===============')
links = soup.find_all("a")
print(links)
for a in links:
    href = a.attrs['href']
    text = a.string
    print("***", href, "---", text)
'''


'''
print('=============step02 : find() 함수===============')
print(soup.find(id="one"))
print(soup.find(id="one").string)

print('=============span을 class값으로 접근해 출력=============')
print(soup.select('.redColor'))

print('=============span을 class값으로 접근하되 p객체 내 값만 출력=============')
print(soup.select('.redColor')[0].string)   # 왜 None값?????????
'''

'''
select() : css selector 사용 가능한  API
         : 반환타입 list
         : 사용시 index값으로 개별 사용 가능

'''

'''
print("===========step01 - .접근자로 계층 구조에 맞게 검색============")
    # text 데이터 : string/get_text() / string(해당 tag의 하위 자식 문자열인 경우에만 해당) / get_text()
print(soup.html)
print('=============================')
print(soup.html.h1)
print('=============================')
#print(type(soup.html))     <class 'bs4.element.Tag'>  클래스 타입인 걸 확인
#print(soup.html.p[1])      => 리스트 타입이 아니라 오류!!
#print('-', soup.html.next_sibling.next_sibling.next_sibling.next_sibling,  '-')

print(soup.html.span.p)   #<p>웹페이지3</p>
print(soup.html.span.p.sting)
'''









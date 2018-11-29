# 알라딘, 위키북스

import requests
import lxml.html
import re
import time

def main():
    session = requests.Session()
    response = session.get("https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1")
    urls = page_list(response)
  
    for url in urls:
        response=session.get(url)
        bookINFO=page_detail(response)
        print(bookINFO)
        

def page_list(response):
    root = lxml.html.fromstring(response.text)
    #root.make_links_absolute(response.url)
    count=0
    for a in root.cssselect('a.bo3'):
        url = a.get('href')
        print("**1")
        yield url
        count+=1
        print(count)


def page_detail(response):
    root = lxml.html.fromstring(response.text)
    bookINFO= {
        'url' : response.url,
        'title': root.cssselect(".pwrap_bgtit a")[0].text_content(),
        'price' : root.cssselect("tr:nth-child(1) > td.p_goodstd02")[0].text_content()
        #'content' : [normalize_space(p.text_content()) for p in root.cssselect("#tabs_3 .hanbit_edit_view p")
        #                                if normalize_space(p.text_content()) != '']
    }
    return bookINFO

def normalize_space(s):
    return re.sub(r'\s+',' ',s).strip()

if __name__ == "__main__":
    main()



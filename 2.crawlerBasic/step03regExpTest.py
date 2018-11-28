
import re

def reUse():   
    # test data - http://www.hanbit.co.kr에서 발췌한 tag 구조
    data = '<td class="left"><a href="/store/books/look.php?p_code=B7198274060">book info</a></td>'


    #data 변수의 데이터에서 /store/books/look.php?p_code=B7198274060  
    d1 = re.search(r"(/.+\d)", data).group(1)
    print(d1) 
    

    #data 변수의 데이터에서 book_info만 뽑아내기
    #d2 = re.sub(r">\w+\s\w+",'book_info',data)
    #print(d2) 
    d2=re.sub(r"\w{4}\s\w{4}",'book_info',data)
    print(d2)
    d4=re.sub(r"<.*?>","",data) #d4=d2
    print(d4)

    #B7198274060
    d3 = re.search(r"(\w\d+)",data).group(1)
    print(d3) 
    d5=re.search(r'p_code=(.*)(")',data).group(1) #d5=d3
    print(d5)

    
#최상위 스크립트 환경
if __name__=="__main__":   
    reUse()

'''
정규식이 a.b인 경우 문자열 a\nb는 매치되지 않음
왜냐하면 \n은 . 메타 문자와 매치되지 않기 때문
\n 문자와도 매치되게 re.DOTALL 옵션을 사용
'''


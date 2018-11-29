

def generator(n):
    i=0
    while i<n:
        print("1##")
        i +=1
        print("2##")
#for x in generator(5):   =>generator는 반환값이 없기때문에 오류 발생!
#    print("-----", x)
generator(5) #이케 바꿔주야함!
print("**************")
'''
23->16->17-18-19-20(데이터 반환)->23-24->21-22-18-19-20->23->24-21-22->18->19
'''
def yieldGenerator(n):
    i=0
    while i < n:
        print("1 ###")
        yield i
        i+=1
        print("2 ###")
for x in yieldGenerator(5):
    print("-----", x)

'''
1. 모든 지역에 거주하는 대상 가구수의 합
2. 가구당 평균 전력사용량의 총 평균
3. 가구당 평균 전기요금의 합
'''
import csv

newhouse = []
newVolt = []
newPay = []
with open("지역별 전기요금 정보(2017.05).csv", "r") as f:
    csv_reader = csv.reader(f) # csv.reader파일객체에 파일 저장
    
    
    for row in csv_reader: #2~4열의 공백과 콤마를 지우고 한줄씩 리스트에 추가
        print('/'+row[1]+'/')
        newhouse.append(row[1].strip().replace(",","")) 
        newVolt.append(row[2].strip().replace(",",""))
        newPay.append(row[3].strip().replace(",",""))


def Sum(sumList): #사용자 정의함수 Sum
    sum = 0
    for i in range(1,len(sumList)):#2번째행부터 sumList의 길이만큼
        if(sumList[i]!=""): # 공백이 나오면 pass
            sum = int(sum + int(sumList[i])) # 변수sum에 한줄씩 더하며 적재
        else:
            pass
    return (sum) 


def Avg(avgObject): #사용자 정의함수 Avg
    count = 0
    for i in range(1,len(avgObject)): #2번째행부터 avgObejct의 길이만큼
        if(avgObject[i]!=""): # 공백이 나오면 pass
            count +=1 #공백 전까지 갯수 하나씩 카운트+1
    
    return (Sum(avgObject)/count) # (총합/카운트 = 평균) 리턴



print(Sum(newhouse))
print(Sum(newPay))
print(Avg(newVolt))
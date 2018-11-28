#미션1 - 모든 지역에 거주하는 대상 가구수의 합
#미션2 - 가구당 평균 전력사용량의 총 평균
#미션3 - 가구당 평균 전기요금의 합
import csv

with open("지역별 전기요금 정보(2017.05).csv", "r", newline='', encoding="utf-8-sig") as f:
    #history.csv 파일로 csv 작성 가능한 객체화
    #writer 변수로 호출하는 함수는 csv 파일로 작성 가능한 기능
    rdr = csv.reader(f)
    first = []
    i = 0
    fsum = 0
    wsum = 0
    asum = 0

    for line in rdr: # line = list
        list1 = []
        if i == 0 :
            i+=1
            continue
            
        if i == 18 :
            break

        fsum += int(line[1].replace(",","").replace(" ",""))
        print(fsum)

        asum += int(line[2].replace(",","").replace(" ",""))
        print(asum)

        wsum += int(line[3].replace(",","").replace(" ",""))

        list1 = [line[0],line[1].replace(",","").replace(" ",""),line[2].replace(",","").replace(" ",""),line[3].replace(",","").replace(" ","")]
        first.append(list1)
        i+=1

    print(first)
    print("모든 지역에 거주하는 대상 가구수의 합: ", fsum, "호")
    print("가구당 평균 전력사용량의 총 평균: ", asum/len(first), "kWh")
    print("가구당 평균 전기요금의 합: ", wsum, "원")

    


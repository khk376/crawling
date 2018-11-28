import csv

newhouse=[]
newvolt=[]
newpay=[]

with open("지역별 전기요금 정보(2017.05).csv", "r") as f:
    csv_reader=csv.reader(f)

    for row in csv_reader:
        
        newhouse.append(row[1].strip().replace(",",""))
        newvolt.append(row[2].strip().replace(",",""))
        newpay.append(row[3].strip().replace(",",""))


def Sum(sumList):
    sum=0
    for i in range(1, len(sumList)):
        if(sumList[i]!=""):
            sum=sum+sumListp[i]
        else:
            pass
    return (sum)

def Avg(avgobject):
    count = 0
    for i in range(1, len(avgobject)):
        if(avgobject[i]!=""):
            count +=1
    return (Sum(avgobject)/count)

print(Sum(newhouse))
print(Sum(newpay))
print(Avg(newvolt))
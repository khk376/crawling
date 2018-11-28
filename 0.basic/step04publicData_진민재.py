import csv
with open("C:/0.ITStudy/0.dataset/지역별_전기요금_정보_2017.05_.csv", "r", newline = "") as r:
    reader = csv.reader(r)
    lists = []
    for i in reader:
        lists.append(i)
        
lists =lists[1:len(lists)+1]
print(lists)

lists2 =[]
for list in lists:
    if list[0]:
        lists2.append(list)

print(lists2)

sum_list = []
mean_list = []
fare_list = []
for item in lists2:
    sum_list.append(int(item[1].replace(",","")))
    mean_list.append(int(item[2].replace(",","")))
    fare_list.append(int(item[3].replace(",","")))

sum = 0
mean = 0
fare = 0

for i in sum_list:
    sum += i
for v in mean_list:
    mean += v
for x in fare_list:
    fare += x
    
print("대상 가구수의 합:", " ", sum)
print("가구당 평균 전력 사용량:", " ", mean/len(mean_list))
print("가구당 평균 전기요금의 합:"," " ,fare)
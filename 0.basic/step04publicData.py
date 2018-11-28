import csv
 
total=0
useavg=0
payavg=0

with open('지역별 전기요금 정보(2017.05).csv', 'r') as f:
    read = csv.reader(f)
    for line in read:
    #for line in range(1, len(total)):
        print(line[1])
 #       for col in line:
 #           total += int(col)

    f.close()   

# 미션 1: 모든 지역에 거주하는 대상 가구 수의 합
# 미션 2: 가구당 평균 전력 사용량의 총 평균
# 미션 3: 가구당 평균 전기요금의 합

### csv 파일 읽어오기
import csv

with open("C:\\0.ITStudy\\0.dataSet\\original_electric.csv", newline = '', encoding = "utf-8-sig") as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'{", ".join(row)}')
            line_count += 1
        else:
            print(f'{row[0]} {row[1]} {row[2]} {row[3]}')
            line_count += 1
    print(f'line_count: {line_count}')


### 미션 1: 모든 지역에 거주하는 대상 가구 수의 합

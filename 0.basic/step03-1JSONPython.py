'''
http://www.w3schools.com 예제
https://www.w3schools.com/python/python_json.asp

1. 예제 이해하기

2. 이 데이터를 파일로 저장 - save()

3. 저장된 파일을 다시 read해서 python 데이터로 변환 후 활용(출력) - view()

4. 의도
    - json과 python의 호환 작업 익숙해지기
    - 개별 함수로 개발해서 모듈화 시키는 연습
    - main 사용 필수 : 최상위 실행 스크립트
'''
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

def save():
    with open("example.json", "w", encoding="utf-8-sig") as f:
        # list 데이터를 파일에 json 형태의 문자열로 출력
        json.dump(x ,fp=f, ensure_ascii=False)

def view():
    with open("example.json", "r", encoding="utf-8-sig") as f1:
        pythonData = json.load(f1)
        return pythonData
        

print("### json 파일을 python파일로 변환하기")
jsonData = json.dumps(x, ensure_ascii=False)
print(jsonData)
save()
print("\n")

print("### json 파일을 python파일로 변환하기")
view()
print(type(view()))

for key, value in view().items():
    print(key,value)
print(view()["cars"][0]["model"])
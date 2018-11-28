'''
이기종 간에 호환되는 포멧인 JSON타입으로 변환하는 작업
JSON 사용 사유
    : 값 구분이 명확
    : 기기에 종속적이지 않음
    : 모든 언어가 호환되는 포멧
    : csv보다 더 효율적인 사유?
        ->고유한 key로 데이터 구분
    : 서버로 부터 대량의 데이터를 client가 JSON 포멧으로 많이 받아서 사용
    : MongoDB의 데이터 저장 포멧
        - json 형태의 문자열
API
    1. python의 list를 Json 형태(객체)로 변환 : dumps()
    2. json의 데이터를 python의 데이터로 변환: loads()

실습단계
    1. 모듈 import
    2. test 데이터 구성
    3. json 객체로 변환

고려사항
    1. 한글 데이터 보호(인코딩)
'''
import json

friends=[{'f1':1, 'name':'황윤후'},
        {'f1':2, 'name':'이해인'},
        {'f1':3, 'name':'김혜경'}]
print(friends[2]['name'])
print(friends)
#시도1.
print("### list를 json 객체로 변환해 보기")
#jsonData = json.dumps(friends)#-> 유니코드로 출력됨. 아스키 추가해줘야해
jsonData = json.dumps(friends, ensure_ascii=False)
print(jsonData)

#시도2. indent값 추가
print("### list를 json 객체로 변환해 보기")
#jsonData = json.dumps(friends)#-> 유니코드로 출력됨. 아스키 추가해줘야해
jsonData = json.dumps(friends, ensure_ascii=False, indent=2)
print(jsonData)

print("###타입 비교###")
print(type(friends))
print(type(jsonData))

print("### json 확장자 파일로 생성")
with open("friends.json", "w", encoding="utf-8-sig") as f:
    # list 데이터를 파일에 json 
    json.dump(friends, fp=f, ensure_ascii=False)
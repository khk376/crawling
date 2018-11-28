from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# userdatabase라는 이름의 database 생성
#db = client.userdatabase

# mydb라는 collection 생성
#collection = db.mydb

# database명 반환
databaseName = client.get_database('userdatabase')
print(1, ' : ', databaseName)

# table 즉 collection 명 반환
collectionName = databaseName.get_collection('mydb')
print(2, ' : ', collectionName)

# collection list
collectionList = databaseName.collection_names()
print(3, ' : ', collectionList)

# insert
# 실행시마다 고유한 _id값이 자동 반영되면서 실행한 수 만큼 저장됨
collectionName.insert({"no" : 1, "name" : "정약용" })


# 전체조회
resultAll = collectionName.find()
print("### 전체 조회 ###")
for result in resultAll:
    print(result)

print("### 조건별 조회 ###")
results = collectionName.find({"no" : 1})
for result in results:
    print(result)

# update
'''
* 속성
update({업데이트를 위해 선택할 key-value}, {수정한 내용의 key-value}, upsert=True)
    - 업데이트, 만일 업데이터 할 데이터가 미 존재할 경우 insert 의미

update({업데이트를 위해 선택할 key-value}, {수정한 내용의 key-value}, upsert=True, multi=True)
    - 업데이트, 만일 업데이터 할 데이터가 여러개인 경우 모두 다 업데이트
'''
collectionName.update({"no":1}, {"no":1, "name":"허준"}, upsert=True)
result = collectionName.find_one({"no":1})
print("\n수정 후 --- ", result)

# 데이터 삭제
collectionName.remove({"no":1})

# 전체조회
resultAll = collectionName.find()
print("### remove() 함수로 삭제후 삭제 후 전체 조회 ###")
for result in resultAll:
    print(result)

# 데이터 삭제
deleteData = { "name": "허준" }
collectionName.delete_one(deleteData)

# 전체조회
resultAll = collectionName.find()
print("### delete_one() 함수로 삭제후 전체 조회 ###")
for result in resultAll:
    print(result)

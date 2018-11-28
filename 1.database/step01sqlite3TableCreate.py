'''
sqlite3을 사용법 습득을 위한 예제
'''


#https://sqlite.org/cli.html
#https://docs.python.org/ko/3.6/library/sqlite3.html

import sqlite3

# 데이터베이스 연결
filepath = "encore.sqlite"
conn = sqlite3.connect(filepath)

# 테이블 생성
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS books") 
cur.executescript("""CREATE TABLE books (
    key text primary key,
    title    text,   
    content text)""")

# 모든 데이터 저장
#cur.execute('insert into books values("002", "data2", "data 이해하기")')

# 동적 데이터
value = ("003", "data3", "data3 이해하기")
cur.execute('insert into books values(?, ?, ?)', value)

conn.commit()

# 모든 데이터 검색 - fetchall()
cur.execute("select * from books")
print("### 모든 검색 ###")
for data in cur.fetchall():
    print(data)

# 특정 데이터 하나만 검색 - fetchone()
cur.execute("select * from books where key='003'")
print("### 특정 데이터만 검색 ###")
data = cur.fetchone()
print(data)

conn.close()
# pip install google-api-python-client
# https://developers.google.com/youtube/v3/getting-started?hl=ko

import os
from apiclient.discovery import build 


# 환경변수에서 API 키 추출하기 -  11월 17일에 신청한 API 키
YOUTUBE_API_KEY = 'AIzaSyDQDnbyE2yfvjJU_fD9mUKOp6le_ICbM3c'

# YouTube API 클라이언트를 생성
# build() 함수의 첫 번째 매개변수에는 API 이름
# 두 번째 매개변수에는 API 버전을 지정
# # 키워드 매개변수 developerKey에는 API 키를 지정
# 이 함수는 내부적으로 https://www.googleapis.com/discovery/v1/apis/youtube/v3/rest 라는
# URL에 접근하고 API 리소스와 메서드 정보를 추출
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# 키워드 매개변수로 매개변수를 지정하고
# search.list 메서드를 호출
# list() 메서드를 실행하면 googleapiclient.http.HttpRequest가 반환 
# execute() 메서드를 실행하면 실제 HTTP 요청이 보내지며, API 응답이 반환

# snippet : 재사용 가능한 소스 코드, 기계어,
#           텍스트의 작은 부분을 일컫는 프로그래밍 용어
search_response = youtube.search().list(
    part='snippet',
    q='요리',
    type='video',
).execute()   

print(1, " - ", type(search_response))
print(2, " - ", search_response)

print("###############################################")
# search_response는 API 응답을 JSON으로 나타낸 dict 객체
for item in search_response['items']:
    # 동영상 제목을 출력
    print(item['snippet']['title'])
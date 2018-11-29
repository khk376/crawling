import os
from apiclient.discovery import build

youtube_api_key='AIzaSyDqmhR0RzfqfMso5fME2er0u_JEMlhjcYY'
youtube=build('youtube', 'v3', developerKey=youtube_api_key)


# snippet : 재사용 가능한 소스 코드, 기계어, 텍스트의 작은 부분을 일컫는 프로그래밍 용어
result= youtube.search().list(
    part='snippet',
    q='요리',
    type='video'
).execute()

print(result)
for item in result['items']:
    print(item['snippet']['title'])
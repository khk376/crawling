# 1. pip install google-api-python-client
import os
from apiclient.discovery import build

youtube = build("youtube", "v3", developerKey="AIzaSyDqmhR0RzfqfMso5fME2er0u_JEMlhjcYY")

search_response = youtube.search().list(
    q='크롤링',
    part="snippet",
    type = 'video'
).execute()
#print(search_response)


video = []

for item in search_response["items"]:
    video.append(item['snippet']['title'])

print(video)
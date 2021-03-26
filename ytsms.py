from twilio.rest import Client 
import urllib
import re
import random
from googleapiclient.discovery import build
from wonderwords import RandomWord

yt_developer_key = ''
yt_api_service_name = 'youtube'
yt_api_version = 'v3'
twilio_account_sid = ""
twilio_auth_token = ""
twilio_sms_number = '+15555555555'
twilio_sms_body_name = "cool person"
affix = " meme "
r = RandomWord()
rob = r.word(include_parts_of_speech=["nouns"])
num_results=random.randrange(1,50)

choices = [ 
'beetle juice',
'beetlejuice',
'oblivion npc',
'npc oblivion',
'morrowind npc',
'npc conversation',
'npc dialogue',
'bernie sanders',
'joe biden',
'donald trump',
'npc',
'bill clinton',
'oblivion',
'karen'
]


def youtube_search():
  youtube = build(yt_api_service_name, yt_api_version, developerKey=yt_developer_key)

  search_response = youtube.search().list(
    q=random.choice(choices) + str(affix) + str(rob),
    part='snippet',
    maxResults=num_results
  ).execute()

  videos = []

  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s' % (search_result['id']['videoId']))
  videos_random = random.choice(videos)
  return (videos_random)

client = Client(twilio_account_sid, twilio_auth_token)

message = client.messages \
                .create(
                     body="Hello "+ twilio_sms_body_name + ", welcome to rick's friendly python messaging service, enjoy the following video!\r\r\n"+"https://www.youtube.com/watch?v="+youtube_search(),
                     messaging_service_sid='TWILIO_MESSAGING_SERVICE_SID',
                     to=twilio_sms_number
                 )

print(message.sid)

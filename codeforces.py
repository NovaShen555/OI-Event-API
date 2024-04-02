import requests
import json

url = 'https://codeforces.com/api/contest.list'
requests = requests.get(url)
data = json.loads(requests.text)
data = data['result']

for i in data:
    print(str(i['id']) + " " + i['name'])
    print("start:"+str(i['startTimeSeconds'])+" end:"+str(i['startTimeSeconds']+i['durationSeconds']))

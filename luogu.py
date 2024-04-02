import json
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup


url = 'https://www.luogu.com.cn/contest/list'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36 Edg/123.0.0.0'
}
response = requests.get(url, headers=headers, timeout = 5)
soup = BeautifulSoup(response.text, 'html.parser')
res = soup.script.get_text()
res = unquote(res.split('\"')[1])

data = json.loads(res)
data = data['currentData']['contests']['result']
for i in data:
    print(str(i['id'])+" "+i['name'])
    print("start:"+str(i['startTime'])+" end:"+str(i['endTime']))

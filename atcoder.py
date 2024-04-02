from lxml import etree

import requests

from datetime import datetime


def convert_to_timestamp(time_str):
    # 转换为datetime对象，注意时区的处理
    dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S%z")
    # 转换为时间戳
    return int(dt.timestamp())


def convert_to_second(time_str):
    hours, minutes = map(int, time_str.split(':'))
    # 将小时和分钟转换为秒
    return (hours * 60 + minutes) * 60


url = 'https://atcoder.jp/contests/'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 '
                  'Safari/537.36 Edg/123.0.0.0'
}
response = requests.get(url, headers=headers, timeout=5)
element = etree.HTML(response.content.decode('utf-8'))
nodes = element.xpath('//*[@id="contest-table-upcoming"]/div/div/table/tbody/tr')
for node in nodes:
    start_time = convert_to_timestamp(node.xpath('td[1]/a/time')[0].text)
    duration = convert_to_second(node.xpath('td[3]')[0].text)

    print(node.xpath('td[2]/a')[0].text)
    print("start:" + str(start_time) + " end:" + str(start_time + duration))

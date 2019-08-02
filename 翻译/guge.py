import execjs

with open('myguge.js',encoding='utf-8') as f:
    js = f.read()
query = 'hi'
token = execjs.compile(js).call("vo", query,'433927.2762404701')#后者参数为TTK，在源码中
print(token)

import requests
import json
data = {
    'client':'webapp',
    'sl':'auto',
    'tl':'zh-CN',
    'hl':'zh-CN',
    'dt':'at',
    'dt':'bd',
    'dt':'ex',
    'dt':'ld',
    'dt':'md',
    'dt':'qca',
    'dt':'rw',
    'dt':'rm',
    'dt':'ss',
    'dt':'t',
    'otf':'2',
    'ssel':'0',
    'tsel':'0',
    'kc':'1',
    'tk':token,
    'q':query,
}
headers = {
    'authority':'translate.google.cn',
    'method':'GET',
    'scheme':'https',
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'cookie':'NID=187=pIafMff7mdrwSXa0NXODsEtMMqZESXoDalukrLa9KAhgdSuIayIPoUJJucog1sCcsGPudFCcvbhhNuiNm0FGaOfANCxbKbomj63N5HaXnwggiZcdbC5AOuGgD7MheXZoSu0I69PtlT03u04hZPLxOUnYScLLAWo1pBYqFlfX990; _ga=GA1.3.1188730027.1562135084; _gid=GA1.3.548288202.1562135084; 1P_JAR=2019-7-3-6',
    'referer':'https://translate.google.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}
url = 'https://translate.google.cn/translate_a/single?dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss'#如果不带dt=xx一串参数，只返回一部分
res = requests.get(url=url, headers=headers, params=data)
result = res.content.decode('utf-8')
print(result)

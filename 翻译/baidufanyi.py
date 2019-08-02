import execjs

with open('baidu.js',encoding='utf-8') as f:
    js = f.read()
query = 'hi'
sign = execjs.compile(js).call("e", query)
print(sign)

import requests
import json
data = {
    "from": "zh",
    "to": "en",
    "query":query,
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": sign,
    "token": "261d93745136045b7ea6a1badc54a075",
}
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '154',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BAIDUID=BADB5E5D72667C5F54A34848245C74AB:FG=1; BIDUPSID=BADB5E5D72667C5F54A34848245C74AB; PSTM=1534988617; H_WISE_SIDS=124614_125822_108269_124694_125945_114745_123552_125629_120162_125735_118894_118867_118845_118820_118788_107311_125006_124978_117428_125776_125652_124636_124897_124939_125487_125171_125289_125710_125285_124938_124683_124030_110085_123289_125645_125428_125875; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=0N6UHl4VTVQR1k2d0k1YWtMRmRRaTJhLWFpQk1mLWZwS3YxU01UTW0tMEtNaEpjQVFBQUFBJCQAAAAAAAAAAAEAAACrlRIPNDM0ODkwOTc0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAql6lsKpepbS; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1542288873,1542333802,1542365440,1542422410; __cfduid=dde3763f9db2ea63b180aa1372d14e3921542882903; BDSFRCVID=LNuOJeC62mNCkaT90LMd--Y9EeTt9t7TH6aItwTAQU9bjkQNDx7JEG0PfU8g0KubJmOPogKKKgOTHICF_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tR-tVC0-fCI3fP36q4co-4FjbqOH54cXHDOH0Kvzt-55OR5Jj65NW-FtMGtf2j3kyCT-hInH-RF5jDn-3MA--fF1hmcayhjMXbvXQp-2KhTCsq0x0-6le-bQypoa2b-HBIOMahvc5h7xOhIC05C-jTvBDG_eq-JQ2C7WsJjs24ThD6rnhPF3K4rbKP6-3MJO3b7zon6lJbrSSpO_5n3V3tkEKh6tb6oP-N7CohFLtC0BhK0Gj6Rjh-40b2TJK4625CoJsJOOaC7tqR7zKPnhK4t8HfJfhtJfHJue_II5JjuKhI-wjTD_D6J3eHtqqh5gW57Z0lOnMp05jt3uh6J_hKurXpKJ0JQ2aCDfhC5RLKOSVIO_e6LbejOWjHDs5-7ybCPXLn58Kb5_f5rnhPF3yMvDKP6-3MJO3b7JbpTvJbrSOUob-jrl5f63247XtbTwKRnlohFLtD8KMI-GjjRMK4_SMUoHetrK-D5XQbC8Kb7VbTC4LfnkbfJBD4-jXJJC2JvXQpOy5R5lfM7NyUOO5fI7yajK25KHbe5h2h5v3fOASIO63bbpQT8rbfDOK5Oib4j7htOnab3vOpvTXpO1yftzBN5thURB2DkO-4bCWJ5TMl5jDh05y6TXjH-ttTLDJn3fL-082R6oDn8k-PnVePF3LtnZKxtqtDDOBDJ7QI3lDbk6557ZbbDqhRJ8t4TnWncKWho1bIb_MR5cK65IhPrb2HJ405OT2j-O0KJcbRo0Hpb4hPJvyUPsXnO7BxJlXbrtXp7_2J0WStbKy4oTjxL1Db0eBjIHtnFJVI05fCvKeJbYK4oj5KCyMfca5C6JKCOa3RA8Kb7VbpR85fnkbfJBDxcw3-nKQnKj2p6eH66Zbq5N3b8B55-7yajKBR3fQg6I-CTt2JvG8lb9jU6pQT8rbR_OK5OibCrZWl7xab3vOpvTXpO1yftzBN5thURB2DkO-4bCWJ5TMl5jDh05y6ISKx-_J5te3f; MCITY=-%3A; H_PS_PSSID=1438_21081_18559_28019_26350; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=5; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1544166294; from_lang_often=%5B%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
url = 'https://fanyi.baidu.com/v2transapi'
res = requests.post(url=url, headers=headers, data=data)

result = json.loads(res.text).get("trans_result").get('data')[0]
item = dict()
item['source'] = result.get('dst')
print(item)

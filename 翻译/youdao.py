import requests,hashlib,time, random,json
from urllib import parse

def getMD5(v):
    import hashlib
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def getts():
    ts = int(time.time()*1000)
    return str(ts)


def getSalt(ts):
    salt = str(ts) + str(random.randint(0, 10))
    return salt

def getdata():
    client = 'fanyideskweb'
    temp = '@6f#X3=cCuncYssPsuRUE'
    navigator_appVersio = '5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    key = input('需翻译：')

    bv = getMD5(navigator_appVersio)
    ts = getts()
    salt = getSalt(ts)
    sign = getMD5(client+key+salt+temp)

    data = {
        'i':key,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':client,
        'salt':salt,
        'sign':sign,
        'ts':ts,
        'bv':bv,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_REALTlME',
    }
    return data

if __name__ == "__main__":
    data = getdata()
    #对data进行编码，bytes格式
    data = parse.urlencode(data).encode()
    print(len(data))
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": str(len(data)),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=685021846@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=366356259.5731474; _ntes_nnid=1f61e8bddac5e72660c6d06445559ffb,1535033370622; JSESSIONID=aaaVeQTI9KXfqfVBNsXvw; ___rl__test__cookies=1535204044230",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    res = requests.post(url=url,headers=headers,data=data)
    html = res.json()
    print(html)


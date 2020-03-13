import execjs,json,requests,time,re
from urllib.parse import quote

user = "h5oyqb4hwz@chaliivi.fun"  ### 输入账号密码 适用于手机号
pw = "azlmseyw"

'''###非调用js方法
def get_username(user_name):
        #获取账号加密
        username_quote = urllib.parse.quote_plus(user_name)
        username_base64 = base64.b64encode(username_quote.encode("utf-8"))
        return username_base64.decode("utf-8")
    
def get_password(servertime, nonce, pubkey):
        ##密码加密
        string = (str(servertime) + "\t" + str(nonce) + "\n" + str(self.pass_word)).encode("utf-8")
        public_key = rsa.PublicKey(int(pubkey, 16), int("10001", 16))
        password = rsa.encrypt(string, public_key)
        password = binascii.b2a_hex(password)
        return password.decode()
'''
    
with open('wb.js') as f:
    js = f.read()
su = execjs.compile(js).call("getsu", user)
print(su)
burl = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=&rsakt=mod&client=ssologin.js(v1.4.19)&_={}'.format(str(round(time.time() * 1000)))
headers = {
    'scheme':'https',
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9',
    'Content-Type':'application/x-www-form-urlencoded',
    'cookie':'SINAGLOBAL=183.15.176.189_1562202096.905826; UOR=www.baidu.com,tech.sina.com.cn,; U_TRS1=0000007d.790f456f.5d229ce6.1f690140; UM_distinctid=16bcf34e850617-03c1571a29ab81-454c092b-12ae3a-16bcf34e851631; lxlrttp=1560672234; SUB=_2AkMqYhuDf8NxqwJRmfsWyWzka4tzyAvEieKcPupYJRMyHRl-yD83qlEEtRB6AeI1bDmSszSZpW-mK8W4PgjRrNYzcQwr; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W56WQyDn1Z_c0hGhRh5FE.h; vjuids=fd60b7735.16c40c9950d.0.46d03c41749b6; vjlast=1564455048; ArtiFSize=14; ULV=1564642074816:4:1:3:116.24.64.224_1564636997.778002:1564455048071; login=1d5adbc41bf925048a06589ff4d2f3d5; Apache=183.15.178.115_1564712467.226702; ULOGIN_IMG=gz-3d282e51b4ed27139d407dc1e1e5095bda0e',
    'Host':'login.sina.com.cn',
    'Origin':'https://weibo.com',
    'referer':'https://weibo.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

s = requests.session()
resu = s.get(burl).content.decode('gbk')
#print(resu)
resu = resu.split('sinaSSOController.preloginCallBack(')[-1].split(')')[0]
#print(resu)
resu = json.loads(resu)

nonce=resu.get('nonce')
pubkey=resu.get('pubkey')
servertime=resu.get('servertime')
rsakv = resu.get('rsakv')

print('nonce',nonce)
print('pubkey',pubkey)
print('servertime',servertime)
print('rsakv',rsakv)

passw = execjs.compile(js).call("getpassword",pw,pubkey,servertime,nonce)
print(passw)

data = {
    "entry":"weibo",
    "gateway":"1",
    "from":"",
    "savestate":"7",
    "qrcode_flag":"false",
    "useticket":"1",
    "pagerefer":"https://login.sina.com.cn/crossdomain2.php?action=logout&r=https%3A%2F%2Fpassport.weibo.com%2Fwbsso%2Flogout%3Fr%3Dhttps%253A%252F%252Fweibo.com%26returntype%3D1",
    "vsnf":"1",
    "su":su,
    "service":"miniblog",
    "servertime":servertime,
    "nonce":nonce,
    "pwencode":"rsa2",
    "rsakv":rsakv,
    "sp":passw,
    "sr":"1475*830",
    "encoding":"UTF-8",
    "prelt":"26",
    "url":"https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
    "returntype":"META",
}
headers2 ={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'825',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'SINAGLOBAL=183.15.176.189_1562202096.905826; UOR=www.baidu.com,tech.sina.com.cn,; U_TRS1=0000007d.790f456f.5d229ce6.1f690140; UM_distinctid=16bcf34e850617-03c1571a29ab81-454c092b-12ae3a-16bcf34e851631; lxlrttp=1560672234; vjuids=fd60b7735.16c40c9950d.0.46d03c41749b6; vjlast=1564455048; ArtiFSize=14; login=1d5adbc41bf925048a06589ff4d2f3d5; Apache=183.15.178.115_1564712467.226702; ULOGIN_IMG=gz-3d282e51b4ed27139d407dc1e1e5095bda0e; SCF=AjmU8S4CLM0Rl6dU3Z0NBX4rRP_QFz69l-CCSt_AzBU1XaVAsxoU_fqJLfeD6u45eP6A4Ks3LNRZznhgo5SWoy8.; ULV=1564716547246:5:2:4:183.15.178.115_1564712467.226702:1564642074816; SGUID=1564716547781_99924112; U_TRS2=00000073.36933374.5d43ae09.68425ab1; SUB=_2AkMqH0SrdcPxrAJWkPwTyGzjaIhH-jyZyi1dAn7tJhMyAhgv7ksAqSVutBF-XGI-NOtaPwh9a-pstDIjzLJCa9pk; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9W5FnGGBr-542J8MkH.cobVe5JpVhKMXShBpSoU5UgeVqcRt',
'Host':'login.sina.com.cn',
'Origin':'https://weibo.com',
'Referer':'https://weibo.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)&_=1564713731419'
print('******'*10)
print(data)
res = s.post(url=url, headers=headers2, data=data)
print(res.cookies)
result = res.content.decode('gbk')
print(result)

##重定向 两次
while True:
    pat = '''location\.replace\(['"](.*?)['"]\)'''
    login_url = re.findall(pat,result)
    if login_url:
        result = s.get(login_url[0]).content.decode('gbk')
        print(result)
    else:
        break



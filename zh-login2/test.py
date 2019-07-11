###验证js encrypt函数是否可用
from urllib.parse import urlencode
import execjs

login_data = {
    'captcha':"",
    'clientId':"c3cef7c66a1843f8b3a9e6a1e3160e20",
    'grantType':"password",
    'lang':"en",
    'password':"",   ###
    'refSource':"inbox",
    'signature':"",  ###
    'source':"com.zhihu.web",
    'timestamp':1558335693187,
    'username':"",   ###
    'utmSource':"",
}

print(urlencode(login_data))
def _encrypt(form_data: dict):
        with open('./encrypt.js',encoding='UTF-8') as f:
            myjs = execjs.compile(f.read())
            return myjs.call('Q', urlencode(form_data))



data = _encrypt(login_data)
print(data)

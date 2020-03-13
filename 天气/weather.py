import execjs,time,json,base64,hashlib,requests

###https://www.aqistudy.cn/
###调用js
'''
with open('js.js') as f:
    js = f.read()
query = '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'
token = execjs.compile(js).call("decodeData", query)
print(token)

'''
######## DES  CBC16位秘钥
from pyDes import *
def DesEncrypt(res,key,iv=b"9ff4453b"):
    Des_Key = (key+"0000")[0:8]
    k = des(Des_Key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    k.setKey(key)##重写为16位
    EncryptStr = k.encrypt(res)
    return base64.b64encode(EncryptStr) #转base64编码返回

def DesDecrypt(res,key,iv=b"9ff4453b"):
    Des_Key = (key+"0000")[0:8]
    EncryptStr = base64.b64decode(res)
    k = des(Des_Key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    k.setKey(key)##重写为16位
    DecryptStr = k.decrypt(EncryptStr)
    #print(DecryptStr)
    return DecryptStr 



'''
加密解密时未提供适合的密文填充工具，因此有必要自己实现一个，下面是常见的 PKCS#5 / PKCS#7 填充模式的一般写法：
PKCS#5 padding is identical to PKCS#7 padding, except that 
it has only been defined for block ciphers that use a 64 bit (8 byte) 
block size.
But in AES, there is no block of 8 bit, so PKCS#5 is PKCS#7.
'''
## windows安装pycryptodome,linux安装pycrypto
## 使用的是AES CBC加密解密法
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex   #b2a_hex：转16进制  、a2b_hex：与b2a_hex对应

BS = AES.block_size    
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]
    
class PrpCrypt(object):
 
    def __init__(self, key,iv=b'0000000000000000'):
        self.key = key.encode('utf-8')
        self.iv = iv
        self.mode = AES.MODE_CBC
        

    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, self.iv)
        # 这里密钥key 长度必须为16（AES-128）,
        # 24（AES-192）,或者32 （AES-256）Bytes 长度
        # 目前AES-128 足够目前使用
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            # \0 backspace
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        elif count > length:
            add = (length - (count % length))
            # text = text + ('\0' * add)
            text = text + ('\0' * add).encode('utf-8')
        
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        b2a_hex_ciphertext = str(b2a_hex(self.ciphertext), encoding = "utf-8") 
        return b2a_hex_ciphertext  ##str形式
        
 
    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        text = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, self.iv)
        plain_text = cryptor.decrypt(text)
        # print(plain_text)
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')[:-8]

    

def hex_md5(sss):
    return hashlib.md5(sss.encode(encoding='UTF-8')).hexdigest()

def base64_en(sss):
    return str(base64.b64encode(sss),'utf-8')

## dict 转 json 去除非value值内的其他空格
def cjson(obj):
    return json.dumps(obj,ensure_ascii=False).replace(', "',',"').replace(': ',':')
    
def my_getParam(method,obj,pc):
    appId = "1a45f75b824b2dc628d5955356b5ef18"
    ts = '1570774367691'#str(int(round(time.time()*1000)))
    clienttype = "WEB"
    #method = "GETCITYWEATHER"
    #obj = {"city":"北京","type":"HOUR","startTime":"2019-10-09 13:00:00","endTime":"2019-10-10 16:00:00"}
    
    sort_obj ={"city":obj['city'],"endTime":obj["endTime"],"startTime":obj["startTime"],"type":obj["type"]}
    sort_obj_dumps = cjson(sort_obj)
    mixmd5 = hex_md5(appId + method + ts + clienttype + sort_obj_dumps)
    #print(mixmd5)
    param = {
        "appId": appId,
        "method": method,
        "timestamp": int(ts),
        "clienttype": clienttype,
        "object": obj,
        "secret": mixmd5
    }
    param_dumps = cjson(param)
    base64_param = base64_en(param_dumps.encode('utf-8'))
    #print(base64_param)
    e = pc.encrypt(pad(base64_param))
    
    result = base64_en(a2b_hex(e[:-32])) ##去掉后面pad的32位 再16进制转字符串base64编码
    #print(result)
    return result



def crawlcontent(data):
    burl = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    res = requests.post(burl,headers=headers,data=data).content
    res = res.decode('utf-8')
    #print(res)
    return res





def my_decodeData(data):
    aes_key = "6faf4a2fa46ac1cb"
    aes_iv = b'4d6c56abc669f198'
    
    des_key = "863f30c7f96c96fb"
    des_iv = b"9ff4453b"
    
    pc = PrpCrypt(aes_key, aes_iv)
    data = pc.decrypt(data)
    
    data = DesDecrypt(data,des_key,des_iv)
    data = base64.b64decode(data).decode('utf-8')
    return data




key4 = "d0936268a554ed2a"
iv4 = b'2441e23aca5285a8'
pc = PrpCrypt(key4, iv4)  # 初始化密钥

obj = {'city': "上海", 'type': "HOUR", 'startTime': "2019-10-10 11:00:00", 'endTime': "2019-10-11 14:00:00"}
result = my_getParam('GETCITYWEATHER',obj,pc)
resultdata={"d":result}
needdecrypt = crawlcontent(resultdata)
print(my_decodeData(needdecrypt))
'''
### 解密 解析
needdecrypt='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'
print(my_decodeData(needdecrypt))
'''

import execjs,time,json,base64

'''
sss0 = "你好siri,今天天气30摄氏度！...++/=1"
sss1 = "你好siri,今天天气30摄氏度！...++/=1"
sss2 = sss1.encode('utf-8')
print(sss2,type(sss2))
print(base64.encodestring(sss2))
print(base64.b64encode(sss2))
'''


from Crypto.Cipher import DES,DES3

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
 
 
class PrpCrypt(object):
 
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.mode = AES.MODE_CBC
 
    # 加密函数，如果text不足16位就用空格补足为16位，
    # 如果大于16当时不是16的倍数，那就补足为16的倍数。
    def encrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
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
        return b2a_hex(self.ciphertext)
 
    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, b'0000000000000000')
        plain_text = cryptor.decrypt(a2b_hex(text))
        # return plain_text.rstrip('\0')
        return bytes.decode(plain_text).rstrip('\0')


class DESUtil(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')
        self.__BLOCK_SIZE_8 = self.BLOCK_SIZE_8 = DES.block_size
        self.IV = "9ff4453b".encode('utf-8') # __IV = chr(0)*8
        
    
    def encryt(self,text):
        text = text.encode('utf-8')
        cipher = DES.new(self.key, DES.MODE_CBC, self.IV)
        x = self.__BLOCK_SIZE_8 - (len(text) % self.__BLOCK_SIZE_8)
        if x != 0:
            text = text + chr(x)*x
        msg = cipher.encrypt(text)
        # msg = base64.urlsafe_b64encode(msg).replace('=', '')
        msg = base64.b64encode(msg)
        return msg
    
    def decrypt(self,enStr):
        # enStr += (len(enStr) % 4)*"="
        # decryptByts = base64.urlsafe_b64decode(enStr)
        decryptByts = base64.b64decode(enStr)
        cipher = DES.new(self.key, DES.MODE_CBC,self.IV)
        msg = cipher.decrypt(decryptByts)
        b2a_hex_ciphertext = str(b2a_hex(msg), encoding = "utf-8") 
        print(b2a_hex_ciphertext)
        result = base64_en(a2b_hex(b2a_hex_ciphertext))
        print(result)
        return result

def base64_en(sss):
    return str(base64.b64encode(sss),'utf-8')


from pyDes import *
import base64

# Des CBC
# 自定IV向量

def DesEncrypt(res,key,iv=b"9ff4453b"):
    Des_Key = (key+"0000")[0:8]
    k = des(Des_Key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    k.setKey(key)
    EncryptStr = k.encrypt(res)
    return base64.b64encode(EncryptStr) #转base64编码返回

def DesDecrypt(res,key,iv=b"9ff4453b"):
    Des_Key = (key+"0000")[0:8]
    EncryptStr = base64.b64decode(res)
    k = des(Des_Key, CBC, iv, pad=None, padmode=PAD_PKCS5)
    k.setKey(key)
    DecryptStr = k.decrypt(EncryptStr)
    #print(DecryptStr)
    return DecryptStr 


if __name__ == '__main__':
    res = "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"
    des_key = "863f30c7f96c96fb"
    des_iv = b"9ff4453b"
    result = DesDecrypt(res,des_key,des_iv)
    EncryptStr = base64.b64decode(result).decode('utf-8')
    print(EncryptStr)
    


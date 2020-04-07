import base64
import zlib
import json,time
from urllib import parse

Parameters = {
	'cityName':'深圳',
	'cateId':'0',
	'areaId':'31',
	'sort':'',
	'dinnerCountAttrId':'',
	'page':'3',
	'userId':'',
	'uuid':'687696e83faf45b488eb.1551933832.1.0.0',
	'platform':'1',
	'partner':'126',
	'originUrl':'http://sz.meituan.com/meishi/b31/pn3/',
	'riskLevel':'1',
	'optimusCode':'1',
}


def dict2str(p_dict):
    d2l = []
    for key, value in p_dict.items():
        d2l.append(key + '=' + str(value))
    return '&'.join(d2l)


def make_sign(paramstr):
	compressstr = zlib.compress(paramstr.encode('utf-8'))
	sign = base64.b64encode(compressstr)
	#print(sign)
	return sign

def make_url(param):
	url = 'http://sz.meituan.com/meishi/api/poi/getPoiList?'
	url1 = dict2str(param)
	url = url + url1
	url = url + '&' + '_token=' + maketoken(param)
	print(url)
	return url

def maketoken(Param):
	#按固定顺序排序
	signParameters = {
	'areaId':Param['areaId'],
	'cateId':Param['cateId'],
	'cityName':Param['cityName'],
	'dinnerCountAttrId':Param['dinnerCountAttrId'],
	'optimusCode':Param['optimusCode'],
	'originUrl':Param['originUrl'],
	'page':Param['page'],
	'partner':Param['partner'],
	'platform':Param['platform'],
	'riskLevel':Param['riskLevel'],
	'sort':Param['sort'],
	'userId':Param['userId'],
	'uuid':Param['uuid'],
	}
	#得到sign,并填充mytoken
	str1 = dict2str(signParameters)
	sign = make_sign(str1).decode()
	ts = int(round(time.time() * 1000))
	cts = ts + 100
	url1 = Param['originUrl']
	url2 = 'https://sz.meituan.com/meishi/'

	mytoken ={
	'rId':100900,
	'ver':'1.0.6',
	'ts':ts,
	'cts':cts,
	'brVD':[1435, 190],
	'brR':[[1475, 830], [1475, 792], 24, 24],
	'bI':[url1, url2],
	'mT':[],
	'kT':[],
	'aT':[],
	'tT':[],
	'aM':'',
	'sign':sign
	}
	#mytoken做处理，去空格转为str，压缩并b64加密，最后qote（URL编码）输出
	mytoken = json.dumps(mytoken).replace(' ','')
	#print('dict后： ',mytoken)
	mydecode = zlib.compress(mytoken.encode())
	#print('compress后： ',mydecode)
	mydecode = base64.b64encode(mydecode)
	#print('b64encode后： ',mydecode)
	result = parse.quote(mydecode)
	#print('quote后： ',result)
	return result
	

url = make_url(Parameters)


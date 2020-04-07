import requests,json,re,time,execjs


class tCookie:
    def __init__(self):
        self.url = "http://www.gsxt.gov.cn/SearchItemCaptcha?t={}".format(int(round(time.time() * 1000)))
        with open(r'./js/cookies.js') as f:
            cookie_crack = f.read()
        self.cookie_crack = execjs.compile(cookie_crack)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'
        }

    def require_js(self):
        """
        不带cookies请求首页，获得返回的js
        :return:页面中的js,和set_cookies中的jsluid
        """
        response = requests.get(self.url, headers=self.headers)
        if response.status_code == 521:
            return response.text, response.headers['Set-Cookie'].split('=')[1].split(';')[0]
        else:
            print(response.text)
            print(self.headers)
            return None, None

    def first_decryption(self, first_js):
        """
        解密js,获得第二层加密的js
        :param first_js:
        :return:
        """
        x = re.findall('var x="(.*?)"', first_js)[0]
        y = '"'+ re.findall(',y="(.*?)"', first_js)[0] + '"'
        #print('x',x)
        #print('y',y)
        second_js = self.cookie_crack.call('getjs', x, y)
        #print('second_js',second_js)
        return second_js

    def regex(self, js):
        regex =  "!*window\[.*?\]"
        find = re.findall(regex, js)
        if find:
            for f in find:
                if '!' in f:
                    if len(re.findall('!', f)) % 2 == 0:
                        js = js.replace(f, 'false')
                    else:
                        js = js.replace(f, 'true')
                else:
                    js = js.replace(f, 'undefined')
        js = js.replace('window.headless', 'undefined')
        return js
    

    def sejs_maker(self,second_js):
        #pat = """setTimeout(.*?);"""
        #second_js = re.sub(pat,'',second_js)
        
        ##转义
        #js = second_js.replace('\\\\', '\\')
        
        second_js = 'cookie=' + second_js.split('document.cookie=')[1]
        second_js = second_js.split('Path=/;')[0] + "'"

        ### 替换window,document
        second_js = self.regex(second_js)
        
        s = """
            function cook() {
            %s
            return cookie
            }
            """
        new_js = s % second_js
        print('最终js:',new_js)
        ctx = execjs.compile(new_js)
        # 切割获得的__jsl_clearance
        jsl = ctx.call('cook')
        #print('jsl',jsl)
        jsl = jsl.split(';')[0]
        jsl_clearance = jsl.split('=')[1]
        print('jsl_clearance',jsl_clearance)
        return jsl_clearance

    def test_cookies(self, jsluid, jsl_clearance):
        """
        带cookies访问,测试拿到的是否正确
        :param jsluid:cookies中的参数
        :param jsl_clearance: cookies中的参数
        """
        headers = self.headers.copy()
        headers['Cookie'] = f'__jsluid_h={jsluid}; __jsl_clearance={jsl_clearance};'
        response = requests.get(self.url, headers=headers)
        print('SearchItemCaptcha结果为：',response.text)
        return response


    def run(self):
        count = 0
        while count < 5:
            fjs,jsluid = self.require_js()
            sejs = self.first_decryption(fjs)
            try:
                jsl_clearance = self.sejs_maker(sejs)
            except Exception as e:
                print(e)
                time.sleep(2)
                count = count + 1
                continue
            else:
                res = self.test_cookies(jsluid, jsl_clearance)
                if res.status_code == 200:
                    print('jsluid, jsl_clearance 有效!')
                    JSESSIONID = re.findall('JSESSIONID=(.*?);', res.headers['Set-Cookie'])[0]
                    tlb_cookie = re.findall('tlb_cookie=(.*?);', res.headers['Set-Cookie'])[0]
                    return jsluid, jsl_clearance,res.json(),JSESSIONID,tlb_cookie
                else:
                    print(res.status_code)
                    time.sleep(2)
                    count = count + 1
                    continue


        

ss = tCookie()
jsluid, jsl_clearance, res, JSESSIONID, tlb_cookie = ss.run()
print(jsluid,jsl_clearance,res,JSESSIONID,tlb_cookie)

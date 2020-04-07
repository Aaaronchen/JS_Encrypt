**登陆** https://paicc-core.pingan.com.cn/paicc-core-web/webapi/login.view?tabs=account&appId=16666 

----------

**js为**

1. https://captcha-static.pingan.com/static/js/fullpage.pingan.1.3.9.js
2. https://captcha-static.pingan.com/static/js/slide.pingan.1.2.js


----------
**调用代码**

    pwd_encrypt_js_path = './js/login_pwd_encrypt.js'
    fullpage_t1_js_path = './js/fullpage_t1.js'
    fullpage_w1_js_path = './js/fullpage_w1.js'
    fullpage_w2_js_path = './js/fullpage_w2.js'
    slide_other = './js/slide_other.js'
    slide_a_js_path = './js/slide_a.js'
    slide_u_js_path = './js/slide_U.js'
    
    def get_js(js_path):
    """获取js可执行对象"""
    with open(os.path.dirname(__file__) + js_path, encoding='GBK') as f:
    js_file = f.read()
    return execjs.compile(js_file)
    
    
    pwd_encrypt_js = get_js(pwd_encrypt_js_path)
    fullpage_t1_js = get_js(full_page_t1_js_path)
    fullpage_w1_js = get_js(full_page_w1_js_path)
    fullpage_w2_js = get_js(full_page_w2_js_path)
    slide_other_js = get_js(slide_other)
    slide_u_js = get_js(slide_u_js_path)
    slide_a_js = get_js(slide_a_js_path)
    
    
    def get_encrypt_pwd(pwd):
    """获取加密后的密码"""
    return pwd_encrypt_js.call('pwdEncrypt', pwd)
    
    
    def get_fullpage_t1(s):
    """获取fullpage的t1参数"""
    return fullpage_t1_js.call('get_t', s)
    
    
    def get_fullpage_w1(gt, challenge, s):
    """获取fullpage的w1参数"""
    t = get_fullpage_t1(s)
    return fullpage_w1_js.call('get_w', gt, challenge, s, t)
    
    
    def get_fullpage_w2(gt, challenge, s):
    """获取fullpage的w2参数"""
    return fullpage_w2_js.call('get_w', gt, challenge, s)
    
    
    def get_slide_w(gt, challenge, s, offset, track):
    """获取slide的w参数"""
    u = {
    'lang': 'zh-cn',
    'userresponse': slide_other_js.call('getUserResponse', offset - 1, challenge),
    'passtime': track[-1][-1],
    'imgload': random.randint(110, 180),
    'a': slide_other_js.call("mouse_encrypt", track),
    'ep': {"v": "1.2", "f": slide_other_js.call("lmWn", gt + challenge)},
    'rp': slide_other_js.call("lmWn", gt + challenge[0:32] + str(track[-1][-1]))
    }
    u = slide_u_js.call('_encrypt', u, s)
    a = slide_a_js.call('get_a', s)
    return u + a
    
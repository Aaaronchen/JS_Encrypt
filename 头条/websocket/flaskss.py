from flask import Flask, request,render_template
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
import time

user_socket_list = []
msg = ''
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/api',methods=['POST'])
def ws1():
    global msg,user_socket_list
    url = request.form["url"]
    print(url)
    for socket in user_socket_list:
        socket.send(url)
        time.sleep(0.1)
        print(msg)
        return url+'&_signature='+msg

                
@app.route('/ws')
def ws2():
    global msg,user_socket_list
    user_socket = request.environ.get('wsgi.websocket') # type:WebSocket  
    # 建立连接
    if user_socket:
        user_socket_list.append(user_socket) # 将建立的连接添加进一个列表
        print(len(user_socket_list))
    else:
        return '请用websocket链接'
    while 1:
        message = user_socket.receive()
        if 'started' not in message:
            print(message)
            msg = message
    
                
                
if __name__ == '__main__':
    http_serv = WSGIServer(('0.0.0.0',8000),app,handler_class=WebSocketHandler)
    http_serv.serve_forever()

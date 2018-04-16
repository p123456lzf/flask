# -*- coding: utf-8 -*-
from flask import Flask
from torrents_api import get_torrents_api,get_torrent

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/keyword/<keyword>/page/<i>')
def a(keyword,i):
    return get_torrents_api(keyword,i)

@app.route('/url/<url>')
def b(url):
    return get_torrent(url)

if __name__ == "__main__":
    #print(into_flash_str(4201587825642984))
    app.run(host='0.0.0.0',port=5001,debug=True)
    #, ssl_context=("ssl.crt","ssl.key")
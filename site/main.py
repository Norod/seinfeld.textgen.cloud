# -*- coding: utf-8 -*-

import os

from flask import Flask, request, send_file
from model import extend

maxNumOfTokensToExtend = 128

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_file('favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/robots.txt')
def robots():
    return send_file('robots.txt', mimetype='text/plain')

@app.route('/checkpoint')
def checkpoint():
    return ("20211005-1735")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return send_file('index.html')
    
    data = request.form.get('text_in')
    if len(data) > 0:
        title_data = str(data)
    else:
        title_data = ""
    
    return extend(title_data,maxNumOfTokensToExtend)


if __name__ == "__main__":
    app.run('0.0.0.0', os.environ.get('PORT', 8080))

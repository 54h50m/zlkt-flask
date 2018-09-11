# _*_ coding: utf-8 _*_
__author__ = '54h50m'

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

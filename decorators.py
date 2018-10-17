# _*_ coding: utf-8 _*_
__author__ = '54h50m'
__date__ = '2018/10/17 23:34'

from functools import wraps
from flask import session,redirect,url_for


# 登录限制为装饰器
def login_required(func):

    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_id'):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper
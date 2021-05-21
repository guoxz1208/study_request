# coding:utf -8
"""
读、写json文件，并获取token
"""
import os,sys
from Common.handle_json import HandJson
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

def cookie_value():
   get_cookie = HandJson().get_value("cookie",'/Config/cookie.json')
   return get_cookie

def write_cookie(key):
   write_cookie = HandJson().write_value(key,'/Config/cookie.json')
   return write_cookie

if __name__ == '__main__':
    # data={'token':'1234567890'}
    # write_cookie(data,'/Config/cookie.json')
    print(cookie_value())

# coding:utf -8
"""
读、写json文件，并获取token
"""
import os,sys
from Common.handle_json import HandJson
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

def cookie_value(key,file_name=None):
   get_cookie = HandJson().get_value(key,file_name)
   return get_cookie

def write_cookie(key,file_name=None):
   write_cookie = HandJson().write_value(key,file_name)
   return write_cookie

if __name__ == '__main__':
    # data={'token':'1234567890'}
    # write_cookie(data,'/Config/cookie.json')
    print(cookie_value('token','/Config/cookie.json'))

# coding:utf -8
"""
获取header
"""
import json
from Common.handle_json import HandJson
import os,sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

def read_header():
    header_value = HandJson().read_json('/Config/header.json')
    return header_value

def write_header_token(key):
    headers = read_header()
    headers['token'] = key
    return headers

if __name__ == '__main__':
    data = 'qwqweqweqwewqesdasda'
    print(read_header())
    print(write_header_token(data))

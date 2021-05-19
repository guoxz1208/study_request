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

def read_header(file_name):
    header_value = HandJson().read_json(file_name)
    return header_value

if __name__ == '__main__':
    print(read_header('/Config/header.json'))

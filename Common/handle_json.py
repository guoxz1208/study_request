# coding:utf -8
"""
读取json配置文件
"""
import json
from jsonpath_rw import jsonpath,parser
import os
import sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
sys.path.append(base_path)

class HandJson:
    # 读取json文件中内容
    def read_json(self,file_name=None):
        if file_name == None:
            file_path = base_path + '/Config/header.json'
        else:
            file_path = base_path + file_name
        with open(file_path,encoding='utf -8') as f:
            date = json.load(f)
        return date

    # 读取json文件中内容
    def get_value(self,key,file_name=None):
        data = self.read_json(file_name)
        return data.get(key)

    # json文件写入内容
    def write_value(self,data,file_name=None):
        data_value = json.dumps(data)
        if file_name == None:
            file_path = base_path + '/Config/header.json'
        else:
            file_path = base_path + file_name
        with open(file_path,'w') as f:
            f.write(data_value)

    #  # json文件中增加内容
    # def updata_value(self):





if __name__ == '__main__':
    json_test = HandJson()
    print(json_test.read_json('/Config/token.json'))
    # print(json_test.get_value('token','/Config/cookie.json'))
    # print(json_test.write_value("{'token':'1234567890'}"))

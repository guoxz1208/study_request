# coding=utf -8
"""
接口请求方法
"""
import json
import requests
import os,sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
from Common.handle_cookie import write_cookie
from Common.handle_ini import HandIni
from Common.handle_json import HandJson

class BaseRequest:

    def send_get(self,url,params=None,headers=None,cookie=None,get_cookie=None,token=None,get_token=None):
        if token != None:
            headers["token"] = token
            print(headers)
            response = requests.get(url=url,data=params,headers=headers,cookies=cookie,verify=False)
        else:
            response = requests.get(url=url,data=params,headers=headers,cookies=cookie,verify=False)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            # 工具方法转换成字典
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value,'/Config/cookie.json')
        res = response.text
        if get_token != None:
            token_value = response.headers
            token = token_value["token"]
            HandIni().write_value(token)

        return res

    def send_post(self,url,params,headers=None,cookie=None,get_cookie=None,token=None,get_token=None):
        if token != None:
            headers["toekn"] = token
            # print(headers)
            response = requests.post(url=url,json=params,headers=headers,cookies=cookie,verify=False)
        else:
            response = requests.post(url=url,json=params,headers=headers,cookies=cookie,verify=False)

        if get_cookie != None:
            cookie_value_jar = response.cookies
            # 工具方法转换成字典
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, '/Config/cookie.json')

        # if get_token != None:
        #     token_value = response.headers
        #     token = token_value["token"]
        #     HandIni().write_value(token)
        res = response.text
        return res

    def run_main(self,method,url,params,headers=None,cookie=None,get_cookie=None,token=None,get_token=None):
        if method == "GET":
            res = self.send_get(url,params,headers,cookie,get_cookie,token,get_token)
        else:
            res = self.send_post(url,params,headers,cookie,get_cookie,token,get_token)
        try:
            res = json.loads(res)
        except:
            print("这个结果是一个text")
        print("--->", res)
        return res

# if __name__ == '__main__':
#     """
#     url = "http://47.101.48.192:8001/api/login"
#     login_value = {"username": "admin", "password": "12345"}
#     headers = {"Content-Type":"application/json"}
#     """
#
#
#     method="POST"
#     url = "http://47.101.48.192:8001/api/login"
#     data = {"username": "admin","password": "123456"}
#     header = {"Content-Type": "application/json;charset=UTF-8"}
#     cookie = None
#     get_cookie = {'is_cookie': 'app'}
#     token = None
#     get_token = {'is_token'}
#
#     request = BaseRequest()
#     request.run_main(method,url,data,header,cookie,get_cookie,token,get_token)
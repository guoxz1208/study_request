# coding:utf -8
"""
用例执行
"""

import os,sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import pytest
from Tools.excel_data import ExcelData
from Base.base_request import BaseRequest
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


#('登录成功', 'http://47.101.48.192:8001/api/login', 'POST', '{"username": "admin","password": "123456"}', {'Content-Type': 'application/json'}, None, None, None, {'is_token': 'app'})
class TestCase:

    @pytest.mark.parametrize("caseName,url,method,data,header,cookie,get_cookie,token,get_token",ExcelData().excle_value('login','/Config/header.json','cookie','/Config/cookies.json'))
    def test_login(self,caseName,url,method,data,header,cookie,get_cookie,token,get_token):
        print("caseName:",caseName)
        """
        method:POST
        url:http://47.101.48.192:8001/api/login
        data:{"username": "admin","password": "123456"}
        header:{'Content-Type': 'application/json;charset=UTF-8'}
        cookie:None
        get_cookie:{'is_cookie': 'app'} 
        toekn:None
        get_token:{'is_token': 'app'}
        """
        res = BaseRequest().run_main(method,url,data,header,cookie,get_cookie,token,get_token)
        return res



if __name__ == '__main__':
    # pytest.main(['test_case.py','-s','--alluredir',base_path+'/report/tmp'])
    # os.system('allure serve ../report/tmp')
    pytest.main(['-s', "--html="+base_path +"/Report/html/report"+nowTime+".html", 'test_case.py'])

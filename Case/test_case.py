# coding:utf -8
"""
用例执行
"""
import json
import os,sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)
import pytest
# from Tools.excel_data import ExcelData
from Tools.excel_text import ExcelText
from Base.base_request import BaseRequest
from Common.handle_excel import HandExcel
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


#('登录成功', 'http://47.101.48.192:8001/api/login', 'POST', '{"username": "admin","password": "123456"}', {'Content-Type': 'application/json'}, None, None, None, {'is_token': 'app'})
class TestCase:

    @pytest.mark.parametrize("caseName,url,method,data,headers,cookie,get_cookie,token,get_token,expect",ExcelText().excle_value('test'))
    def test_login(self,caseName,url,method,data,headers,cookie,get_cookie,token,get_token,expect):

        res = BaseRequest().run_main(method,url,data,headers,cookie,get_cookie,token,get_token)
        row = HandExcel().get_row("test")
        one = 0
        # HandExcel().write_excel(2,13,json.dumps(res),1)

        # print(expData)
        assert expect['code'] in str(res["code"])

        # return res



if __name__ == '__main__':
    pytest.main(['test_case.py','-s','--alluredir', base_path+'/Report/tmp'])
    # pytest.main(['test_login.py', '-s', '--alluredir', '../report/tmp'])
    os.system('allure serve'+ base_path+'/Report/tmp')
    # os.system('allure serve ../report/tmp')
    # pytest.main(['-s', "--html="+base_path +"/Report/html/report"+nowTime+".html", 'test_case.py'])

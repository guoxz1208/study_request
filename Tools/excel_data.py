# coding=utf -8
"""
根据handle_excle.py文件读取其中的内容
"""
from Common.handle_excel import HandExcel
from Common.handle_ini import HandIni
from Common.handle_json import HandJson
from Common.handle_header import read_header
from Common.handle_cookie import cookie_value
import json
import os
import sys
# base_path = os.getcwd()
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
sys.path.append(base_path)

class ExcelData:
    def __init__(self):
        self.excel = HandExcel()
        self.ini = HandIni()
        self.json = HandJson()


    def excle_value(self,sheet_name,header_path,cooks,cooks_path):
        """
        :param sheet_name: sheet页名称
        :param header_path: 请求头json配置文件路径
        :param cooks: cookies值
        :param cooks_path: cookies配置文件路径
        """
        resList = []
        header = None
        cookie =None
        get_cookie = None
        token = None
        base_url = self.ini.get_value('server','host')
        row_num = self.excel.get_row()
        one = 0
        for one in range(row_num):
            if sheet_name in self.excel.get_cell_value(one, 0):
                case_name = self.excel.get_cell_value(one, 1)
                is_run = self.excel.get_cell_value(one, 2)
                # print(case_name,data)
                if is_run in 'yes':
                    res_url = self.excel.get_cell_value(one,3)
                    url = base_url + res_url
                    method = self.excel.get_cell_value(one,4)
                    data = self.excel.get_cell_value(one,5)
                    header_run = self.excel.get_cell_value(one,6)
                    if header_run in 'yes':
                        header = read_header(header_path)
                    cookie_method = self.excel.get_cell_value(one,7)
                    if cookie_method == 'yes':
                        cookie = cookie_value(cooks,cooks_path)
                        # cookie = HandIni().get_value('type','token','/Config/token.ini')
                        # print("================="+cookie)
                    elif cookie_method == 'write':
                        get_cookie = {"is_cookie":"app"}
                    else:
                        cookie = None
                        get_cookie = None
                    token_method = self.excel.get_cell_value(one,8)
                    if token_method == 'yes':
                        token = HandIni().get_value('type', 'token', '/Config/token.ini')
                    elif token_method == 'write':
                        get_token = {"is_token": "app"}
                    else:
                        token = None
                        get_token = None

                    resList.append((case_name,url,method,data,header,cookie,get_cookie,token,get_token))
            one +=1
        return resList

if __name__ == '__main__':
    excel_data = ExcelData()
    print(excel_data.excle_value('login', '/Config/header.json', 'token', '/Config/cookies.json'))
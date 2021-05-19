# coding=utf -8
"""
读取ini配置文件
"""
import configparser
import os
import sys
base_path = os.path.abspath(os.path.join(os.getcwd(),'../'))
# base_path = os.getcwd()
sys.path.append(base_path)

class HandIni:
# 打开ini配置文件
    def read_ini(self,file_name=None):
        if file_name == None:
            file_path = base_path + '/Config/server.ini'
        else:
            file_path = base_path + file_name
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding="utf-8-sig")
        return cf

    # 读取配置文件ini内容
    # section：所属部分；option：内容选项
    def get_value(self,section,option,file_name=None):
        cf = self.read_ini(file_name)
        data = cf.get(section,option)
        return data

    def write_value(self,key,file_name=None):
        if file_name == None:
            file_path = base_path + '/Config/server.ini'
        else:
            file_path = base_path + file_name
        cf = self.read_ini(file_path)
        list = []
        list = cf.sections()       # 获取到配置文件中所有分组名称
        print(list)
        if 'type' not in list:
            cf.add_section('type')              # 添加分组名称
            cf.set('type', 'token', key)  # 给type分组设置值
        # cf.remove_option('type', 'stuno')  # 删除type分组的stuno
        # cf.remove_section('tpye')  # 删除配置文件中type分组
        o = open(base_path+'/Config/token.ini', 'w')
        cf.write(o)
        o.close()

        return list


if __name__ == '__main__':
    ini = HandIni()
    print(ini.write_value("123123",'/Config/token.ini'))

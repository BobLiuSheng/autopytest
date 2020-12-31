#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 11:28
# @Author : 刘升
# @Version：V 0.1
# @File : utility.py
# @desc :Util类，读取数据类，当前仅实现读取数据源文件格式为Excel
import xlrd
import xlsxwriter
class ExcelUtil:
    def __init__(self,file_name,mode='r'):
        if mode == 'r':
            self.workbook = xlrd.open_workbook(file_name)
        elif mode == 'w':
            self.workbook = xlsxwriter.Workbook(file_name)
        else:
            raise Exception('Error: init Excel class with error mode: %s' % mode)
    
    def read(self,sheet_name):
        """
        ExcelUtil.read("Excelsheet名称"),读取Excel表中sheet表内容，参数为sheet名字
        return[[],[],[].....]
        """
        sheet = self.workbook.sheet_by_name(sheet_name)
        nrows = sheet.nrows
        data = []
        for i in range(nrows):
            data.append(sheet.row_values(i))
        return data

    def param_case(data):
        """
        前置方法data = ExcelUtil.read("Excelsheet名称")
        ExcelUtil.param_case(data),接收read读取的列表测试数据，并遍历组成[{},{}]格式，ddt调用格式
        """
        list_dict_data = []
        list_key = data[0]
        for d in data[1:]:
            dict_data = {}
            for i in range(len(list_key)):
                dict_data[list_key[i]] = str(d[i]).strip()
            list_dict_data.append(dict_data)
        return list_dict_data

    def param_setting(data,server_name):
        """
        前置方法data = ExcelUtil.read("Excelsheet名称")
        ExcelUtil.param_setting(data,server_name="对应Server_Name名称")
        """
        list_key = data[0]
        for d in data[1:]:
            if d[0] == server_name:
                dict_data = {}
                for i in range(len(list_key)):
                        dict_data[list_key[i]] = str(d[i]).strip()
                return dict_data

if __name__ == '__main__':
    excelpath = r'E:\WorkSpaces\MyGit\autopytest\autopytest\testcase\carsir_api_testcase.xlsx'
    excelfile = ExcelUtil(excelpath,'r')
    # exceldata = excelfile.read("CARSIR_APP")
    # ExcelUtil.param_case(exceldata)
    setting_data = excelfile.read("API_SETTING")
    ExcelUtil.param_setting(setting_data,"CarSir")
    # excelfile.get_sheet("CARSIR_APP")

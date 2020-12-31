#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 20:06
# @Author : 刘升
# @Version：V 0.1
# @File : test_api.py
# @desc :执行测试用例
import unittest
import ddt as ddt
import json
import requests

from autopytest.auto.utility import ExcelUtil

excelpath = r'E:\WorkSpaces\MyGit\autopytest\autopytest\testcase\carsir_api_testcase.xlsx'
excelfile = ExcelUtil(excelpath, 'r')
exceldata = excelfile.read("CARSIR_APP")
setting = excelfile.read("API_SETTING")
testdata = ExcelUtil.param_case(exceldata)
testsetting = ExcelUtil.param_setting(setting,"CarSir")
host = testsetting["HOST"]
header = eval(testsetting["Headers"])#将读取到的字符串转成字典格式
phone = testsetting["Phone"]

@ddt.ddt
class Test_api(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Action")

    @ddt.data(*testdata)
    def test_api(self,data):
        path = data["接口请求地址"]
        url = str(host + path)
        r = requests.post(url=url,headers = header)
        responsemsg=json.loads(json.dumps(r.json()))
        print("响应体：",responsemsg["message"])



if __name__ == '__main__':
    unittest.main()
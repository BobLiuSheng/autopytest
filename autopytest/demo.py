#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/30 19:53
# @Author : 刘升
# @Version：V 0.1
# @File : demo.py
# @desc :
import re
import unittest

import ddt

# testData = [{'用例编号': 'API_CarSir_GetCode_01', '用例标题': 'CarSir获取验证码-手机号为空', '请求方式': 'POST', 'Token': 'yes', '接口请求地址': '/olympic/api-resource/sms/customer/login/sendCode?mobile=${phone}', '请求参数': '', '断言方式': 'self.assertEqual("成功",responsemsg["message"])', '期望返回结果': '{"code":200,"data":true,"message":"成功","success":true}', '测试结果': '', '是否运行': 'yes'},
#             {'用例编号': 'API_CarSir_GetCode_02', '用例标题': 'CarSir获取验证码-手机号为错误手机号码', '请求方式': 'POST', 'Token': 'yes', '接口请求地址': '/olympic/api-resource/sms/customer/login/sendCode?mobile=${phone}', '请求参数': '', '断言方式': 'self.assertEqual("成功",responsemsg["message"])', '期望返回结果': '{"code":200,"data":true,"message":"成功","success":true}', '测试结果': '', '是否运行': 'yes'}]
# @ddt.ddt
# class Test_api(unittest.TestCase):
#     @ddt.data(*testData)
#     def test_api(self,data):
#         print("2222")
#         print(data["用例编号"])
#         print(data)
#
# if __name__ == '__main__':
#     unittest.main()

list = ['API_SETTING', 'CARSIR_APP', 'CENTER_APP']
str = list[0]
result = str.split('_')
print(result[1])
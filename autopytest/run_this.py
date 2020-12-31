# coding=utf-8
import unittest
import time, datetime
import os
import logging
from autopytest.auto import HTMLTestRunner

curpath = os.path.dirname(os.path.realpath(__file__))
print("curpath::::" + curpath)
report_path = os.path.join(curpath, "report")
print(report_path)
log_path = os.path.join(curpath, "log")
if not os.path.exists(report_path): os.mkdir(report_path)
case_path = os.path.join(curpath, "testcase")
def add_case(casepath=case_path, rule="test*.py"):
    print("step1")
    print(curpath)
    print(case_path)
    '''加载所有的测试用例'''
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(casepath, pattern=rule, )
    print("step2")
    print(discover)
    return discover

def run_case(all_case, reportpath=report_path):
    '''执行所有的用例, 并把结果写入测试报告'''

    # HTML格式报告
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    # htmlreport = reportpath + "/" + r"result" + now + ".html"

    htmlreport = os.path.join(reportpath,"result" + now + ".html")
    print("测试报告生成地址：%s" % htmlreport)
    fp = open(htmlreport, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="平台接口自动化测试报告", description="用例执行情况")

    # LOG日志记录
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename=log_path + '/' + now + r"result.log",
                        filemode='w')
    logger = logging.getLogger()
    logger.info(all_case)

    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()
    time.sleep(2)
    # sendmain(htmlreport, mail_to=['dsdsdsds'])
    print("发送测试报告邮件OK")

if __name__ == "__main__":
    cases = add_case()
    run_case(cases)
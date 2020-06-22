#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-
@Author: GaoKang
Project description：base_login
"""

import os
import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_case.public.base_page import BasePage

Excel_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'web_test_init.xlsx')


def dut_baseinfo():
    """
    获取待测设备ip和登陆用户名、密码
    :param excel_path: 存储信息的Excel路径
    :return: 设备ip、登陆用户名、密码、浏览器类型
    """
    book = xlrd.open_workbook(Excel_path)
    sheet = book.sheet_by_index(0)
    baseinfo = sheet.row_values(1)
    return baseinfo


class BaseLogin(object):
    def __init__(self):
        baseinfo = dut_baseinfo()
        if baseinfo[0] == 'Firefox':
            self.driver = webdriver.Firefox()
        elif baseinfo[0] == 'Ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.base_url = baseinfo[1]
        self.pagetitle = baseinfo[2]
        self.username = baseinfo[3]
        self.password = baseinfo[4]
        # self.driver = webdriver.Chrome()
        # self.base_url = 'http://120.0.60.5/WebContent/view.asp'
        # self.pagetitle = 'Web管理系统'

    def login_web(self):
        bspg = BasePage(self.driver, self.base_url, self.pagetitle)
        bspg.open_url()
        uername_loc = (By.ID, 'userName')
        pass_loc = (By.ID, 'password')
        login_loc = (By.ID, 'logonBt')
        bspg.send_keys(uername_loc, self.username)
        bspg.send_keys(pass_loc, self.password)
        bspg.find_element(*login_loc).click()


def main():
    """
    主函数
    """
    login = BaseLogin()
    print(login.base_url)
    login.login_web()


if __name__ == "__main__":
    main()

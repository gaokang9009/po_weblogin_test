#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-12-21
@Author: GaoKang
Project description：unittest LoginPage
"""

from selenium.webdriver.common.by import By
from time import sleep
import unittest
from test_case.public.LoginPage import LoginPage
from test_case.public.base_login import BaseLogin


class TestLoginPage(unittest.TestCase):
    def setUp(self):
        login_base = BaseLogin()
        self.driver = login_base.driver
        self.url = login_base.base_url
        self.pagetitle = login_base.pagetitle
        self.login_web = LoginPage(self.driver, self.url, self.pagetitle)
        self.login_web.open_url()

    # @unittest.skip
    def test_openweb(self):
        ele = self.driver.find_element(*(By.ID, 'copyright'))
        self.assertIn('鼎点视讯科技有限公司', ele.text)

    # @unittest.skip
    def test_swich_language(self):
        for i in range(4):
            ele = self.driver.find_element(*(By.ID, 'currentLanguage'))
            ele_text = self.driver.find_element(*(By.ID, 'copyright')).text
            # print(ele_text)
            if ele.text == 'English':
                self.assertIn('Topvision', ele_text)
            else:
                self.assertIn('鼎点视讯科技有限公司', ele_text)
            self.login_web.switch_language()
            sleep(1)

    # @unittest.skip
    def test_ch_loginweb(self):
        self.login_web.input_username('admin')
        self.login_web.input_password('admin')
        self.login_web.login_submit()
        ele = self.login_web.find_element(*(By.ID, 'topvision_logo'))
        self.assertIn('images/topvision-logo2.png', ele.get_attribute('src'))

    # @unittest.skip
    def test_en_loginweb(self):
        self.login_web.switch_language()
        self.login_web.input_username('admin')
        self.login_web.input_password('admin')
        self.login_web.login_submit()
        ele = self.login_web.find_element(*(By.ID, 'topvision_logo'))
        self.assertIn('images/topvision-logo2_en.png', ele.get_attribute('src'))

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        print("\r\nUnit test end!")


if __name__ == "__main__":
    unittest.main()

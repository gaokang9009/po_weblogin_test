#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-12-21
@Author: GaoKang
Project description：unittest LoginPage
"""
import pytest
from selenium.webdriver.common.by import By
from time import sleep


@pytest.mark.usefixtures('login_web')
class Test_Login_Page(object):

    @pytest.mark.smoke
    @pytest.mark.run(order=1)
    def recive_para(self, login_web):
        self.login_web, self.driver = login_web

    def test_openweb(self):
        ele = self.driver.find_element(*(By.ID, 'copyright'))
        assert '科技有限公司' in ele.text

    @pytest.mark.smoke
    def test_swich_language(self):
        for i in range(4):
            ele = self.driver.find_element(*(By.ID, 'currentLanguage'))
            ele_text = self.driver.find_element(*(By.ID, 'copyright')).text
            # print(ele_text)
            if ele.text == 'English':
                assert 'Topvision' in ele_text
            else:
                assert '科技有限公司' in ele_text
            self.login_web.switch_language()
            sleep(1)

    def test_ch_loginweb(self):
        self.login_web.input_username('admin')
        self.login_web.input_password('admin')
        self.login_web.login_submit()
        ele = self.login_web.find_element(*(By.ID, 'topvision_logo'))
        assert 'images/topvision-logo2.png' in ele.get_attribute('src')

    def test_en_loginweb(self):
        self.login_web.switch_language()
        self.login_web.input_username('admin')
        self.login_web.input_password('admin')
        self.login_web.login_submit()
        ele = self.login_web.find_element(*(By.ID, 'topvision_logo'))
        assert 'images/topvision-logo2_en.png' in ele.get_attribute('src'), 'not in'

    def setup_class(self):
        print("\r\nUnit test end!")


if __name__ == "__main__":
    pytest.main(['-v', '-s', '-m', "smoke"])

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-12-21
@Author: GaoKang
Project description：unittest LoginPage
"""
import pytest
from test_case.public.DeviceSnapPage import DeviceSnapPage


class Test_Snap_Page(object):

    def test_recive_para(self, login_web):
        self.driver, self.url, self.pagetitle = login_web
        snapPage = DeviceSnapPage(self.driver, self.url, self.pagetitle)
        snapPage.switch_to_snap()
        assert 1 == 1

    def test_recive_para1(self, login_web):
        self.driver, self.url, self.pagetitle = login_web
        snapPage = DeviceSnapPage(self.driver, self.url, self.pagetitle)
        snapPage.switch_to_snap()
        assert 1 == 1

    def setup_class(self):
        print("\r\nUnit test end!")


if __name__ == "__main__":
    pytest.main(['-v', '-s', '-m', "smoke"])

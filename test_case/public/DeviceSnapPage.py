#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-12-21
@Author: GaoKang
Project description：DeviceSnapPage
"""

from selenium.webdriver.common.by import By
from test_case.public.base_page import BasePage
from test_case.public.base_login import BaseLogin
import time


class DeviceSnapPage(BasePage):
    def __init__(self, driver, base_url, pagetitle):
        super().__init__(driver, base_url, pagetitle)
        self.snap_loc = (By.CSS_SELECTOR, '#ext-gen42 > em > span > span')

    def switch_to_snap(self):
        try:
            self.find_element(*self.snap_loc).click()
        except AttributeError:
            pass


def main():
    """
    主函数
    """
    login_base = BaseLogin()
    driver = login_base.driver
    base_url = login_base.base_url
    pagetitle = login_base.pagetitle
    login_base.login_web()
    snappage = DeviceSnapPage(driver, base_url, pagetitle)
    snappage.switch_to_snap()
    time.sleep(5)


if __name__ == "__main__":
    main()

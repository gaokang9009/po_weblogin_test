#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
created on 2019-12-21
@author：GaoKangKang
Project:LoginPage
"""

from selenium.webdriver.common.by import By
from test_case.public.base_page import BasePage
from test_case.public.base_login import BaseLogin


class LoginPage(BasePage):
    def __init__(self, driver, base_url, pagetitle):
        super().__init__(driver, base_url, pagetitle)
        self.uer_loc = (By.ID, 'userName')
        self.pass_loc = (By.ID, 'password')
        self.login_submit_loc = (By.ID, 'logonBt')
        self.login_cancel_loc = (By.CLASS_NAME, 'BUTTON75')
        self.switch_language_loc = (By.ID, 'language')

    def input_username(self, username):
        self.send_keys(self.uer_loc, username)

    def input_password(self, password):
        self.send_keys(self.pass_loc, password)

    def login_submit(self):
        try:
            self.find_element(*self.login_submit_loc).click()
        except AttributeError:
            pass

    def login_cancel(self):
        try:
            self.find_element(*self.login_cancel_loc).click()
        except AttributeError:
            pass

    def switch_language(self):
        try:
            self.find_element(*self.switch_language_loc).click()
        except AttributeError:
            pass


def main():
    """
    just test LoginPage
    """
    login_base = BaseLogin()
    driver = login_base.driver
    base_url = login_base.base_url
    pagetitle = login_base.pagetitle
    login_web = LoginPage(driver, base_url, pagetitle)
    login_web.open_url()
    login_web.input_username('admin')
    login_web.input_password('admin')
    login_web.login_submit()
    driver.quit()


if __name__ == "__main__":
    main()

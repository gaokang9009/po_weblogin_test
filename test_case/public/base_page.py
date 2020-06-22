#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
created on 2019-12-21
@author：GaoKangKang
Project:基础类BasePage
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class BasePage(object):
    """
    定义基类，实现常用函数
    """
    def __init__(self, driver, base_url, pagetitle):
        self.base_url = base_url
        self.driver = driver
        self.pagetitle = pagetitle

    def on_page(self, pagetitle):
        return pagetitle in self.driver.title

    def _open_url(self, url, pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle), '打开页面失败%s' % url

    def open_url(self):
        self._open_url(self.base_url, self.pagetitle)

    def find_element(self, *loc):
        try:
            # WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(*loc).is_displayed())
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('%s is not found!' % loc[1])

    def switch_frame(self, loc):
        return self.driver.switch_frame.to(loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            elem = self.find_element(*loc)
            if click_first:
                elem.click()
            if clear_first:
                elem.clear()
            elem.send_keys(value)
        except AttributeError:
            pass


def main():
    """
    just test class BasePage
    """
    driver = webdriver.Chrome()
    base_url = 'http://120.0.60.6/WebContent/view.asp'
    pagetitle = 'Web管理系统'
    web = BasePage(driver, base_url, pagetitle)
    web.open_url()
    uername_loc = (By.ID, 'userName')
    pass_loc = (By.ID, 'password')
    login_loc = (By.ID, 'logonBt')
    web.send_keys(uername_loc, 'admin')
    web.send_keys(pass_loc, 'admin')
    web.find_element(*login_loc).click()
    driver.quit()


if __name__ == "__main__":
    main()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-
@Author: GaoKang
Project description：
"""

import pytest
from test_case.public.LoginPage import LoginPage
from test_case.public.base_login import BaseLogin


@pytest.fixture()
def login_web():
    """登陆web的fixture"""
    login_base = BaseLogin()
    driver = login_base.driver
    url = login_base.base_url
    pagetitle = login_base.pagetitle
    login_base.login_web()
    # login_web = LoginPage(driver, url, pagetitle)
    # login_web.open_url()
    yield driver, url, pagetitle
    driver.close()

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2019-
@Author: GaoKang
Project description：
"""

import logging
import telnetlib
import time
import re


class TelnetClient(object):
    def __init__(self, host_ip, username, password):
        self.tn = telnetlib.Telnet()
        self.host_ip = host_ip
        self.username = username
        self.password = password

    # 此函数实现telnet登录主机
    def login_host(self):
        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(self.host_ip, port=23)
        except:
            logging.warning('%s网络连接失败'%self.host_ip)
            return False
        # 等待login出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Username:', timeout=10)
        self.tn.write(self.username.encode('ascii') + b'\n')
        # 等待Password出现后输入用户名，最多等待10秒
        self.tn.read_until(b'Password:', timeout=5)
        self.tn.write(self.password.encode('ascii') + b'\n')
        # 延时两秒再收取返回结果，给服务端足够响应时间
        time.sleep(2)
        # 获取登录结果
        # read_very_eager()获取到的是的是上次获取之后本次获取之前的所有输出
        command_result = self.tn.read_very_eager().decode('ascii')
        if 'Topvision' in command_result:
            logging.info('%s登录成功'%self.host_ip)
            return True
        else:
            logging.warning('%s登录失败，用户名或密码错误'%self.host_ip)
            return False

    def execute_command(self, command):
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(2)

    # 此函数实现执行传过来的命令，并输出其执行结果
    def execute_command_get(self, command):
        # 执行命令
        self.tn.write(command.encode('ascii')+b'\n')
        time.sleep(1)
        # 获取命令结果
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.warning('命令执行结果：\n%s' % command_result)
        return command_result

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"quit\n")


if __name__ == '__main__':
    telnet_client = TelnetClient('120.0.60.5', 'admin', 'admin')
    # 如果登录结果返加True，则执行命令，然后退出
    if telnet_client.login_host():
        telnet_client.execute_command_get('list')
        telnet_client.execute_command('enable')
        telnet_client.execute_command('con ter')
        telnet_client.execute_command('super')
        telnet_client.execute_command('8ik,(OL>')
        telnet_client.execute_command('shell')
        telnet_client.execute_command('cd app')
        out_str = telnet_client.execute_command_get('ls -al | grep output')
        print(re.search(r'\d{6,}', out_str).group())
        telnet_client.logout_host()
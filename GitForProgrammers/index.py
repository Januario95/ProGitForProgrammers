#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
Created at Thur Jul 29 2021 01:46:23

@author: Januario Cipriano
"""


import time

print(time.ctime())

soma = lambda *args: sum(args)

username = 'Januario95'
password = 'Jaci1995'


def welcome():
    print('Welcome')


def login(user, passwd):
    if user == username and passwd == password:
        welcome()
    else:
        print('Login failed')


login(username, password)

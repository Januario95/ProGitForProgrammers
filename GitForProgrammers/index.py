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


class Person(object):
    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    def __str__(self):
        return f'{self.name} - {self.age} years old'


person = Person()
person.name = 'Olga Matias'
person.age = 24
print(person)

class Movie(object):
    def __init__(self, title, duration, release=None):
        self.title = title
        self.duration = duration
        self.release = release



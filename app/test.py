#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 15:52
# @Author  : Cl0udG0d
# @File    : test.py
# @Github: https://github.com/Cl0udG0d
from db import db
def test():
    print('hi')
    db.create_all()


if __name__ == '__main__':
    test()

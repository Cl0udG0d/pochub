#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 9:51
# @Author  : Cl0udG0d
# @File    : config.py
# @Github: https://github.com/Cl0udG0d
import os

DEBUG=False
SECRET_KEY = os.urandom(24)

ALLOWED_EXTENSIONS = set(['py','yaml'])

SQLALCHEMY_DATABASE_URI='sqlite:///database/pochub.db'
SQLALCHEMY_TRACK_MODIFICATIONS=True


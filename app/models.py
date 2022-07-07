#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 10:11
# @Author  : Cl0udG0d
# @File    : models.py
# @Github: https://github.com/Cl0udG0d

from db import db
from datetime import datetime

class Pocs(db.Model):
    __tablename__ = 'pocs'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(256), nullable=False)
    filename=db.Column(db.Text, nullable=False)
    system=db.Column(db.String(256), nullable=False,default="其他")
    categroy=db.Column(db.String(256), nullable=False,default="其他")
    detail=db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

class TempPoc(db.Model):
    __tablename__ = 'temppoc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename=db.Column(db.Text, nullable=False)
    detail=db.Column(db.Text, nullable=False)

def test():
    print('hi')


if __name__ == '__main__':
    test()

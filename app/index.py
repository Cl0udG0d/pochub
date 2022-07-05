#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 15:35
# @Author  : Cl0udG0d
# @File    : index.py.py
# @Github: https://github.com/Cl0udG0d
import os

from flask import render_template,Flask
from init import app


@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search',methods=['POST'])
def search():
    return

@app.route('/test_route')
def test_route():
    return render_template('base.html')

def test():
    print('hi')


if __name__ == '__main__':
    app.run()

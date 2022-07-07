#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 10:19
# @Author  : Cl0udG0d
# @File    : init.py
# @Github: https://github.com/Cl0udG0d

from flask import Flask
from db import db
import config
from models import *


app = Flask(__name__,
            template_folder = './templates',
            static_folder = './static',
    )
app.config.from_object(config)
db.init_app(app)
with app.app_context():
    db.create_all()

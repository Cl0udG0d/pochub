#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/7/5 10:18
# @Author  : Cl0udG0d
# @File    : manage.py
# @Github: https://github.com/Cl0udG0d

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate
from index import app
from models import *


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

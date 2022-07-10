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
    category=db.Column(db.String(256), nullable=False,default="其他")
    detail=db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now)

class TempPoc(db.Model):
    __tablename__ = 'temppoc'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    filename=db.Column(db.Text, nullable=False)
    detail=db.Column(db.Text, nullable=False)


def querTempPocDetail(tid):
    '''
    查询临时poc的文件内容
    :param tid:
    :return:
    '''
    poc = TempPoc.query.filter(TempPoc.id == tid).first()
    return poc.detail

def delTempPocData():
    '''
    删除临时表中的全部数据
    :param tid:
    :return:
    '''
    pocs = TempPoc.query.all()
    [db.session.delete(poc) for poc in pocs]
    db.session.commit()

def insertPocData(poc):
    '''
    插入新poc
    :return:
    '''
    name = poc["filename"].split('.')[0] if "." in poc["filename"] else poc["filename"]
    system = poc["system"]
    category = poc["category"]
    detail = querTempPocDetail(poc["tid"])
    newpoc = Pocs(name=name,filename=poc["filename"],system=system,category=category,detail=detail)
    db.session.add(newpoc)
    db.session.commit()

def querySearchText(text,page):
    pocs=Pocs.query.order_by(Pocs.id.desc()).filter(Pocs.detail.like("%" + text + "%")).paginate(page=page, per_page=10, error_out=False)
    return pocs

def querySearchSystem(system,page):
    pocs = Pocs.query.order_by(Pocs.id.desc()).filter(Pocs.system.like("%" + system + "%")).paginate(page=page, per_page=10, error_out=False)
    return pocs

def querySearchName(name,page):
    pocs = Pocs.query.order_by(Pocs.id.desc()).filter(Pocs.name.like("%" + name + "%")).paginate(page=page, per_page=10, error_out=False)
    return pocs

def querySearchCategory(category,page):
    pocs = Pocs.query.order_by(Pocs.id.desc()).filter(Pocs.category.like("%" + category + "%")).paginate(page=page, per_page=10, error_out=False)
    return pocs

def test():
    print('hi')


if __name__ == '__main__':
    test()

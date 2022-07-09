#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/6/29 15:35
# @Author  : Cl0udG0d
# @File    : index.py.py
# @Github: https://github.com/Cl0udG0d
import json
import os

from flask import(
    render_template,Flask,request,flash,redirect,url_for,make_response
)
from init import app
from models import *
import mimetypes
import config
from werkzeug.utils import secure_filename



@app.route('/index/')
@app.route('/')
def index():
    return render_template('index.html',pochub_active=True)


@app.route('/poclist',methods=['GET'])
@app.route('/poclist/<int:page>',methods=['GET'])
def poclist(page=1,msg=None):
    paginate = Pocs.query.order_by(Pocs.id.desc()).paginate(page=page, per_page=10, error_out=False)
    pocs = paginate.items
    return render_template('poclist.html', pagination=paginate, pocs=pocs,poclist_active=True)

@app.route('/pocDetail/<int:id>',methods=['GET'])
def pocDetail(id=1):
    poc= Pocs.query.filter(Pocs.id == id).first()
    if not poc:
        flash('{} 加载失败'.format(id))
        return redirect(url_for('poclist'))
    return poc.detail

@app.route('/tempPocDetail/<int:id>',methods=['GET'])
def tempPocDetail(id=1):
    poc = TempPoc.query.filter(TempPoc.id == id).first()
    if not poc:
        flash('{} 加载失败'.format(id))
        return redirect(url_for('poclist'))
    return poc.detail


@app.route('/download/<int:id>',methods=['GET'])
def download(id=None):
    try:
        poc = Pocs.query.filter(Pocs.id == id).first()
        response = make_response(poc.detail)
        mime_type = mimetypes.guess_type(poc.filename)[0]
        response.headers['Content-Type'] = mime_type
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(poc.filename.encode().decode('latin-1'))
        return response
    except Exception as err:
        print('download_file error: {}'.format(str(err)))
        flash('{} Download oss files failed!'.format(id))
        return redirect(url_for('poclist'))

@app.route('/result',methods=['GET'])
@app.route('/result/<int:page>',methods=['GET'])
def result(page=1,pocs=None,msg=None):
    paginate = pocs.paginate(page=page, per_page=10, error_out=False)
    pocs = paginate.items
    return render_template('poclist.html', pagination=paginate, pocs=pocs,poclist_active=True)

@app.route('/search',methods=['GET'])
@app.route('/search/<int:page>',methods=['GET'])
def search(page=1,msg=None):
    search_type = request.args.get('search_type')
    # print(search_type)
    search_keyword = request.args.get('search_keyword')
    if search_type=="text":
        paginate=querySearchText(text=search_keyword,page=page)
    elif search_type=="name":
        paginate=querySearchName(search_keyword,page=page)
    elif search_type=="system":
        paginate=querySearchSystem(search_keyword,page=page)
    else:
        paginate=querySearchCategory(search_keyword,page=page)
    pocs = paginate.items
    return render_template('search.html', pagination=paginate, pocs=pocs, poclist_active=True,search_type=search_type,search_keyword=search_keyword)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS

@app.route('/upload',methods=['GET','POST'])
def upload():
    '''
    上传poc到临时表
    :return:
    '''
    if request.method=='GET':
        return render_template('uploadpoc.html',upload_active=True)
    else:
        for file in request.files.getlist('files'):
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                content=file.read()
                temppoc=TempPoc(filename=filename,detail=content)
                db.session.add(temppoc)
        db.session.commit()
        return redirect(url_for('managepoc'))


@app.route('/managepoc',methods=['GET','POST'])
def managepoc():
    '''
    整理poc:从临时表到poc表
    :return:
    '''
    if request.method == 'GET':
        pocs = TempPoc.query.order_by(TempPoc.id.desc()).all()
        return render_template('managepoc.html', upload_active=True,pocs=pocs)
    else:
        '''
        将临时poc修正为正式poc
        '''
        data=request.form.get('jsontext')
        for poc in data.split(';'):
            poc=json.loads(poc)
            insertPocData(poc)
        delTempPocData()
        return redirect(url_for('poclist'))


# @app.route('/test_route')
# def test_route():
#     from db import db
#     poc = Pocs(name="测试",filename='test.py',detail="测试")
#     try:
#         db.session.add(poc)
#     except:
#         db.session.rollback()
#     db.session.commit()
#     db.session.close()
#     return render_template('base.html')

def test():
    print('hi')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8080
    )

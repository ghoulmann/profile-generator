#!/usr/bin/python3.7
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

from flask import render_template, jsonify, redirect, url_for
#from flask_appbuilder.models.sqla.interface import SQLAInterface
#from flask_appbuilder import ModelView, ModelRestApi
from log_generator import generate_access_log
#from . import appbuilder, db
from os.path import join
#from random import randint
from profile_generator import Person, Device
from datetime import timedelta, datetime
import json


"""
    Application wide 404 error handler
"""


@app.route('/')
def welcome():
    person = Person()
    device = Device(person.first_name)
    message = "This is not for you"
    return render_template('index.html', person = person, device = device)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e)
@app.route('/admin/log/<entries>/')
@app.route('/log/<entries>/')
def make_access_log(entries):
    log_entries = generate_access_log(entries, datetime.now()-timedelta(days=1))
    outfile = join('static/','fakeaccesslog.txt')
    fh = open(outfile, '+w')
    for entry in log_entries:
        fh.write(entry+"\r")
    fh.close()
    #return render_template('fake_access_log.html', log=log_entries)
    return redirect(url_for('get_access_log'))
"""View fake logs"""
@app.route('/admin/log/')
@app.route('/log/')
@app.route('/admin/access')
def get_access_log():
    infile = join('static/', 'fakeaccesslog.txt')

    fh = open(infile, 'r')
    #log_entries = fh.readlines()
    log = fh.read()
    fh.close()
    #for i in log_entries:
    #    if len(i) < 2:
    #        log_entries.remove(i)
    #    i = i.replace("\r", "").replace('\n', '').strip()


    return render_template('from_file.html', content=log)
@app.route('/admin/account_dump/')
@app.route('/admin/users/')
def fake_users():
    users = {}
    for i in range(15):
        try:
            a = Person()
        except IndexError:
            a = Person()
        #users[a.username]=a.get_json_str()
        users[a.username] = vars(a) #(a.__dict__, indent=4)
        #users.update(a.json_out())
        del a
    #return render_template('list.html', list = users.items())
    return jsonify(users)
#db.create_all()
if __name__ == "__main__":
    app.run(host='0.0.0.0')


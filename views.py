from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from LogGenerator import AccessLog, generate_access_log
from . import appbuilder, db
from os.path import join
from random import randint
from profiler import Person
from datetime import timedelta, datetime

"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )

"""Fake Log Generation"""
@appbuilder.app.route('/admin/log/<entries>/')
@appbuilder.app.route('/log/<entries>/')
def make_access_log(entries):
    log_entries = generate_access_log(entries, datetime.now()-timedelta(days=1))
    outfile = join('app/static/fake_logs/','fakeaccesslog.txt')
    fh = open(outfile, '+w')
    for entry in log_entries:
        fh.write(entry+'\r')
    fh.close()
    return (render_template('fake_access_log.html', log=log_entries, base_template=appbuilder.base_template, appbuilder=appbuilder
    )
    )
"""View fake logs"""
@appbuilder.app.route('/admin/log/')
@appbuilder.app.route('/log/')
@appbuilder.app.route('/admin/access')
def get_access_log():  
    infile = join('app/static/fake_logs/', 'fakeaccesslog.txt')
    
    fh = open(infile, 'r')
    log = fh.read()
    fh.close()
    log = log.split("\r")
    
    return render_template('fake_access_log.html', log=log)
@appbuilder.app.route('/admin/account_dump/')
@appbuilder.app.route('/admin/users/')
def fake_users():
    users = []
    for i in range(14):
        try:
            a = Person()
        except IndexError:
            a = Person()
        users.append(a.get_json_str())
        del a
    return render_template('list.html', list=users)
db.create_all()

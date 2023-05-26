#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

username = None

@app.context_processor
def inject_globals():
    return {
        "isclever": [
            "2012",
            "2017",
            "2022", 
            "2027", 
            "2032", 
            "2012", 
            "2007", 
            "2002", 
            "2037"
        ]
    }


@app.route('/')
def root():
    return flask.render_template(
        'index.html',
        username=username
    )

@app.route('/name', methods = ['GET', 'POST'])
def hello_name():
    global username
    
    if request.method == 'POST':
        name_param=request.form.get('name')
        username = name_param
        return flask.render_template(
            'index.html',
            username=username
        )
    elif request.method == 'GET':
        if username is None:
            name_param="Гость"
        else:
            name_param = username   

        return flask.render_template(
            'surprise.html',
            name=name_param,
            method=request.method
        )

if __name__ == '__main__':
   app.run(debug = True)

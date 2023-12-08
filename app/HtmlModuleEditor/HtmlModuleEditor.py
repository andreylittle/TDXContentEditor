import os
import time

import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify

import json

HTMLModuleEditor = Blueprint("HtmlModuleEditor",__name__,template_folder="templates", static_url_path="TDXContentEditor/app/HtmlModuleEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\HtmlModuleEditor\static"))

@HTMLModuleEditor.route('/', methods=["GET"])
def HTMLModuleEditorPage():
    with open('app/HTMLModuleEditor/static/fontawesome.json', 'r') as f:
        icons = json.load(f)
    return render_template("HTMLModuleEditor.html", icons=icons['4.7.0'])

@HTMLModuleEditor.route('Template1', methods=['GET', 'POST'])
def Template1Preview():

    dataObject = request.form.to_dict()
    print(dataObject)





    return render_template("UNCW HTML 1.html",
                           **dataObject
                           )
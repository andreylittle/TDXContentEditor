import base64
import os
import time

import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify, Markup
from flask_cors import CORS, cross_origin

import json

HTMLModuleEditor = Blueprint("HtmlModuleEditor",__name__,template_folder="templates", static_url_path="TDXContentEditor/app/HtmlModuleEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\HtmlModuleEditor\static"))

@HTMLModuleEditor.route('/', methods=["GET"])
def HTMLModuleEditorPage():
    with open('app/HTMLModuleEditor/static/fontawesome.json', 'r') as f:
        icons = json.load(f)
    return render_template("HTMLModuleEditor.html", icons=icons['4.7.0'])


@HTMLModuleEditor.route("CardTiles", methods=['GET'])
def test():
    return render_template('UNCW HTML 1.html')


@HTMLModuleEditor.route("DownloadModule", methods=["POST"])
def downloadModule():
    print(request.form.to_dict())
    pass



def getModule():
    pass
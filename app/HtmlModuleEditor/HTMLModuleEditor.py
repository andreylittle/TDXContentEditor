import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify

import json

HTMLModuleEditor = Blueprint("HTMLModuleEditor",__name__, static_folder="static", template_folder="templates")

@HTMLModuleEditor.route('/', methods=["GET"])
def HTMLModuleEditorPage():

    return render_template("HTMLModuleEditor.html")
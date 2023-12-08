import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify
import os
import json

ServiceTemplateEditor = Blueprint("ServiceTemplateEditor",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/ServiceTemplateEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\ServiceTemplateEditor\static"))

@ServiceTemplateEditor.route('/', methods=["GET"])
def ServiceTemplateEditorPage():

    return render_template("ServiceTemplateEditor.html")
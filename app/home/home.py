import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify

import json
import os

home = Blueprint("home",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/home/static", static_folder=os.path.join(os.getcwd() +r"\app\home\static"))

@home.route('/', methods=["GET"])
def homepage():

    return render_template("home.html")


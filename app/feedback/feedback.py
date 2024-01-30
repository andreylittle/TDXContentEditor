import flask
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify

import json
import os

feedback = Blueprint("feedback",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/feedback/static", static_folder=os.path.join(os.getcwd() +r"\app\feedback\static"))

@feedback.route('/', methods=["GET"])
def homepage():
    return render_template("feedback.html")
@feedback.route('/leaveFeedback', methods=["POST"])
def feedbackReview():
    pass

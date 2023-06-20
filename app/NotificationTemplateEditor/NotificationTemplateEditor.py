from collections import OrderedDict
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify
import json
import os

NotificationEditor = Blueprint("NotificationEditor",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/NotificationTemplateEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\NotificationTemplateEditor\static"))


@NotificationEditor.route('/', methods=["GET"])
def getHome():
    DefaultTemplate = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/default-template-preview.html", "r")
    customTemplate1 = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/custom1-template-preview-ConsolidatedTemplate.html", "r")
    customTemplate2 = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/custom2-template-preview-OUITTemplate.html", "r")


    return render_template("defaultTemplateEditor.html", default_template_preview=DefaultTemplate.read(), custom1_template_preview=customTemplate1.read(),custom2_template_preview=customTemplate2.read()  )

@NotificationEditor.route("/DownloadDefaultTemplates", methods=["GET", "POST"])
def download_defaultTemplates():
    return True


@NotificationEditor.route("/DownloadCustom1Templates", methods=["GET", "POST"])
def download_custom1_template():
    return True
@NotificationEditor.route("/DownloadCustom2Templates", methods=["GET", "POST"])
def download_custom2_template():
    return True



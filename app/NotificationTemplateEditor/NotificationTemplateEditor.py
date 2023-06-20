from collections import OrderedDict
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify
import json
import os
import io
import pathlib
import shutil
import zipfile

NotificationEditor = Blueprint("NotificationEditor",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/NotificationTemplateEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\NotificationTemplateEditor\static"))


@NotificationEditor.route('/', methods=["GET"])
def getHome():
    DefaultTemplate = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/default-template-preview.html", "r")
    customTemplate1 = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/custom1-template-preview-ConsolidatedTemplate.html", "r")
    customTemplate2 = open("app/NotificationTemplateEditor/static/PreviewHTMLTemplates/custom2-template-preview-OUITTemplate.html", "r")


    return render_template("defaultTemplateEditor.html", default_template_preview=DefaultTemplate.read(), custom1_template_preview=customTemplate1.read(),custom2_template_preview=customTemplate2.read()  )

@NotificationEditor.route("/DownloadDefaultTemplates", methods=["POST"])
def download_defaultTemplates():
    basepath = os.getcwd()
    data = [{
        'formid': 1,
        'exportFolderBase': f'{basepath}\DefaultExportFolder',
        'mainFolderLocation': fr'{basepath}\NotificationTemplateEditor\static\DefaultTemplates',
        'fields': [request.form.to_dict()],
        'tickets': {
            'CheckboxKey': 'Ticket_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\NotificationTemplateEditor\static\DefaultTemplates\TicketTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\TicketTemplates'

        },
        'knowledgebase': {
            'CheckboxKey': 'KB_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\NotificationTemplateEditor\static\DefaultTemplates\KBTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\KnowledgebaseTemplates'

        },
        'projects': {
            'CheckboxKey': 'Project_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\NotificationTemplateEditor\static\DefaultTemplates\ProjectTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\ProjectTemplates'

        }

    }

    ]
    index = None
    for object in data:
        if int(object['formid']) == int(request.args['formid']):
            index = data.index(object)
            break

    #Need to add section that verifies that no export folder exists and if it does delete it
    export_folder_to_remove = data[index]['exportFolderBase']
    if os.path.exists(export_folder_to_remove):
        try:
            shutil.rmtree(export_folder_to_remove)
        except:
            pass
        return download_defaultTemplates()





    if data[index]['tickets']['CheckboxKey'] in request.form.to_dict():
        get_ticket_templates(data[index]['tickets']['BaseTemplateFolder'], data[index]['exportFolderBase'], data[index]['tickets']['ExportFolder'], request.form.to_dict())


    return True

def get_ticket_templates(workingDirectory, baseExportDirectory, TicketExportDirectory,fields):
    print(workingDirectory, baseExportDirectory, TicketExportDirectory, fields)
    pass








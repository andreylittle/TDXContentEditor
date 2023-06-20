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
        'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates',
        'fields': [request.form.to_dict()],
        'tickets': {
            'CheckboxKey': 'Ticket_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\TicketTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\TicketTemplates'

        },
        'knowledgebase': {
            'CheckboxKey': 'KB_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\KBTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\KnowledgebaseTemplates'

        },
        'projects': {
            'CheckboxKey': 'Project_CheckBox',
            'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\ProjectTemplates',
            'ExportFolder': fr'{basepath}\DefaultExportFolder\ProjectTemplates'

        }

    }

    ]
    index = None
    for object in data:
        if int(object['formid']) == int(request.args['formid']):
            index = data.index(object)
            break

    #Gets the desired export folder and checks to see if it already exists, if it does delete it, and if it does not create it
    export_folder = data[index]['exportFolderBase']
    if os.path.exists(export_folder):
        try:
            shutil.rmtree(export_folder)
        except:
            pass
        return download_defaultTemplates()
    else:
        os.mkdir(export_folder)






    if data[index]['tickets']['CheckboxKey'] in request.form.to_dict():
        get_ticket_templates(data[index]['tickets']['BaseTemplateFolder'], data[index]['exportFolderBase'], data[index]['tickets']['ExportFolder'], request.form.to_dict())

    if data[index]['knowledgebase']['CheckboxKey'] in request.form.to_dict():
        get_kb_templates(data[index]['knowledgebase']['BaseTemplateFolder'], data[index]['exportFolderBase'], data[index]['knowledgebase']['ExportFolder'], request.form.to_dict())

    if data[index]['projects']['CheckboxKey'] in request.form.to_dict():
        get_project_templates(data[index]['projects']['BaseTemplateFolder'], data[index]['exportFolderBase'], data[index]['projects']['ExportFolder'], request.form.to_dict())


    return True


#Working Direcvtory is Base Template Folder contains where base ticket templates exists this is source
#baseExportDirectory is the directory where I should
#Destination will be the Ticket Export Directory
#Fields will be used for the find/replace in the new exported directory
def get_ticket_templates(workingDirectory, baseExportDirectory, TicketExportDirectory,fields):

    print(workingDirectory, baseExportDirectory, TicketExportDirectory, fields)
    shutil.copytree(src=workingDirectory, dst= TicketExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)

    pass


def get_kb_templates(workingDirectory, baseExportDirectory, TicketExportDirectory,fields):

    print(workingDirectory, baseExportDirectory, TicketExportDirectory, fields)
    shutil.copytree(src=workingDirectory, dst= TicketExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)

    pass
def get_project_templates(workingDirectory, baseExportDirectory, TicketExportDirectory,fields):

    print(workingDirectory, baseExportDirectory, TicketExportDirectory, fields)
    shutil.copytree(src=workingDirectory, dst= TicketExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)

    pass





from collections import OrderedDict
from flask import Blueprint, render_template, send_file, request, render_template_string, make_response,jsonify
import json
import os
import io
import pathlib
import shutil
import zipfile
import time

NotificationEditor = Blueprint("NotificationEditor",__name__, template_folder="templates", static_url_path="TDXContentEditor/app/NotificationTemplateEditor/static", static_folder=os.path.join(os.getcwd() +r"\app\NotificationTemplateEditor\static"))


@NotificationEditor.route('/', methods=["GET"])
def getHome():
    return render_template("defaultTemplateEditor.html",

                           )
@NotificationEditor.route("/ChangeLog", methods=["GET"])
def getChangeLog():
    return render_template('changelog.html')
@NotificationEditor.route("/DownloadDefaultTemplates", methods=["POST"])
def download_defaultTemplates():
    basepath = os.getcwd()
    current_time = time.time()

    data = [
        {
            'formid': 1,
            'exportFolderBase': f'{basepath}\exports\DefaultExportFolder - {current_time}',
            'zipFilePath':f'./exports/DefaultExportFolder - {current_time}/',
            'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates',
            'fields': [request.form.to_dict()],
            'tickets': {
                'CheckboxKey': 'Ticket_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\TicketTemplates',
                'ExportFolder': fr'{basepath}\exports\DefaultExportFolder - {current_time}\TicketTemplates'
            },
            'knowledgebase': {
                'CheckboxKey': 'KB_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\KBTemplates',
                'ExportFolder': fr'{basepath}\exports\DefaultExportFolder - {current_time}\KnowledgebaseTemplates'

            },
            'projects': {
                'CheckboxKey': 'Project_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\DefaultTemplates\ProjectTemplates',
                'ExportFolder': fr'{basepath}\exports\DefaultExportFolder - {current_time}\ProjectTemplates'

            }

        },
        {
            'formid': 2,
            'exportFolderBase': f'{basepath}\exports\Custom1ExportFolder - {current_time}',
            'zipFilePath':f'./exports/Custom1ExportFolder - {current_time}/',
            'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom1Templates',
            'fields': [request.form.to_dict()],
            'tickets': {
                'CheckboxKey': 'consolidated_Ticket_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom1Templates\TicketTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom1ExportFolder - {current_time}\TicketTemplates'

            },
            'knowledgebase': {
                'CheckboxKey': 'consolidated_knowledgebase_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom1Templates\KnowledgebaseTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom1ExportFolder - {current_time}\KnowledgebaseTemplates'

            },
            'projects': {
                'CheckboxKey': 'consolidated_project_CheckBox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom1Templates\ProjectTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom1ExportFolder - {current_time}\ProjectTemplates'

            }

        },
        {
            'formid': 3,
            'exportFolderBase': f'{basepath}\exports\Custom2ExportFolder - {current_time}',
            'zipFilePath': f'./exports/Custom2ExportFolder - {current_time}/',
            'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom2Templates',
            'fields': [request.form.to_dict()],
            'tickets': {
                'CheckboxKey': 'custom_2_ticket_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom2Templates\TicketTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom2ExportFolder - {current_time}\TicketTemplates'

            },
            'knowledgebase': {
                'CheckboxKey': 'custom_2_knowledgebase_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom2Templates\KnowledgebaseTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom2ExportFolder - {current_time}\KnowledgebaseTemplates'

            },
            'projects': {
                'CheckboxKey': 'custom_2_project_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom2Templates\ProjectTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom2ExportFolder - {current_time}\ProjectTemplates'

            }

        },
        {
            'formid': 4,
            'exportFolderBase': f'{basepath}\exports\Custom3ExportFolder - {current_time}',
            'zipFilePath': f'./exports/Custom3ExportFolder - {current_time}/',
            'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom3Templates',
            'fields': [request.form.to_dict()],
            'tickets': {
                'CheckboxKey': 'custom_3_ticket_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom3Templates\TicketTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom3ExportFolder - {current_time}\TicketTemplates'

            },
            'knowledgebase': {
                'CheckboxKey': 'custom_3_knowledgebase_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom3Templates\KnowledgebaseTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom3ExportFolder - {current_time}\KnowledgebaseTemplates'

            },
            'projects': {
                'CheckboxKey': 'custom_3_project_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom3Templates\ProjectTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom3ExportFolder - {current_time}\ProjectTemplates'

            }

        },
        {
            'formid': 5,
            'exportFolderBase': f'{basepath}\exports\Custom4ExportFolder - {current_time}',
            'zipFilePath': f'./exports/Custom4ExportFolder - {current_time}/',
            'mainFolderLocation': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom4Templates',
            'fields': [request.form.to_dict()],
            'tickets': {
                'CheckboxKey': 'custom_4_ticket_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom4Templates\TicketTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom4ExportFolder - {current_time}\TicketTemplates'

            },
            'knowledgebase': {
                'CheckboxKey': 'custom_4_knowledgebase_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom4Templates\KnowledgebaseTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom4ExportFolder - {current_time}\KnowledgebaseTemplates'

            },
            'projects': {
                'CheckboxKey': 'custom_4_project_checkbox',
                'BaseTemplateFolder': fr'{basepath}\app\NotificationTemplateEditor\static\CustomTemplates\Custom4Templates\ProjectTemplates',
                'ExportFolder': fr'{basepath}\exports\Custom4ExportFolder - {current_time}\ProjectTemplates'

            }

        }

    ]
    index = None
    for object in data:
        if int(object['formid']) == int(request.args['formid']):
            index = data.index(object)
            print(object)
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




    base_path2 = pathlib.Path(data[index]['zipFilePath'])
    data = io.BytesIO()

    with zipfile.ZipFile(data, mode='w') as z:
        for folder in base_path2.iterdir():
            if folder.is_dir():
                for root, _, files in os.walk(folder):
                    for file in files:
                        file_path = pathlib.Path(root) / file
                        z.write(file_path, arcname=file_path.relative_to(base_path2))

    # with zipfile.ZipFile(data, mode='w') as z:
    #     for folder in base_path2.iterdir():
    #         # print(folder)
    #         z.write(folder)
    #         for file in folder.iterdir():
    #             try:
    #                 for subFile in file.iterdir():
    #                     z.write(subFile)
    #             except:
    #                 pass
    #             # print(file)
    #             z.write(file)

    data.seek(0)
    return send_file(
        data,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'Export.zip'
    )


#Working Direcvtory is Base Template Folder contains where base ticket templates exists this is source
#baseExportDirectory is the directory where I should
#Destination will be the Ticket Export Directory
#Fields will be used for the find/replace in the new exported directory
def get_ticket_templates(workingDirectory, baseExportDirectory, MainExportDirectory,fields):

    shutil.copytree(src=workingDirectory, dst= MainExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)
    all_files = os.listdir(MainExportDirectory)

    for file in all_files:
        FilePath = os.path.join(MainExportDirectory,file)
        with open(FilePath, "r") as file:
            data = file.read()
            for key, value in fields.items():
                data = data.replace(f'[{key}]', value)
        with open(FilePath, "w") as file:
            file.write(data)


    pass


def get_kb_templates(workingDirectory, baseExportDirectory, MainExportDirectory,fields):

    shutil.copytree(src=workingDirectory, dst= MainExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)

    all_files = os.listdir(MainExportDirectory)

    for file in all_files:
        FilePath = os.path.join(MainExportDirectory, file)
        with open(FilePath, "r") as file:
            data = file.read()
            for key, value in fields.items():
                data = data.replace(f'[{key}]', value)
        with open(FilePath, "w") as file:
            file.write(data)
    pass
def get_project_templates(workingDirectory, baseExportDirectory, MainExportDirectory,fields):

    shutil.copytree(src=workingDirectory, dst= MainExportDirectory, symlinks=False, ignore=None, copy_function=shutil.copy2,
                    ignore_dangling_symlinks=False, dirs_exist_ok=False)

    all_folders = os.listdir(MainExportDirectory)

    for Folder in all_folders:
        # print(Folder)
        FilePath = os.path.join(MainExportDirectory, Folder)
        Files_in_Folders = os.listdir(FilePath)
        for file in Files_in_Folders:
            File_inFolder_Path = os.path.join(MainExportDirectory, Folder, file)

            with open(File_inFolder_Path, "r") as file:
                data = file.read()
                for key, value in fields.items():
                    data = data.replace(f'[{key}]', value)
            with open(File_inFolder_Path, "w") as file:
                file.write(data)


    pass





import os
import shutil
basePath = os.getcwd()
export_folder = rf'{basePath}\exports'
all_exportFolders = os.listdir(export_folder)

if len(all_exportFolders) >=1:
    for file in all_exportFolders:
        shutil.rmtree(rf'{export_folder}\{file}')



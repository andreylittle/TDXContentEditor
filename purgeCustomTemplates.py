import os
import shutil
basePath = os.getcwd()
export_folder = rf'{basePath}\exports'
all_files = os.listdir(export_folder)

if len(all_files) >=1:
    for file in all_files:
        os.remove(file)



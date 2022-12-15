import os
import zipfile
import json



# PATH = "C:\\widget"
def modify_manifest(PATH):
    with open(os.path.join(PATH, 'manifest.json'), 'r') as file:
        manifest = json.load(file)

    version = manifest["widget"]["version"].split('.')
    version[-1] = str(int(version[-1])+1)
    version = '.'.join(version)
    manifest["widget"]["version"] = version

    with open(os.path.join(PATH, 'manifest.json'), 'w') as file:
        json.dump(manifest, file)


def remove_widget_zip(PATH):
    try:
        file_to_remove = os.path.join(PATH, "widget.zip")
        os.remove(file_to_remove)
    except Exception:
        print(Exception)

    
def add_files_to_archive(PATH):
    archive = os.path.join(PATH, "widget.zip")
    with zipfile.ZipFile(archive, 'w') as zf:
        for folder, subfolders, files in os.walk(PATH):
            for file in files:
                if file.endswith('.zip'):
                    continue
                zf.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), start=PATH), compress_type = zipfile.ZIP_DEFLATED)
    
    
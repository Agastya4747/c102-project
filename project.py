import os
import shutil
from_dir="C:/Users/agast/Downloads"
to_dir="C:/Users/agast/OneDrive/Desktop/whithatjr/c102/Test"
list_of_files=os.listdir(from_dir)
for file_name in list_of_files:
    name,ext = os.path.splitext(file_name)
    if ext=="":
        continue
    if ext in [".gif",".png",".jpg",".jpeg",".jfif",".txt",".rtf",".pdf",".docx"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"project_file"
        path3=to_dir+"/"+"project_file"+"/"+file_name
        if os.path.exists(path2):
            shutil.copy(path1,path3)
            print("Moving "+file_name)
        else:
            os.mkdir(path2)
            shutil.copy(path1,path3)
            print("Moving "+file_name)
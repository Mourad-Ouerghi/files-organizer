import os
from random import random 
import shutil

folder_path=input("Enter the absolute path of the folder you want to organize : ")
os.chdir(folder_path)
files_list=list()
directories_list=list()
extensions_set=set()
files_list_dest_path=list()
files_list_names_dest_path=list()

for file in os.scandir(folder_path):
    if file.is_dir():
        directories_list.append(str(file.name))
    else:
        files_list_names_dest_path.append(str(file.name))
        files_list.append(file)
        extension=str(file.name).split('.')
        extensions_set.add(extension[len(extension)-1].lower())
for folder in extensions_set:
    if folder not in directories_list:
        os.mkdir(folder)
for file in files_list:
    src_path=file.path
    dest_path=folder_path+"\\"+str(file.name).split('.')[1]
    files_list_dest_path=os.scandir(dest_path)
    if len(list(files_list_dest_path))>0:
        if str(file.name) not in files_list_names_dest_path:
            shutil.move(src_path,dest_path)
        else:
            print("the file ",file.name," already exists in destination")
            print("renaming the file ....")
            path_devided=str(file.path).split('.')
            new_path=path_devided[0]+'-'+str(int(random()*1000000000))+'.'+path_devided[1]
            os.rename(file.path,new_path)
            print("moving the file .....")
            shutil.move(new_path,dest_path)
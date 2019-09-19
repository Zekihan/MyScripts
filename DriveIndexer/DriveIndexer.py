# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""

import os
import shutil
import time
import sys

def create_folder(path):
    try:
        os.mkdir(path)
    except:
        e = sys.exc_info()[0]
        logging (index_path_root+"Log.txt", "Creation of the directory \""+ path +"\" failed due to \"%s\" ." %e)

def create_file(path):
    try:
        f= open(path,"w+")
        f.write("Just for indexing. There is no real data.")
        f.close()
    except:
        e = sys.exc_info()[0]
        logging (index_path_root+"log.txt", "Creation of the file \""+ path +"\" failed due to \"%s\" ." %e)

def index_folder(root, index_path):
    print("Indexing \"%s\" ." % root)
    try:
        for file in os.listdir(root):
            current_path = os.path.join(root, file);
            if os.path.isdir(current_path):
                path = os.path.join(index_path, file)
                create_folder(path)
                index_folder(current_path,path)
            elif os.path.isfile(current_path):
                path = os.path.join(index_path, file)
                create_file(path)
    except PermissionError:
        e = sys.exc_info()[0]
        logging (index_path_root+"log.txt", "Indexing of the directory \""+ root +"\" failed due to \"%s\" ." %e)
    else:
        print("Successfully indexed \"%s\" ." % root)

def delete_folder(path):
    try:
        shutil.rmtree(path)
    except:
        e = sys.exc_info()[0]
        logging (index_path_root+"log.txt", "Deletion of the directory \""+ path +"\" failed due to \"%s\" ." %e)
        
def logging(path,message):
    print (message)
    try:
        localtime = time.asctime( time.localtime(time.time()))
        f= open(path,"a+")
        f.write(localtime+": "+message+"\n")
        f.close()
    except:
        e = sys.exc_info()[0]
        print ("Logging failed due to \"%s\" ." %e)

#root = "D:\\"
#index_path_root= "C:\\Users\\Zekihan\\Desktop\\Index of D"
root = input("Root path to indexed.\n")
index_path_root= input("Give path to indexed files to stored.\n")

if (not index_path_root.endswith('\\')):
   index_path_root += "\\" 

delete_folder(index_path_root)
create_folder(index_path_root)
index_folder(root,index_path_root)
print ("\n\n\n")
print("Indexing finished.For more information check the log file.")
input("Press any key to exit.\n\n\n")
# -*- codin.g: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""
import os
import time
import shutil

def create_shortcut(shortcut_path,target):
    from win32com.client import Dispatch
    
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = target
    shortcut.save()

DAYCOUNT = 14

save_path = "C:\\Users\\Zekihan\\Desktop\\güncel\\"
shows_path = "D:\\Dizi\\"


now = int(time.time())

current = []

shows = os.listdir(shows_path)
for show in shows:
    season = os.listdir(shows_path + show)
    timex = 0
    for i in season:
        if timex < os.path.getmtime(shows_path+show+"\\"+i):
            timex = int(os.path.getmtime(shows_path+show+"\\"+i))
    if ((now-86400*DAYCOUNT) < timex):
        current.append(show)

for i in os.listdir(save_path):
    p = save_path+"\\"+i
    try:
        if os.path.isfile(p):
            os.remove(p)
        else:    ## Show an error ##
            shutil.rmtree(p)
    except Exception as e:
        print ("Error: %s - %s." % (e.filename, e.strerror))        

for i in current:
    create_shortcut(save_path + i + ".lnk", shows_path + i)    




shows = os.listdir(shows_path)
show = os.listdir(shows_path+shows[8])
season = os.listdir(shows_path+shows[8]+"\\"+show[-1])
for i in season:
    timez =  os.path.getmtime(shows_path+shows[8]+"\\"+show[-1]+"\\"+i)
    print(timez)




















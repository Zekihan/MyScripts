#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 05:30:59 2020

@author: zekihan
"""

import os
import sys
import json
import getpass
import instaloader

def get_credentials():
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data", "credentials")
    if os.path.exists(path):
        print("There is credentials do you want to use it (y/n)")
        answer = input()
        if(answer == "y"):
            f= open(path,"r+")
            x = f.read()
            f.close()
            username, password = x.split(",")
        else:
            print("Type username")
            username = input()
            password = getpass.getpass(prompt='Password: ', stream=None)
    else:
        print("Type username")
        username = input()
        password = getpass.getpass(prompt='Password: ', stream=None)
        print("Do you want to save credentials (y/n)")
        answer = input()
        if(answer == "y"):
            f= open(path,"w+")
            f.write(username+","+password)
            f.close()
            print("Credentials saved")
    return username,password

def get_saved(username, password):
    
    try:
        print("Logging in")
        L = instaloader.Instaloader(max_connection_attempts=0)
        
        # Login or load session
        L.login(username, password)        # (login)
        #L.interactive_login(username)      # (ask password on terminal)
    except:
        e = sys.exc_info()[1]
        print("Failed due to \"%s\"." %e)
        os._exit(0)

    profile = instaloader.Profile.from_username(L.context, username)

    print("Getting saved posts")
    a = profile.get_saved_posts()
    print(a)

    set_list = []
    doubles = []
    alll = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data", "test")
    for i in a:
        usrname = i.owner_username
        f= open(path,"a+")
        f.write(usrname+'\n')
        f.close()
    return set_list, doubles, alll

username, password = get_credentials()
set_list, doubles, alll = get_saved(username,password)

answer = "a"
while(answer != "q"):
    print("To get saved accounts press 1")
    print("To get saved more than once press 2")
    print("To quit press q")
    answer = input()
    if(answer == "1"):
        print(set_list)
    if(answer == "2"):
        print(doubles)

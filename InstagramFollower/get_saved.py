#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 05:30:59 2020

@author: zekihan
"""

import os
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
    
    print("Logging in")
    L = instaloader.Instaloader()
    
    # Login or load session
    L.login(username, password)        # (login)
    #L.interactive_login(username)      # (ask password on terminal)

    profile = instaloader.Profile.from_username(L.context, username)

    print("Getting saved posts")
    a = profile.get_saved_posts()

    set_list = []
    doubles = []
    for i in a:
        usrname = i.owner_username
        if usrname not in set_list:
            set_list.append(usrname)
        else:
            if usrname not in doubles:
                doubles.append(usrname)
    
    return set_list, doubles

username, password = get_credentials()
set_list, doubles = get_saved(username,password)

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

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

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "data", "saved.json")

f= open(path,"r+")
lines = f.read()
f.close()

a = json.loads(lines)

username, password = get_credentials()
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

profile = instaloader.Profile.from_username(L.context, 'jameszorander')
followed = profile.get_followees()


f = []
for i in followed:
    f.append(i.username)

s = ''
count = 0
for i in a:
    if i[0] not in f:
        count+=1
        url = 'https://www.instagram.com/' + i[0]
        s += f'<a href="{url}">{count}: {i[0]}</a> <br> <br>'

print(count)

path = os.path.join(my_path, "data", "test.html")
f= open(path,"w+")
f.write(s)
f.close()
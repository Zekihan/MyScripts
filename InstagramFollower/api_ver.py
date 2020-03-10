#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:57:14 2020

@author: zekihan
"""

import os
import getpass
import instaloader
import json

def get_credentials():
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data", "credentials")
    if os.path.exists(path):
        print("There is credentials do you want to use it (y/n)")
        answer = "y"#input()
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
    

username, password = get_credentials()

userlist = ["gamingsetups.tv"]
L = instaloader.Instaloader()
    
# Login or load session
L.login(username, password)        # (login)
#L.interactive_login(username)      # (ask password on terminal)

for i in userlist:
    
    profile = instaloader.Profile.from_username(L.context, i)
    
    if (not profile.followed_by_viewer):
        if not profile.is_private:
            followees = []
            followers = []
            
#            print("Starting to get followees")
#            for followee in profile.get_followees():
#                followees.append(followee.username)
            
            print("Starting to get followers")
            x = profile.get_followers()
            for follower in profile.get_followers():
                followers.append(follower.username)
        if (profile.requested_by_viewer):
            print("require follow")
        else:
            pass
    else:
        followees = []
        followers = []
        
        print("Starting to get followees")
        for followee in profile.get_followees():
            followees.append(followee.username)
        
        print("Starting to get followers")
        for follower in profile.get_followers():
            followers.append(follower.username)
        
    








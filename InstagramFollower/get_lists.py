#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:03:58 2020

@author: zekihan
"""

import os
import getpass
import instaloader
import json


def get_lists(username, password):
    

    followees = []
    followers = []
    
    L = instaloader.Instaloader()
    
    # Login or load session
    L.login(username, password)        # (login)
    #L.interactive_login(username)      # (ask password on terminal)
    
    profile = instaloader.Profile.from_username(L.context, "zekihanazman")
    
    print("Starting to get followees")
    for followee in profile.get_followees():
        followees.append(followee.username)
    
    print("Starting to get followers")
    for follower in profile.get_followers():
        followers.append(follower.username)
    
    return followees, followers


def write_data(followees, followers):
    
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data")
    if not os.path.exists(path):
        os.mkdir(path)
    
    try:
        os.remove(os.path.join(path, "data-old"))
    except FileNotFoundError:
        pass

    try:
        os.rename(os.path.join(path, "data-new"),os.path.join(path, "data-old"))
    except FileNotFoundError:
        pass

    dict4j = {
                "followees" : followees,
                "followers" : followers
                }
    save = json.dumps(dict4j, indent=4)
    f= open(os.path.join(path, "data-new"),"w+")
    f.write(save)
    f.close()

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
            print("tpye username")
            username = input()
            password = getpass.getpass(prompt='Password: ', stream=None)
    else:
        print("tpye username")
        username = input()
        password = getpass.getpass(prompt='Password: ', stream=None)
        print("Do you want to save credentials (y/n)")
        answer = input()
        if(answer == "y"):
            f= open(path,"w+")
            f.write(username+","+password)
            f.close()
            print("Credentials added")
    return username,password
    
    
username, password = get_credentials()
followees, followers = get_lists(username,password)
write_data(followees, followers)








    

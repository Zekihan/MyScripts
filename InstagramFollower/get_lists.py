#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:03:58 2020

@author: zekihan
"""

import os

username = "allthingsdeveloper"
password = "9All@Things@Developer9"

def get_lists(username, password):
    
    import instaloader

    followees = []
    followers = []
    
    L = instaloader.Instaloader()
    
    # Login or load session
    L.login(username, password)        # (login)
    #L.interactive_login(username)      # (ask password on terminal)
    
    profile = instaloader.Profile.from_username(L.context, "zekihanazman")
    
    for followee in profile.get_followees():
        followees.append(followee.username)
    
    for follower in profile.get_followers():
        followers.append(follower.username)
    
    return followees, followers

def get_lists_interactive(username):
    
    import instaloader

    followees = []
    followers = []
    
    L = instaloader.Instaloader()
    
    # Login or load session
#    L.login(username, password)        # (login)
    L.interactive_login(username)      # (ask password on terminal)
    
    profile = instaloader.Profile.from_username(L.context, "zekihanazman")
    
    for followee in profile.get_followees():
        followees.append(followee.username)
    
    for follower in profile.get_followers():
        followers.append(follower.username)
    
    return followees, followers

def write_data(followees, followers):
    
    import json
    
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
    
followees, followers = get_lists(username,password)
write_data(followees, followers)








    

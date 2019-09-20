# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 18:07:43 2019

@author: Zekihan
"""
import os
import json
      
def open_data():
    global mdict
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = (my_path + "\\data\\results.json")
    if not os.path.exists(my_path + "\\data"):
        os.mkdir(my_path + "\\data")
    if os.path.exists(path):  
        f = open(path,"r+")
        old = json.loads(f.read())
        f.close()
        mdict.update(old)

def get_current_both_follow():
    for i in followed_new:
        if i in followers_new :
            both_follow.append(i)
def get_current_i_follow():
    for i in followed_new:
        if i not in followers_new :
            i_follow.append(i)
def get_current_you_follow():
    for i in followers_new:
        if i not in followed_new :
            you_follow.append(i)

def get_losed():
    for i in followers_old:
        if i not in followers_new :
            lostfollowers.append(i)

def get_discarded():
    for i in followed_old:
        if i not in followed_new :
            discardfollowers.append(i)

def get_new_followers():
    for i in followers_new:
        if i not in followers_old :
            new_followers.append(i)           

def get_new_followed():
    for i in followed_new:
        if i not in followed_old :
            new_followed.append(i) 



def init(username):
    open_data()
    x = list(mdict.values())
    d1 = int(x[0][0]["timestamp"])
    d2 = int(x[0][1]["timestamp"])
    followed_old = []
    followers_old = []
    followed_new = []
    followers_new = []
    both_follow = []
    i_follow = []
    you_follow = []
    
    lostfollowers = []
    discardfollowers = []
    new_followers = []
    new_followed = []
    if d1 > d2:
        followed_new = mdict["raw_data"][0]["data"][username]["followed"]
        followers_new = mdict["raw_data"][0]["data"][username]["followers"]
        followed_old = mdict["raw_data"][1]["data"][username]["followed"]
        followers_old = mdict["raw_data"][1]["data"][username]["followers"]
    else:
        followed_new = mdict["raw_data"][1]["data"][username]["followed"]
        followers_new = mdict["raw_data"][1]["data"][username]["followers"]
        followed_old = mdict["raw_data"][0]["data"][username]["followed"]
        followers_old = mdict["raw_data"][0]["data"][username]["followers"]
    both_follow =  mdict["insight"]["both_follow"]
    i_follow = mdict["insight"]["i_follow"]
    you_follow = mdict["insight"]["you_follow"]
    
    lostfollowers = mdict["insight"]["lostfollowers"]
    discardfollowers = mdict["insight"]["discardfollowers"]
    new_followers = mdict["insight"]["new_followers"]
    new_followed = mdict["insight"]["new_followed"]
    return followed_new, followers_new, followed_old, followers_old, both_follow, i_follow, you_follow, lostfollowers, discardfollowers, new_followers,new_followed

def save_results():
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = (my_path + "\\data\\results.json")
    if not os.path.exists(my_path + "\\data"):
        os.mkdir(my_path + "\\data")
    if os.path.exists(path):  
        old = {"raw_data" : mdict["raw_data"], "insight": {
        "both_follow" : both_follow,
		"i_follow" : i_follow,
		"you_follow" : you_follow,
		"lostfollowers" : lostfollowers,
		"discardfollowers" : discardfollowers,
		"new_followers" : new_followers,
		"new_followed" : new_followed
        }}
        save = json.dumps(old, indent=4)
        f= open(path,"w+")
        f.write(save)
        f.close()
      

mdict = {}

username = "zekihanazman"
followed_new, followers_new, followed_old, followers_old, both_follow, i_follow, you_follow, lostfollowers, discardfollowers, new_followers,new_followed = init(username)

get_current_both_follow()
get_current_i_follow()
get_current_you_follow()
get_losed()
get_discarded()
get_new_followers()
get_new_followed()

save_results()
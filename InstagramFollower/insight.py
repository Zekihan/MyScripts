#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:26:43 2020

@author: zekihan
"""

import os
import json
      
def open_data():
    
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "data")
    if not os.path.exists(path):
        print("no data")
        exit(1)
    if os.path.exists(os.path.join(path, "data-new")):
        f = open(os.path.join(path, "data-new"),"r+")
        new = json.loads(f.read())
        f.close()
    else:
        new = []
    if os.path.exists(os.path.join(path, "data-old")):
        f = open(os.path.join(path, "data-old"),"r+")
        old = json.loads(f.read())
        f.close()
    else:
        old = []
    
    return new, old

def get_same(first_list,second_list):
    l = []
    for i in first_list:
        if i in second_list :
            l.append(i)
    return l
    
def get_diffrence(first_list,second_list):
    l = []
    for i in first_list:
        if i not in second_list :
            l.append(i)
    return l

new, old = open_data();

friends = get_same(new['followees'],new['followers'])

not_followers = get_diffrence(new['followees'],new['followers'])

blind_followers = get_diffrence(new['followers'],new['followees'])

new_followers = get_diffrence(new['followers'],old['followers'])

new_followees = get_diffrence(new['followees'],old['followees'])

lost_followers = get_diffrence(old['followers'],new['followers'])

unfollowed = get_diffrence(old['followees'],new['followees'])












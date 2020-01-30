#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 01:26:43 2020

@author: zekihan
"""

import os
import json
      
def open_data():
    
    print("Opening data")
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

print("Creating insight on data")
friends = get_same(new['followees'],new['followers'])

not_followers = get_diffrence(new['followees'],new['followers'])

blind_followers = get_diffrence(new['followers'],new['followees'])

new_followers = get_diffrence(new['followers'],old['followers'])

new_followees = get_diffrence(new['followees'],old['followees'])

lost_followers = get_diffrence(old['followers'],new['followers'])

unfollowed = get_diffrence(old['followees'],new['followees'])

answer = "a"
while(answer != "q"):
    print("To get not following press 1")
    print("To get mutually following press 2")
    print("To get fans press 3")
    print("To get new followers press 4")
    print("To get new followed press 5")
    print("To get lost followers press 6")
    print("To get unfolloweds press 7")
    print("To get followers press 8")
    print("To get followees press 9")
    print("To quit press q")
    answer = input()
    if(answer == "1"):
        print(not_followers)
    if(answer == "2"):
        print(friends)
    if(answer == "3"):
        print(blind_followers)
    if(answer == "4"):
        print(new_followers)
    if(answer == "5"):
        print(new_followees)
    if(answer == "6"):
        print(lost_followers)
    if(answer == "7"):
        print(unfollowed)
    if(answer == "8"):
        print(new['followers'])
    if(answer == "9"):
        print(new['followees']) 














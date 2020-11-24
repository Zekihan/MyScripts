# -*- codin.g: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""
import requests
import json
from bs4 import BeautifulSoup

def get_urls():

    f = open("C:\\Users\\Zekihan\\Desktop\\bookmarks_11_7_20.html")
    lines = f.readlines()
    f.close()

    urls = []
    for i in lines:
        urls.append(i.split("<DT><A HREF=\"")[1].split("\" ADD_DATE=\"")[0])
    
    return urls

def get_content(url):

    response = requests.get(url)
    image_url = response.text.split("<img itemprop=\"image\"")[1].split("src=\"")[1].split("\" />")[0]
    image_url = "https://www.anime-planet.com/" + image_url
    try:
        description = response.text.split("<div class=\"pure-1 md-3-5\">\n<div><p>")[1].split("</p></div>")[0]
        description = BeautifulSoup(description, features="html.parser").get_text()
    except:
        description = "To be updated"

    tags = []
    tags2 = ""
    tags_unparsed = response.text.split("<div class=\"tags \">")[1].split("<ul>")[1].split("</ul>")[0].split("<a href=\"/manga/tags")
    for i in tags_unparsed[1:]:
        tag = i.split(" data-tooltip-entry=\"manga\">\n")[1].split("\n</a>\n</li>")[0]
        tag = BeautifulSoup(tag, features="html.parser").get_text()
        tags.append(tag)
        tags2 += tag + ","
    tags2 = tags2[:-1]

    try:
        ch = response.text.split("<div class=\"pure-1 md-1-5\">\n")[1].split("\n</div>")[0].split("Ch:")[1].split("+")[0]
        ch = BeautifulSoup(ch, features="html.parser").get_text()
    except:
        ch = 0
    try:
        name = response.text.split("<h1 itemprop=\"name\">")[1].split("</h1>")[0]
        name = BeautifulSoup(name, features="html.parser").get_text()
    except:
        name = response.text.split("<h1 itemprop=\"name\" class=\"long\">")[1].split("</h1>")[0]
        name = BeautifulSoup(name, features="html.parser").get_text()
    year = response.text.split("iconYear'> ")[1].split("</span>")[0]
    status = "Publishing"
    if("?" not in year):
        status = "Completed"

    result = {
        "url": url,
        "img": image_url,
        "description": description,
        "tags": tags2,
        "published": ch,
        "read": 0,
        "name": name,
        "status": status,
        "Personel_Status": "Want To Read"
    }
    return result

def get_result():
    urls = get_urls()
    result = []
    errored = []
    for url in urls:
        try:
            result.append(get_content(url))
        except:
            errored.append(url)
        
    return result, errored

result, error = get_result()

save = json.dumps(result, indent=4)

f = open("test2.json","w")
f.write(save)
f.close()

print(error)









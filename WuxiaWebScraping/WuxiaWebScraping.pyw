# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""

from tkinter import Tk,Scrollbar,RIGHT,Listbox,END,re,mainloop,Y,BOTH
import webbrowser

def callback(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    if index%4 == 1:
        url = w.get(index)
        webbrowser.open_new(url)
  
def get_recent_updates():
    import requests
    from bs4 import BeautifulSoup
    import time
    
    url = "https://www.wuxiaworld.com"
    response = requests.get(url)
    
    recents = []
    t = response.text.split("<h3>Most Recently Updated</h3>\n</div>\n<div class=\"section-content\">\n<table class=\"table table-novels\">\n<thead class=\"hidden-xs\">\n<tr>\n<th>Title</th>\n<th>Release</th>\n<th>Translator</th>\n<th>Time</th>\n</tr>\n</thead>\n<tbody>")
    t = t[1].split("<tr>")
    
    for i in range(1,len(t)):
        item = []
        x = t[i].split("<td>\n<span class=\"title\">\n<a href=\"")[1].split("\">")[1].split("</a>")[0]
        soup = BeautifulSoup(x, "html.parser")
        item.append(soup.text)
        x = t[i].split("<div class=\"visible-xs-inline\">\n<a class=\"")[1].split("\" href=\"")[1].split("\">")
        item.append(url + x[0])
        x = x[1].split("</a>")
        soup = BeautifulSoup(x[0], "html.parser")
        item.append(soup.text[1:-1]) 
        x = t[i].split("data-timestamp=\"")[1].split("\">")[0]
        item.append(x)
        recents.append(item)
    
    ts = time.time()
    top = Tk() 
    top.geometry("800x600") 
    sb = Scrollbar(top)  
    sb.pack(side = RIGHT, fill = Y)  
    mylist = Listbox(top, yscrollcommand = sb.set )
    for recent in recents:
        mylist.insert(END, recent[0])
        mylist.insert(END, recent[1])
        char_list = recent[2]
        re_pattern = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)
        filtered_string = re_pattern.sub(u'\uFFFD', char_list) 
        mylist.insert(END, filtered_string)
        diff = (int(ts)-int(recent[3]))
        if diff>3600:
            hour = str(int(diff/3600))
            mylist.insert(END, "%s hour ago.\n" %hour)
        elif diff>(24*3600):
            day = str(int(diff/(24*3600)))
            mylist.insert(END, "%s day ago.\n" %day)
        else:
            minute = str(int(diff/60))
            mylist.insert(END, "%s minute ago.\n" %minute)
        
        mylist.bind('<<ListboxSelect>>', callback)
    
    
    mylist.pack( fill = BOTH, expand=True)  
    sb.config( command = mylist.yview )  
      
    mainloop()
import sys

def main():
    try:
        get_recent_updates()
    except:
        e = sys.exc_info()[1]
        path = "C://Users//Zekihan//Desktop//Coding//MyScripts//log.txt"
        message = "Failed due to \"%s\"." %e
        f= open(path,"a+")
        f.write("%s \n" %message)
        f.close()
        main()
        
main()
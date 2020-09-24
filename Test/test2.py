# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:26:17 2020

@author: Zekihan
"""

import requests

y = 0 
url = "https://readnovelfull.com/ajax/latest-novels"
response = requests.post(url,json={'p':2})
x = response.text.split('<div class="row" itemscope=""> <div class="col-xs-9 col-sm-6 col-md-5 col-title"> <span class="glyphicon glyphicon-chevron-right"></span> ')
for i in x:
    try:
        print(i.split('title="')[1].split('">')[0])
        y+=1
    except:
        pass

print(y)

url = 'https://readnovelfull.com/latest-release-novel?page=2'
response = requests.get(url)
# print(response.text)

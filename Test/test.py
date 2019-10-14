# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""

path = "C:\\Users\\Zekihan\\Desktop\\logcat.txt"

f = open(path,"r+", encoding="ISO-8859-1")
logs = f.readlines()
f.close()

data = []
for log in logs:
    if "COMMAND_GET_CURRENT_BATTERY_LEVEL " in log:
        data.append(log)

data_l1 = []
data_l2 = []
data_l3 = []
data_l4 = []
data_l5 = []

for i in data:
    if i.split("Battery level : ")[1].split(" charging state : ")[0] == "1":
        data_l1.append(int(i.split(" battVoltage : ")[1].split(",  Battery level : ")[0]))
    if i.split("Battery level : ")[1].split(" charging state : ")[0] == "2":
        data_l2.append(int(i.split(" battVoltage : ")[1].split(",  Battery level : ")[0]))
    if i.split("Battery level : ")[1].split(" charging state : ")[0] == "3":
        data_l3.append(int(i.split(" battVoltage : ")[1].split(",  Battery level : ")[0]))
    if i.split("Battery level : ")[1].split(" charging state : ")[0] == "4":
        data_l4.append(int(i.split(" battVoltage : ")[1].split(",  Battery level : ")[0]))
    if i.split("Battery level : ")[1].split(" charging state : ")[0] == "5":
        data_l5.append(int(i.split(" battVoltage : ")[1].split(",  Battery level : ")[0]))

abs_max = max(data_l5)
abs_low = min(data_l1)
print(abs_low)
print(abs_max)
x = abs_max - abs_low

for i in data_l1:
    print(round((i - abs_low)/x*100))
    
print("\n")

for i in data_l2:
    print(round((i - abs_low)/x*100))
        
print("\n")

for i in data_l3:
    print(round((i - abs_low)/x*100))
    
print("\n")

for i in data_l4:
    print(round((i - abs_low)/x*100))
    
print("\n")

for i in data_l5:
    print(round((i - abs_low)/x*100))





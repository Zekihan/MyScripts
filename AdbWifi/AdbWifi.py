# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 20:35:00 2019

@author: Zekihan
"""

from subprocess import check_output
import os

ip = "192.168.1.199:5555"
x = check_output(f"adb connect {ip}", shell=True).decode()
if(x == f"already connected to {ip}"+os.linesep):
    print(f"already connected to {ip}")
elif(x == f"cannot connect to {ip}: No connection could be made because the target machine actively refused it. (10061)"+os.linesep):
    print(f"cannot connect to {ip}")
    input("press any key to exit.")
elif(x == f"connected to {ip}"+os.linesep):
    print(f"connected to {ip}")
    input("press any key to exit.")
else:
    print("Error but no idea")
    input("press any key to exit.")
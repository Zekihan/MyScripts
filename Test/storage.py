# -*- codin.g: utf-8 -*-
"""
Created on Mon Jul 20 15:26:17 2019

@author: Zekihan
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

import os
import json
import random
import string

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "macro.json")

global mdict
mdict = {}

f = open(path,"r+")
base = json.loads(f.read())
f.close()
mdict.update(base)

def rand11():
    l = []
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.digits))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.digits))
    l.append(random.choice(string.ascii_uppercase))
    l.append(random.choice(string.ascii_uppercase))
    return l

def create(l, num):
    count = 0
    mdict["Name"] = f"Macro ({num})"
    for i in range(14,42,3):
        mdict["Events"][i]["KeyName"] = l[count]
        mdict["Events"][i+1]["Msg"] = f'start_{l[count].lower()}_end del=0 enter=0'
        mdict["Events"][i+2]["KeyName"] = l[count]
        count += 1
    
    save = json.dumps(mdict, indent=4)
    path = os.path.join(my_path, "result", f"macro ({num}).json")
    f= open(path,"w+")
    f.write(save)
    f.close()

for i in range(1 ,101):
    l = rand11()
    create(l, i)
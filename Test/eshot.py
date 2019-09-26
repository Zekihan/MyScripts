# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 15:26:17 2019

@author: Zekihan
"""

import requests

def get_time_table(busId, direction1="", direction2=""):

    time_table = []

    url = f"https://www.eshot.gov.tr/tr/UlasimSaatleri/288?bisikletAparatliMi=False&hatId={busId}&hatYon=0"
    response = requests.get(url)

    content = response.text.split('<div class="col-md-4 col-sm-12 col-xs-12">')

    for j in range(1,len(content)):
        time_part = content[j]
        c = time_part.split('<ul class="timescape">')
        if len(c) == 3:
            temp = []
            direct1 = []
            direct1_raw = c[1]
            time_table1 = direct1_raw.split('<span class="pull-left">');
            for i in time_table1:
                direct1.append(i.split('</span>')[0])
            temp.append(direct1[1::])
    
            direct2 = []
            direct2_raw = c[2]
            time_table2 = direct2_raw.split('<span class="pull-left">');
            for i in time_table2:
                direct2.append(i.split('</span>')[0])
            temp.append(direct2[1::])
            time_table.append(temp)
        else:
            temp = [[],[]]
            time_table.append(temp)

    if direction1 == "":
        direction1 = direct1[0].split('<h4>')[1].split('</h4>')[0].split(' ')[0].lower()

    if direction2 == "":
        direction2 = direct2[0].split('<h4>')[1].split('</h4>')[0].split(' ')[0].lower()

    result_dict = {
                    f"bus_{busId}" :
                        {
                            "saturday" :
                                {
                                    f"{direction1}_{direction2}" : time_table[1][0],
                                    f"{direction2}_{direction1}" : time_table[1][1]
                                },
                            "sunday" :
                                {
                                    f"{direction1}_{direction2}" : time_table[2][0],
                                    f"{direction2}_{direction1}" : time_table[2][1]
                                },
                            "weekday" :
                                {
                                    f"{direction1}_{direction2}" : time_table[0][0],
                                    f"{direction2}_{direction1}" : time_table[0][1]
                                }
                        }
                    }

    return result_dict


#busId = input("Write the bus id.")
busId = 882

#default tags
result = get_time_table(busId)
#custom tags
result = get_time_table(busId,"balıklıova","izmir")

print(result)

#input("Press any key to exit.")






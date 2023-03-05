# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 15:59:31 2023

@author: yunfa
"""

import pandas as pd
def STC():
    areas=['Barking and Dagenham','Barnet','Bexley','Brent',\
           'Bromley','Camden','Croydon','Ealing','Enfield',\
               'Greenwich','Hackney and City of London','Hammersmith and Fulham',\
                   'Haringey','Harrow','Havering','Hillingdon','Hounslow','Islington',\
                       'Kensington and Chelsea','Kingston upon Thames','Lambeth','Lewisham','Merton',\
                           'Newham','Redbridge','Richmond upon Thames','Southwark','Sutton',\
                               'Tower Hamlets','Waltham Forest','Wandsworth','Westminster']
    f=pd.read_csv('sites_and_codes.csv')
    codes=[]
    for i in range(len(areas)):   
        area_code=[]
        for j in range(len(f)):
            line=f.iloc[j]
            current=line['site']
            if len(current)>len(areas[i]):
                if current[:len(areas[i])]==areas[i]:
                    area_code.append(line['code'])
        
        if areas[i]=='Hackney and City of London':
            for j in range(len(f)):
                line=f.iloc[j]
                current=line['site']
                if len(current)>len('City of London'):
                    if current[:len('City of London')]=='City of London':
                        area_code.append(line['code'])
                elif len(current)>len('Hackney'):
                    if current[:len('Hackney')]=='Hackney':
                        area_code.append(line['code'])
            
        codes.append(area_code)
    return areas,codes

        
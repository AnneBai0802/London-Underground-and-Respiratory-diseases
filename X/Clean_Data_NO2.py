# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 02:55:54 2023

@author: yunfa
"""

import pandas as pd
import numpy as np
import math
import Site_To_COde


def clean_NO2():
    '''
    cleans the NO2 file

    Returns
    -------
    NO2 : TYPE numpy array
        DESCRIPTION. gives the average NO2 emission of each borough over the year

    '''
    
    areas,codes=Site_To_COde.STC()
    #read data from file
    data=pd.read_csv('data_2015_2023.csv')
    
    #divide into boroughs
    NO2=np.array([0.0 for i in range(len(areas))])
    start=0
    length=len(data)
    for i in range(len(areas)):
        total=0
        count=0
        records=[]
        print(codes[i])
        if areas[i]=='Hackney and City of London':
            
            for j in range(0,length):
                current=data.iloc[j]
                if current['code'] in codes[i]:
                    records.append(current['no2'])
        else:
            for j in range(start,length):
                current=data.iloc[j]
                if current['code'] in codes[i]:
                    records.append(current['no2'])
                    start=j
                elif len(records)!=0:
                    start=j
                    break

        #calculate average NO2 level over 2021
        for j in range(len(records)):
            value=records[j]
            if not math.isnan(value):
                total+=value
                count+=1
            
        
        if count==0:
            Average_NO2=0
        else:
            Average_NO2=round(total/count,4)
        try:
            NO2[i]=Average_NO2
        except:
            NO2[i]=0
        print(NO2)
        
        
    return areas,NO2
   

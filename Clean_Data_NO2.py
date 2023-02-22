# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 02:55:54 2023

@author: yunfa
"""

import pandas as pd
import numpy as np
import math


def clean_NO2():
    '''
    cleans the NO2 file

    Returns
    -------
    NO2 : TYPE numpy array
        DESCRIPTION. gives the average NO2 emission of each borough over the year

    '''
    #read data from file
    data=pd.read_csv('NO2_london_boroughs.csv')
    
    #divide into boroughs
    NO2=np.array([0.0 for i in range(32)])
    for i in range(32):
        total=0
        count=0
        records=data[data['Site']==i+1]
        
        #calculate average NO2 level over 2021
        for j in range(len(records)):
            value=records.iloc[j]['Value']
            if not math.isnan(value):
                total+=value
                count+=1
            else:
                total+=0
        
        if count==0:
            Average_NO2=0
        else:
            Average_NO2=round(total/count,4)
        try:
            NO2[i]=Average_NO2
        except:
            NO2[i]=0
        
        
    return NO2
    

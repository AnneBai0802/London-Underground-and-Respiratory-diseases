# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


def clean_Covid():
    '''
    cleans the data files

    Returns
    -------
    index : numpy array
        DESCRIPTION. Index value used to determine
    Name_Boroughs : umpy array
        DESCRIPTION. Name of corresponding boroughs
    Percentage_Death_Boroughs : numpy array
        DESCRIPTION. Number of death from COVID out of 1000 people for each borough

    '''

    #read data from the files
    deaths=pd.read_csv('phe_deaths_london_boroughs.csv')
    cases=pd.read_csv('phe_cases_london_boroughs.csv')
    
    
    
    #select row numbers to which date is in the year of 2021
    begin_deaths=deaths[deaths['date'] == '2021-01-01'].index[0]
    end_deaths=deaths[deaths['date'] == '2022-01-01'].index[0]
    begin_cases=cases[cases['date'] == '2021-01-01'].index[0]
    end_cases=cases[cases['date'] == '2022-01-01'].index[0]
    
    #Divide into boroughs by area code
    Death_Boroughs=np.array([])
    Cases_Boroughs=np.array([])
    Name_Boroughs=np.array([])
    index=np.array([])
    for i in range(2,34):
        No_Death=0
        No_Case=0
        if i<10:
            code='E0900000'+str(i)
        else:
            code='E090000'+str(i)
        for j in range(begin_deaths,end_deaths):
            if deaths.iloc[j]['area_code']==code:
                No_Death+=int(deaths.iloc[j]['new_deaths'])
                Name=deaths.iloc[j]['area_name']
        for j in range(begin_cases,end_cases):
            if cases.iloc[j]['area_code']==code:
                No_Case+=int(cases.iloc[j]['new_cases'])
        Death_Boroughs=np.append(Death_Boroughs,No_Death)
        Cases_Boroughs=np.append(Cases_Boroughs,No_Case)
        Name_Boroughs=np.append(Name_Boroughs,Name)
        index=np.append(index,i-2)
    
    #Calculate percentage death    
    Percentage_Death_Boroughs=Death_Boroughs*1000/Cases_Boroughs
    
    #return value
    return index,Name_Boroughs,Percentage_Death_Boroughs


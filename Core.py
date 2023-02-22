# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 03:46:28 2023

@author: yunfa
"""
def linear(X,m,c):
    return m*X+c
import Clean_Data_Covid
import Clean_Data_NO2
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from operator import itemgetter

NO2=Clean_Data_NO2.clean_NO2()
Name_Boroughs,Percentage_Death_Boroughs=Clean_Data_Covid.clean_Covid()

#sort the values in terms of NO2 level
matrix=[]
for i in range(len(NO2)):
    matrix.append([NO2[i],Percentage_Death_Boroughs[i],Name_Boroughs[i]])
matrix=sorted(matrix, key=itemgetter(0))
NO2=np.array([matrix[i][0] for i in range(len(matrix))])
Percentage_Death_Boroughs=np.array([matrix[i][1] for i in range(len(matrix))])
Name_Boroughs=np.array([matrix[i][2] for i in range(len(matrix))])

po,po_cov=curve_fit(linear,NO2,Percentage_Death_Boroughs)
plt.plot(NO2,Percentage_Death_Boroughs,'x',label='Recorded Data')
plt.plot(NO2,linear(NO2,po[0],po[1]),'-',label='Simulated line, gradient='+str(round(po[0],4)))
plt.xlabel('Average $NO_{2}$ /$\mu g m^{-3}$')
plt.ylabel('Death per 1000 people')
plt.legend()
plt.savefig('Percentage Death against NO2 in 2021',dpi=500)
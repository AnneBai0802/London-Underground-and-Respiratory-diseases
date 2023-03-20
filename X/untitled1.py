# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:24:39 2023

@author: 44785
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Clean_Data_Covid
import scipy as sp

#%%

data_apc = pd.read_csv('LEAI_1.csv')
data_covc = pd.read_csv('phe_cases_london_boroughs.csv')
data_covd = pd.read_csv('phe_deaths_london_boroughs.csv')
data_pop = pd.read_csv('population.csv')

#%%

covid = Clean_Data_Covid.clean_Covid()

#%%

z = data_pop.to_numpy()
x = data_apc.to_numpy()

pop = z[2:34,3]
pop = pop.astype(int)

# CO2 = x[1,1:],x[6,1:], x[11,1:]
# PM2 =  x[2,1:], x[7,1:], x[12,1:]
# PM10 =  x[3,1:], x[8,1:], x[13,1:]
# NOX =  x[4,1:], x[9,1:], x[14,1:]

ratio_deaths = covid[1]/pop
ratio_cases = covid[2]/pop

yvals1 = (x[1,1:].astype(float) + x[6,1:].astype(float) + x[11,1:].astype(float))/3
yvals2 = (x[2,1:].astype(float) + x[2,1:].astype(float) + x[2,1:].astype(float))/3
yvals3 = (x[3,1:].astype(float) + x[2,1:].astype(float) + x[2,1:].astype(float))/3
yvals4 = (x[4,1:].astype(float) + x[2,1:].astype(float) + x[2,1:].astype(float))/3 

#%%
fig = plt.figure()

fig.suptitle("Correlation Investigation in each Greater London Borough", fontsize=16)

fig.text(0.5, 0.04, 'Mean Concentration (2010-2019) in each GLB [tonnes/annum]', ha='center',fontsize=12)
fig.text(0.04, 0.45, 'Cases of Covid19 [per borough population]', va='top', rotation='vertical',fontsize=12)
fig.text(0.04, 0.55, ' Deaths from Covid19[per borough population]', va='bottom', rotation='vertical',fontsize=12)

ax1 = fig.add_subplot(2, 4, 1)
ax2 = fig.add_subplot(2, 4, 2)
ax3 = fig.add_subplot(2, 4, 3)
ax4 = fig.add_subplot(2, 4, 4)
ax5 = fig.add_subplot(2, 4, 5)
ax6 = fig.add_subplot(2, 4, 6)
ax7 = fig.add_subplot(2, 4, 7)
ax8 = fig.add_subplot(2, 4, 8)

fit1, cov1 = np.polyfit(yvals1,ratio_deaths,1,cov=True)
aq1 = sp.poly1d(fit1)
fit2, cov2 = np.polyfit(yvals2,ratio_deaths,1,cov=True)
aq2 = sp.poly1d(fit2)
fit3, cov3= np.polyfit(yvals3,ratio_deaths,1,cov=True)
aq3 = sp.poly1d(fit3)
fit4, cov4 = np.polyfit(yvals4,ratio_deaths,1,cov=True)
aq4 = sp.poly1d(fit4)

fit5, cov5 = np.polyfit(yvals1,ratio_cases,1,cov=True)
aq5 = sp.poly1d(fit5)
fit6, cov6 = np.polyfit(yvals2,ratio_cases,1,cov=True)
aq6 = sp.poly1d(fit6)
fit7, cov7 = np.polyfit(yvals3,ratio_cases,1,cov=True)
aq7 = sp.poly1d(fit7)
fit8, cov8 = np.polyfit(yvals4,ratio_cases,1,cov=True)
aq8 = sp.poly1d(fit8)

ax1.plot(yvals1,ratio_deaths,'x',color ='red', label='CO2')
ax1.plot(yvals1,aq1(yvals1),color='black')
ax2.plot(yvals2,ratio_deaths,'x',color ='blue', label='PM2')
ax2.plot(yvals2,aq2(yvals2),color='black')
ax3.plot(yvals3,ratio_deaths,'x',color ='green', label='PM10')
ax3.plot(yvals3,aq3(yvals3),color='black')
ax4.plot(yvals4,ratio_deaths,'x',color ='orange', label='NOX')
ax4.plot(yvals4,aq4(yvals4),color='black')

ax5.plot(yvals1,ratio_cases,'x',color ='red', label='CO2')
ax5.plot(yvals1,aq5(yvals1),color='black')
ax6.plot(yvals2,ratio_cases,'x',color ='blue', label='PM2')
ax6.plot(yvals2,aq6(yvals2),color='black')
ax7.plot(yvals3,ratio_cases,'x',color ='green', label='PM10')
ax7.plot(yvals3,aq7(yvals3),color='black')
ax8.plot(yvals4,ratio_cases,'x',color ='orange', label='NOX')
ax8.plot(yvals4,aq8(yvals4),color='black')


ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()
ax6.legend()
ax7.legend()
ax8.legend()
plt.show()

#%%

fig,ax = plt.subplots()
ax.plot(covid[0], yvals1,color="red",ls='--',marker="o",label='CO2')
#ax.plot(covid[0], yvals2,color="orange",ls='--',marker="o",label='PM2')
#ax.plot(covid[0], yvals3,color="yellow",ls='--',marker="o",label='PM10')
#ax.plot(covid[0], yvals4,color="pink",ls='--',marker="o",label='NOX')
#ax.set_xlabel("Boroughs in London", fontsize = 14)
ax.set_ylabel("Mean Concentration - NOX [tonnes/annum]",color="red",fontsize=10)
ax2=ax.twinx()
ax2.plot(covid[0], ratio_deaths,color="blue",marker="o")
#ax2.plot(covid[0], ratio_cases,color="green",marker="o")
ax2.set_ylabel("% of Borough that Died from COVID19",color="blue",fontsize=10)
plt.title('Correlation Examination - C02')
plt.gcf().autofmt_xdate()
plt.show()

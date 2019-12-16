# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 14:34:25 2019

@author: mouna
"""

import matplotlib.pyplot as plt
#from sklearn import data1sets
from sklearn.cluster import KMeans
 
import pandas as pd
import numpy as np
 
import os
os.chdir('C:\\internship\\Slack docs')

data1 = pd.read_csv("drill_chisel.csv")

data1 = pd.DataFrame(data1)
print(data1.columns)

data1.State = pd.Categorical(data1.State)
data1['Targets'] = data1.State.cat.codes


data2 = pd.read_csv("hilti_20191212 (1).csv")

data2 = pd.DataFrame(data2)
print(data2.columns)

data2.State = pd.Categorical(data2.State)
data2['Targets'] = data2.State.cat.codes

data1_drill = data1[data1['State']=='Drill']
data2_drill = data2[data2['State']=='Drill']


colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(10,5))
plt.scatter(data1_drill.current_avg, data1_drill.voltage_avg, c=colormap[data1_drill.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Current')
plt.ylabel('Voltage') 
#plt.show()


colormap = np.array(['red', 'lime', 'black'])
plt.figure(figsize=(10,5))
plt.scatter(data2_drill.current_avg, data2_drill.voltage_avg, c=colormap[data2_drill.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Current')
plt.ylabel('Voltage') 
plt.show()


plt.scatter(data1_drill.current_avg, data1_drill.voltage_avg, color='black', s=40)
plt.scatter(data2_drill.current_avg, data2_drill.voltage_avg, color='red', s=40)
plt.title('Real Classification')
plt.xlabel('Current')
plt.ylabel('Voltage') 
plt.show()


x_data1_drill = data1_drill.loc[:,['voltage_avg', 'current_avg', 'power_factor_avg', 'frequency_avg','power_avg']]
 
y_data1_drill = data1_drill.loc[:,['Targets']]

colormap = np.array(['red', 'lime', 'black'])
 
model_data1_drill = KMeans(n_clusters=2)
model_data1_drill.fit(x_data1_drill)

model_data1_drill.labels_

plt.figure(figsize=(10,5))

colormap = np.array(['red', 'lime'])

plt.subplot(1, 2, 1)
plt.scatter(x_data1_drill.current_avg, x_data1_drill.voltage_avg, c=colormap[y_data1_drill.Targets], s=40)
plt.title('Real Classification')

plt.subplot(1, 2, 2)
plt.scatter(x_data1_drill.current_avg, x_data1_drill.voltage_avg, c=colormap[model_data1_drill.labels_], s=40)
plt.title('K Mean Classification')







x_data2_drill = data2_drill.loc[:,['voltage_avg', 'current_avg', 'power_factor_avg', 'frequency_avg','power_avg']]
 
y_data2_drill = data2_drill.loc[:,['Targets']]

colormap = np.array(['red', 'lime', 'black'])
 
model_data2_drill = KMeans(n_clusters=3)
model_data2_drill.fit(x_data2_drill)

model_data2_drill.labels_

plt.figure(figsize=(10,5))

colormap = np.array(['red', 'lime', 'black'])

plt.subplot(1, 2, 1)
plt.scatter(x_data2_drill.current_avg, x_data2_drill.voltage_avg, c=colormap[y_data2_drill.Targets], s=40)
plt.title('Real Classification')

plt.subplot(1, 2, 2)
plt.scatter(x_data2_drill.current_avg, x_data2_drill.voltage_avg, c=colormap[model_data2_drill.labels_], s=40)
plt.title('K Mean Classification')

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:39:47 2019

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

x = data1.loc[:,['voltage_avg', 'current_avg', 'power_factor_avg', 'frequency_avg','power_avg']]

y = data1.loc[:,['Targets']]

colormap = np.array(['red', 'lime', 'black'])
 
plt.figure(figsize=(10,5))
plt.scatter(data1.Targets, data1.current_avg, c=colormap[y.Targets], s=40)

plt.figure(figsize=(10,5))
plt.scatter(x.current_avg, x.voltage_avg, c=colormap[y.Targets], s=40)
plt.xlabel('Current')
plt.ylabel('Frequency')

model = KMeans(n_clusters=2)
model.fit(x)

model.labels_

plt.figure(figsize=(10,5))

colormap = np.array(['red', 'lime'])

plt.subplot(1, 2, 1)
plt.scatter(x.current_avg, x.voltage_avg, c=colormap[y.Targets], s=40)
plt.title('Real Classification')

plt.subplot(1, 2, 2)
plt.scatter(x.current_avg, x.voltage_avg, c=colormap[model.labels_], s=40)
plt.title('K Mean Classification')
'''
# The fix, we convert all the 1s to 0s and 0s to 1s.
predY = np.choose(model.labels_, [1,0]).astype(np.int64)
print (model.labels_)
print (predY)

colormap = np.array(['red', 'lime'])

plt.figure(figsize=(10,5))
plt.scatter(x.current_avg, x.voltage_avg, c=colormap[y.Targets], s=40)
plt.title('Real Classification')
plt.xlabel('Current')
plt.ylabel('Voltage') 
plt.show()

plt.figure(figsize=(10,5))
plt.scatter(x.current_avg, x.voltage_avg, c=colormap[predY], s=40)
plt.title('K Mean Classification')
plt.xlabel('Current')
plt.ylabel('Voltage')
plt.show()

print(sm.accuracy_score(y, predY))

print(sm.confusion_matrix(y, predY))


data1_drill = data1[data1['State']=='Drill']
'''
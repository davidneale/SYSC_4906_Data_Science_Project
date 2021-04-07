#%%
import csv
from pathlib import Path
import numpy as np
import xlrd
import datetime
from datetime import datetime
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import os
import seaborn as sns
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
#%%


#read data
df_R_raw=pd.read_csv('Dataset_R.csv').set_index('Date')
df_CC_raw = pd.read_csv('Dataset_CC.csv').set_index('Date')
df_ER = pd.read_csv('Dataset_ER.csv').set_index('Date')
df_UR = pd.read_csv('Dataset_UR.csv').set_index('Date')
df_HI = pd.read_csv('Dataset_HI.csv').set_index('Date')

# %%09/03/2020
df_R_raw.index = pd.to_datetime(df_R_raw.index,format = '%d/%m/%Y')
df_CC_raw.index = pd.to_datetime(df_CC_raw.index,format = '%d/%m/%Y')
df_ER.index = pd.to_datetime(df_ER.index)
df_UR.index = pd.to_datetime(df_UR.index)
df_HI.index = pd.to_datetime(df_HI.index)
#resampling time step for R and CC (from daily to monthly)
df_R = df_R_raw.resample('MS').mean()
df_CC = df_CC_raw.resample('MS').mean()

# %%
#change the unit of percentage for ER and UR
df_ER['ER']=df_ER['ER']/100.0
df_UR['UR']=df_UR['UR']/100.0

# %%
# resampling to one dataframe and standard;ization
df_raw=df_R.copy()
df=df_raw.copy()
df_raw['CC']=df_CC['CC']
df_raw['ER']=df_ER['ER']
df_raw['UR']=df_UR['UR']
df_raw['HI']=df_HI['HI']
print('raw data')
print(df_raw)
scaler = StandardScaler()
df=pd.DataFrame(scaler.fit_transform(df_raw))
df.columns=df_raw.columns.copy()
df.index=df_raw.index.copy()
print('raw data after standardlization')
print(df)
df.to_csv('Dataset after standardlization.csv')
# %%
#Descriptive Statistics
print('descriptive Statistics')
print(df.describe().T)
df.describe().T.to_csv('descriptive statistics.csv')
df_raw.describe().T.to_csv(' descriptive statistics before.csv')
# %%
#plot raw data
print('time series plots')
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 10))
df['R'].plot(ax=axes[0,0]); axes[0,0].set_title('R')
df['CC'].plot(ax=axes[0,1]); axes[0,1].set_title('Confirmed Cases')
df['ER'].plot(ax=axes[1,0]); axes[1,0].set_title('Employment Rate')
df['UR'].plot(ax=axes[1,1]); axes[1,1].set_title('Unemployment Rate')
df['HI'].plot(ax=axes[2,0]); axes[2,0].set_title('Happiness Index')
plt.savefig('time series plot.png')

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 10))
df_raw['R'].plot(ax=axes[0,0]); axes[0,0].set_title('R')
df_raw['CC'].plot(ax=axes[0,1]); axes[0,1].set_title('Confirmed Cases')
df_raw['ER'].plot(ax=axes[1,0]); axes[1,0].set_title('Employment Rate')
df_raw['UR'].plot(ax=axes[1,1]); axes[1,1].set_title('Unemployment Rate')
df_raw['HI'].plot(ax=axes[2,0]); axes[2,0].set_title('Happiness Index')
plt.savefig('time series plot before.png')

#%%check the quality of the dataset
print('quality of the dataset')
print(df.isna().any())
df.isna().any().to_csv('quality of the dataset.csv')
#%% check the correlation
print('check the correlation')
corr = df.corr()
print(corr)
sns.heatmap(corr, annot=True)
plt.savefig('correlation heatmap.png')
sns.pairplot(df)
plt.savefig('correlation pairplot.png')

# %%
#create linear regression objective
# Create linear regression object
regr = linear_model.LinearRegression()
y = df['HI']
x = df[['R','CC','ER','UR']]
# Train the model using the training sets
regr.fit(x,y)
print('coefficients for R, CC, ER, UR are', regr.coef_)
print('intercept is    ', regr.intercept_)
print('linear regression expression is ')
print('HI = (', regr.coef_[0], ')*R+ (',regr.coef_[1],')*CC +(', regr.coef_[2], ')*ER +(', regr.coef_[3], ')*UR +', regr.intercept_)
# %%
#visualisation
plt.figure(figsize=(10,8))
x1=df.index
plt.scatter(x1,y,color = 'red')
plt.plot(x1,regr.predict(x),color = 'blue')
plt.xlabel('X')
plt.ylabel('Y',rotation = 0)
plt.title("Linear Regression")
plt.savefig('Linear regression.png')
print('evaluating model performance')
print(r2_score(y, regr.predict(x)))
# %%

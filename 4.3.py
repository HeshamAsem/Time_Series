# Import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


df = pd.read_csv('multiTimeline.csv', skiprows=1)
df.head()
df.info()



df.columns = ['month', 'diet', 'gym', 'finance']
df.head()

df.month = pd.to_datetime(df.month)
df.set_index('month', inplace=True)
df.head()



df.plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);

 
df[['diet']].plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);

 

 
diet = df[['diet']]
diet.rolling(12).mean().plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);

 
gym = df[['gym']]
gym.rolling(12).mean().plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);


 
df_rm = pd.concat([diet.rolling(12).mean(), gym.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);

 
diet.diff().plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);


df.plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);



df.corr()


df.diff().plot(figsize=(7,4), linewidth=1, fontsize=10)
plt.xlabel('Year', fontsize=10);


df.diff().corr()

pd.plotting.autocorrelation_plot(diet);





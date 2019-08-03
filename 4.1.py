import pandas as pd
pd.to_datetime('2018-01-15 3:45pm')
pd.to_datetime('7/8/1952')
pd.to_datetime('7/8/1952', dayfirst=True)
pd.to_datetime(['2018-01-05', '7/8/1952', 'Oct 10, 1995'])
pd.to_datetime(['2/25/10', '8/6/17', '12/15/12'], format='%m/%d/%y')


opsd_daily = pd.read_csv('opsd_germany_daily.csv')
opsd_daily.shape


opsd_daily.head(3)
opsd_daily.tail(3)
opsd_daily.dtypes

opsd_daily = opsd_daily.set_index('Date')
opsd_daily.head(3)

opsd_daily.index


opsd_daily = pd.read_csv('opsd_germany_daily.csv', index_col=0,
                         parse_dates=True)

# Add columns with year, month, and weekday name
opsd_daily['Year'] = opsd_daily.index.year
opsd_daily['Month'] = opsd_daily.index.month
opsd_daily['Weekday Name'] = opsd_daily.index.weekday_name
# Display a random sampling of 5 rows
opsd_daily.sample(5, random_state=0)



opsd_daily.loc['2017-08-10']
opsd_daily.loc['2014-01-20':'2014-01-22']
opsd_daily.loc['2012-02']

#=======================================================

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(rc={'figure.figsize':(7, 4)})

opsd_daily['Consumption'].plot(linewidth=0.2);
opsd_daily['Solar'].plot(linewidth=0.2);
opsd_daily['Wind'].plot(linewidth=0.2);


cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_daily[cols_plot].plot(marker='.', alpha=0.2, linestyle='None', 
                 figsize=(7,4), subplots=True)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')


ax = opsd_daily.loc['2017', 'Consumption'].plot()
ax.set_ylabel('Daily Consumption (GWh)');

ax = opsd_daily.loc['2017-01':'2017-02', 'Consumption'].plot(marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)');

#============================================================

fig, ax = plt.subplots()
ax.plot(opsd_daily.loc['2017-01':'2017-02', 'Consumption'], marker='o', linestyle='-')
ax.set_ylabel('Daily Consumption (GWh)')
ax.set_title('Jan-Feb 2017 Electricity Consumption')
 
#============================================================
 
fig, axes = plt.subplots(3, 1, figsize=(7, 6), sharex=True)
for name, ax in zip(['Consumption', 'Solar', 'Wind'], axes):
    sns.boxplot(data=opsd_daily, x='Month', y=name, ax=ax)
    ax.set_ylabel('GWh')
    ax.set_title(name)
    
# Remove the automatic x-axis label from all but the bottom subplot
if ax != axes[-1]:
    ax.set_xlabel('')

#============================================================

sns.boxplot(data=opsd_daily, x='Weekday Name', y='Consumption');
  
 
import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q5 - Store Survey Duration and Revenue.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head())

#print(f"N = {len(df['Trading_Duration'])}")
c = round(np.corrcoef([df['Trading_Duration'],df['AnnualRevenue']])[0,1],3)
a,b = np.polyfit(df['Trading_Duration'], df['AnnualRevenue'], 1)
#print(a,b)
years = np.array(list(range(min(df['Trading_Duration']),max(df['Trading_Duration'])+1)))

#Graph 1: Annual Revenue by Trading Duration (Store Survey)
plt.scatter(df['Trading_Duration'],df['AnnualRevenue'])
plt.plot(years, a * years + b, linestyle = '--',c= 'grey',label=f'line of best fit (c = {c}') # line of best fit
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K'])
plt.xticks(ticks=[0,5,10,15,20,25,30,35])
plt.xlabel('Trading Duration (Years)')
plt.ylabel('Annual Revenue')
plt.title("Annual Revenue by Trading Duration (Year 2004 Store Survey)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()

#Graph 2: 5 Year rolling Average Revenue (Store Survey)

#shops_opened = [sum((df['Trading_Duration']>=year) & (df['Trading_Duration']<year + 5)) for year in years]
#plt.plot(years, shops_opened)

rolling_average = [np.mean(df[(df['Trading_Duration']>=year) & (df['Trading_Duration']<year + 5)]['AnnualRevenue']) for year in years]
#print(rolling_average)
plt.plot(years[:-4], rolling_average[:-4],label='5 Year Average',c='tab:orange')
plt.plot(years[-5:], rolling_average[-5:],label='Less data',linestyle = '-.',c='tab:orange')
plt.plot(years, a * years + b, linestyle = '--',c= 'grey',label=f'line of best fit (c = {c}') # line of best fit
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K'])
plt.xticks(ticks=[0,5,10,15,20,25,30,35])
plt.xlabel('Trading Duration (Years)')
plt.ylabel('Annual Revenue')
plt.title("5 Year rolling Average Revenue (Year 2004 Store Survey)")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()
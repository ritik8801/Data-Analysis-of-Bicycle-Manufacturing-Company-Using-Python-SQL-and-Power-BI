import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q5 - Totalled Orders per stores Last Year.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head())

print(f"N = {len(df['Trading_Duration'])}")
print(np.corrcoef([df['Trading_Duration'],df['AnnualRevenue']]))
c = round(np.corrcoef([df['Trading_Duration'],df['AnnualRevenue']])[0,1],3)
a,b = np.polyfit(df['Trading_Duration'], df['AnnualRevenue'], 1)
#print(a,b)

plt.scatter(df['Trading_Duration'],df['total_revenue'])
plt.plot(df[df['Trading_Duration']%2==0]['Trading_Duration'], a * df[df['Trading_Duration']%2==0]['Trading_Duration'] + b, linestyle = '--',c= 'grey',label=f'line of best fit (c = {c}') # line of best fit
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000,350000,400000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K','$350K','$400K'])
plt.xticks(ticks=[10,15,20,25,30,35,40,45])
plt.xlabel('Trading Duration')
plt.ylabel('Annual Revenue')
plt.title("Revenue Figures Per Store From 2014 Recorded Orders")
plt.legend()
plt.grid(linestyle = '--', linewidth = 0.5)
plt.tight_layout()
plt.show()
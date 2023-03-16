import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q2 - Annual leave and bonuses.sql').read()
# print(query)
df = pd.read_sql_query(query, conn)
# print(df.head())
# print(f"N = {len(df['annual_leave'])}")
pearson_coef,p_value = stats.pearsonr(df['annual_leave'],df['Bonus'])
#print("Pearson correlation coefficient: " + str(pearson_coef))
#print("p-value: " + str(p_value))

c = round(np.corrcoef([df['annual_leave'],df['Bonus']])[0,1],3)
a,b = np.polyfit(df['annual_leave'], df['Bonus'], 1)
# print(a,b)

df["Sales?"]=df["JobTitle"].str.startswith("Sales")

plt.scatter(df[df["Sales?"]]['annual_leave'],df[df["Sales?"]]['Bonus'],color = "tab:blue",label = "Sales Reps.")
plt.scatter(df[~df["Sales?"]]['annual_leave'],df[~df["Sales?"]]['Bonus'],color = "tab:green",label = "Sales Managers")
plt.plot(df['annual_leave'], a * df['annual_leave'] + b,linestyle = '--',c= 'grey',label=f'line of best fit (c = {c})')
plt.yticks( ticks = [0,1000,2000,3000,4000,5000,6000,7000], 
            labels = ['0','$1000','$2000','$3000','$4000','$5000','$6000','$7000'])
plt.xlabel('Annual Leave (hours)')
plt.ylabel('Bonus')
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Bonus by Annual Leave")
plt.tight_layout()
plt.show()
plt.clf()

df= df[df["Sales?"]]
# Graph 2: Only Sales Representatives
c = round(np.corrcoef([df['annual_leave'],df['Bonus']])[0,1],3)
a,b = np.polyfit(df['annual_leave'], df['Bonus'], 1)

plt.scatter(df['annual_leave'],df['Bonus'],color = "tab:blue",label = "Sales Reps.")
plt.plot(df['annual_leave'], a * df['annual_leave'] + b,linestyle = '--',c= 'grey',label=f'line of best fit (c = {c})')
plt.yticks( ticks = [0,1000,2000,3000,4000,5000,6000,7000], 
            labels = ['0','$1000','$2000','$3000','$4000','$5000','$6000','$7000'])
plt.xlabel('Annual Leave (hours)')
plt.ylabel('Bonus')
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.title("Bonus by Annual Leave - Sales Representatives")
plt.tight_layout()
plt.show()
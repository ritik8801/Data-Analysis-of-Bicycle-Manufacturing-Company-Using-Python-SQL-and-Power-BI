import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q6 - Store Size Num Employees and Revenue.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head())
#print(f"N = {len(df['SquareFeet'])}")
#print(np.corrcoef([df['SquareFeet'],df['NumberEmployees'],df['AnnualRevenue']]))

categories = list(set(df['AnnualRevenue']))
categories.sort()

# Graph 1: Annual Revenue by Store Size
for x in categories:
    df_1 = df[df['AnnualRevenue']==x]
    plt.scatter(df_1['SquareFeet'],df_1['AnnualRevenue'])

a,b = np.polyfit(df['SquareFeet'], df['AnnualRevenue'], 1)
c = round(np.corrcoef([df['SquareFeet'],df['AnnualRevenue']])[0,1],3)
# print(a,b)
plt.plot(df['SquareFeet'], a * df['SquareFeet'] + b, c = 'grey',label=f'line of best fit (c = {c}', linestyle = '--')        # Line of Best Fit

plt.xticks( ticks = [0,10000,20000,30000,40000,50000,60000,70000,80000], 
            labels = ['0','10 000 ft$^{2}$','20 000 ft$^{2}$','30 000 ft$^{2}$','40 000 ft$^{2}$','50 000 ft$^{2}$','60 000 ft$^{2}$','70 000 ft$^{2}$','80 000 ft$^{2}$'],
            rotation = 20)
plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K'])
plt.xlabel('Store Size')
plt.ylabel('Annual Revenue')
plt.title("Annual Revenue by Store Size")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()

# Graph 2: Annual Revenue by Number of Employees
for x in categories:
    df_1 = df[df['AnnualRevenue']==x]
    plt.scatter(df_1['NumberEmployees'],df_1['AnnualRevenue'])

c = round(np.corrcoef([df['NumberEmployees'],df['AnnualRevenue']])[0,1],3)
a,b = np.polyfit(df['NumberEmployees'], df['AnnualRevenue'], 1)
# print(a,b)
plt.plot(df['NumberEmployees'], a * df['NumberEmployees'] + b,c = 'grey',label=f'line of best fit (c = {c}',linestyle = '--')        # Line of Best Fit

plt.yticks( ticks = [0,50000,100000,150000,200000,250000,300000], 
            labels = ['$0K','$50K','$100K','$150K','$200K','$250K','$300K'])
plt.xlabel('Number of Employees')
plt.ylabel('Annual Revenue')
plt.title("Annual Revenue by Number of Employees")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()
plt.clf()

# Graph 3: Number of Employees by Store Size
for x in categories:
    df_1 = df[df['AnnualRevenue']==x]
    plt.scatter(df_1['SquareFeet'],df_1['NumberEmployees'],label = f'${round(x/1000)}'+ 'K')
# a,b = np.polyfit(df['SquareFeet'], df['NumberEmployees'], 1)
# print(a,b)
#plt.plot(df['SquareFeet'], a * df['SquareFeet'] + b, c = 'red')        # Line of Best Fit
plt.xticks( ticks = [0,10000,20000,30000,40000,50000,60000,70000,80000], 
            labels = ['0','10 000 ft$^{2}$','20 000 ft$^{2}$','30 000 ft$^{2}$','40 000 ft$^{2}$','50 000 ft$^{2}$','60 000 ft$^{2}$','70 000 ft$^{2}$','80 000 ft$^{2}$'],
            rotation = 20)
plt.xlabel('Store Size')
plt.ylabel('Number of Employees')
plt.title("Number of Employees by Store Size")
plt.grid(linestyle = '--', linewidth = 0.5)
plt.legend(title = 'Colours = Yearly Revenue')
plt.text(x = 5000.5,y = 12,s = '$30K', c = 'tab:blue')
plt.text(x = 15000.5,y = 3,s = '$80K', c = 'tab:orange')
plt.text(x = 22000.5,y = 32,s = '$100K', c = 'tab:green')
plt.text(x = 33000.5,y = 24,s = '$150K', c = 'tab:red')
plt.text(x = 64000,y = 90,s = '$300K', c = 'tab:purple')
plt.tight_layout()
plt.show()
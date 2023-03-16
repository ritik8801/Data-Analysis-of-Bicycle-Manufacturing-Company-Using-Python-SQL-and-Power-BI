import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q4 - Sick Leave by Job Group.sql').read()
#print(query)
df = pd.read_sql_query(query, conn)
#print(df.head(60))
plt.axvline(x=45,linestyle = '--',c= 'grey')
for x in list(set(df['OrganizationLevel']))[::-1]:
    df_1 = df[df['OrganizationLevel']==x]
    plt.barh(df_1['Job_Group'],df_1['Sick_Leave'],label = x,xerr=df_1['Deviation'])

plt.plot(0,0,label = 'error bars',c = 'black')
plt.xlabel('Annual Sick Leave (Hours)')
plt.ylabel('Job Group')
plt.title("Average Sick Leave by Job Group")
plt.xticks(ticks = [0,10,20,30,40,50,60,70])
plt.grid(axis = 'x',linestyle = '--', linewidth = 0.5)
plt.legend(bbox_to_anchor=(1.01, 0.4), loc='upper left', title = 'Organisation Lvl')
plt.tight_layout()
plt.show()
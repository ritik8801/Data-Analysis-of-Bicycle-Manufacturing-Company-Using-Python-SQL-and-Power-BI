import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q4 - Sick leave by job title.sql').read()
#print(query)

df = pd.read_sql_query(query, conn)
df = df[df['Num_Employees']>5]
#print(df.head())
technicians = []
for x in df['Title']:
    if x.startswith("Technician"):
        technicians.append(True)
    else:
        technicians.append(False)

df["Technician"] = df['Title'].str.startswith(" Technician")
#print(df['Technician'])

plt.bar(df[df["Technician"]]['Title'],df[df["Technician"]]['Average_SickLeave'],color="tab:blue",label = "Technicians")
plt.bar(df[~df["Technician"]]['Title'],df[~df["Technician"]]['Average_SickLeave'],color="tab:green",label = "Other")
plt.axhline(y=45,linestyle = '--',c= 'grey',label='Average  Sickleave (45)')
plt.xlabel('Job Title')
plt.ylabel('Average Sick Leave (hours)')
plt.title("Average Sick Leave by Job Title (Above 5 Employees)")
plt.scatter([], [], color='red', marker='$0$', label='Num. Employees')
for i in range(len(df['Title'])):
    height = df['Average_SickLeave'][i]/2
    plt.text(df['Title'][i], height, df['Num_Employees'][i], ha="center", va="bottom",c = "red")
plt.legend(bbox_to_anchor=(0.4, 1.02))
plt.grid(axis = 'y',linestyle = '--', linewidth = 0.5)
plt.xticks(rotation = 45,ticks = list(df["Title"]),labels= [title.replace(" Technician","") for title in df['Title']])
plt.tight_layout()
plt.show()
import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q1,3 Sales By Country Name.sql').read()
print(query)
df = pd.read_sql_query(query, conn)
print(df)

# Clustered bar chart for Sales by Country
X_axis = np.arange(len(df['CountryName']))
plt.bar(X_axis - 0.2, df['Sales_YTD'], 0.4, 
        label = 'Year To Date', color='mediumseagreen')
plt.bar(X_axis + 0.2, df['Sales_LastYear'], 0.4, 
        label = 'Last Year', color='steelblue')
plt.yticks(ticks = [0,5000000,10000000,15000000,20000000,25000000,30000000],
           labels= ["$0M","$5M","$10M","$15M","$20M","$25M","$30M"])
plt.xticks(X_axis, df['CountryName'], rotation=15)
plt.xlabel("Country")
plt.ylabel("Sales")
plt.title("Sales by Country")
plt.grid(axis = "y",linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()

# Pie chart of year to date sales
plt.subplot(1, 2, 1)
plt.pie(df['Sales_YTD'], autopct='%1.1f%%', pctdistance=1.3)
plt.title("Year to Date", y=1.2)
plt.text(-0.75,-1.8,f"Total = ${round(df['Sales_YTD'].sum()/1000000,1)}M",fontsize = "large",style= 'oblique')

# Pie chart of last year sales
plt.subplot(1, 2, 2)
plt.pie(df['Sales_LastYear'], autopct='%1.1f%%', pctdistance=1.3)
plt.title("Last Year", y=1.2)
plt.text(-0.75,-1.8,f"Total = ${round(df['Sales_LastYear'].sum()/1000000,1)}M",fontsize = "large",style= 'oblique')

# Show both pie charts on same figure
plt.legend(df['CountryName'], bbox_to_anchor=(0,1))
plt.suptitle('Sales by Country')
plt.tight_layout()
plt.show()
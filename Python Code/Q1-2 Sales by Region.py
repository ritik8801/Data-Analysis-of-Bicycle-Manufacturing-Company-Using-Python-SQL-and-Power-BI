import pyodbc 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=WINDOWS-MK7DD8I\SERVER1;'
                      'Database=AdventureWorks2019;'
                      'Trusted_Connection=yes;')

query = open('SQL Queries/Q1 Sales by Region.sql').read()
print(query)
df = pd.read_sql_query(query, conn)
print(df.head())

# Stacked bar chart for Sales by US Region
X_axis = np.arange(len(df['RegionName']))
plt.bar(X_axis - 0.2, df['Sales_YTD'], 0.4, 
        label = 'Year To Date', color='mediumseagreen')
plt.bar(X_axis + 0.2, df['Sales_LastYear'], 0.4, 
        label = 'Last Year', color='steelblue')
plt.xticks(X_axis, df['RegionName'])
plt.yticks(ticks = [0,2000000,4000000,6000000,8000000,10000000,12000000],
          labels = ["$0M","$2M","$4M","$6M","$8M","$10M","$12M"])
plt.xlabel("RegionName")
plt.ylabel("Sales")
plt.title("Sales by Region in USA")
plt.grid(axis = "y",linestyle = '--', linewidth = 0.5)
plt.legend()
plt.tight_layout()
plt.show()

# Pie chart of year to date Sales by US Region
plt.subplot(1, 2, 1)
plt.pie(df['Sales_YTD'], autopct='%1.1f%%', pctdistance=0.7)
plt.title("Year to Date")
plt.text(-0.7,-1.4,f"Total = ${round(df['Sales_YTD'].sum()/1000000,1)}M",fontsize = "large",style= 'oblique')

# Pie chart of last year Sales by US Region
plt.subplot(1, 2, 2)
plt.pie(df['Sales_LastYear'], autopct='%1.1f%%', pctdistance=0.7)
plt.title("Last Year")
plt.text(-0.7,-1.4,f"Total = ${round(df['Sales_LastYear'].sum()/1000000,1)}M",fontsize = "large",style= 'oblique')

# Show both pie charts on same figure
plt.legend(df['RegionName'], bbox_to_anchor=(0,1))
plt.suptitle('Sales by Region in USA')
plt.tight_layout()
plt.show()
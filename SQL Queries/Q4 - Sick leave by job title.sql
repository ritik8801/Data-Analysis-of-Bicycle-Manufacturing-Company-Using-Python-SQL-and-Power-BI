SELECT replace(replace(replace(JobTitle,'Production',''),'Representative','Rep.'),' - ',' ') as Title, avg(SickLeaveHours) AS Average_SickLeave, count(*) AS Num_Employees, OrganizationLevel
FROM HumanResources.Employee
GROUP BY jobtitle, OrganizationLevel
ORDER BY count(*) desc
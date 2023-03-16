WITH cte AS (SELECT  cASt(isnull(OrganizationLevel,0) AS INT) AS OrganizationLevel,jobtitle,SickLeaveHours,
CASE	WHEN OrganizationLevel IS NULL OR OrganizationLevel = 0 THEN 'CEO'
        WHEN OrganizationLevel = 1 THEN 'Directors'
		WHEN OrganizationLevel = 2 AND JobTitle LIKE '%Specialist%' THEN 'Specialists'
		WHEN OrganizationLevel = 2 THEN 'Upper Management'
		WHEN OrganizationLevel = 3 AND JobTitle LIKE '%Supervisor%' THEN 'Supervisors'
		WHEN OrganizationLevel = 3 AND JobTitle LIKE '%Sales%' THEN 'Sales Rep.'
		WHEN OrganizationLevel = 3 THEN 'Senior Roles'
		WHEN OrganizationLevel = 4 AND JobTitle LIKE '%Technician%' THEN 'Technicians'
		WHEN OrganizationLevel = 4 THEN 'Entry Roles'		
		ELSE jobtitle END AS Job_Group
FROM HumanResources.Employee)

SELECT avg(SickLeaveHours) AS Sick_Leave,stdev(SickLeaveHours) AS Deviation,Job_Group,OrganizationLevel,count(*) FROM cte
GROUP BY Job_Group,OrganizationLevel
ORDER BY OrganizationLevel DESC

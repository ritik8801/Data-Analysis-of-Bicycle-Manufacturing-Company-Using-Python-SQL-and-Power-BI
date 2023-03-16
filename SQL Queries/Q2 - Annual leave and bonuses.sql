SELECT VacationHours AS annual_leave, Bonus, SalesQuota, ROUND(SalesYTD,2) AS SalesYTD, JobTitle
FROM HumanResources.Employee AS hre
INNER JOIN Sales.SalesPerson AS ssp
ON hre.BusinessEntityID = ssp.BusinessEntityID
ORDER BY annual_leave;
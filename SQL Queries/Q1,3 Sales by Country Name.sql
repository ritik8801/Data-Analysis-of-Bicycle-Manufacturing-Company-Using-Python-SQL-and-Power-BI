/****** Script for Sales by Country  ******/
WITH cte AS 
	(SELECT CountryRegionCode, 
			ROUND(SUM(SalesYTD), 2) AS Sales_YTD, 
			ROUND(SUM(SalesLastYear), 2) AS Sales_LastYear
	FROM Sales.SalesTerritory
	GROUP By CountryRegionCode)

SELECT Name AS CountryName, Sales_YTD, Sales_LastYear
FROM cte
INNER JOIN Person.CountryRegion AS c
ON c.CountryRegionCode = cte.CountryRegionCode
ORDER BY Sales_YTD + Sales_LastYear DESC
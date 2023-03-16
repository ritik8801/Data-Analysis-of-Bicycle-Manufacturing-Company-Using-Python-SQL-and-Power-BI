/****** Script for Sales by US Region  ******/
SELECT Name AS RegionName, 
	   ROUND(SalesYTD, 2) AS Sales_YTD, 
	   ROUND(SalesLastYear, 2) AS Sales_LastYear
FROM Sales.SalesTerritory
WHERE CountryRegionCode = 'US'
ORDER BY Sales_YTD DESC
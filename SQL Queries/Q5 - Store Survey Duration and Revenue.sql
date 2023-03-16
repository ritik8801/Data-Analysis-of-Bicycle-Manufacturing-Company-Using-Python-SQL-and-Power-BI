SELECT YearOpened, 2004 - YearOpened AS Trading_Duration, BusinessType, Specialty, SquareFeet , AnnualRevenue 
FROM Sales.vStoreWithDemographics
ORDER BY SquareFeet DESC
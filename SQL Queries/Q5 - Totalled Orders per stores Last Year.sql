WITH cte AS (SELECT	storeID, 
			sum(SubTotal) AS total_revenue 
			FROM sales.SalesOrderHeader AS o
			INNER JOIN sales.Customer AS c
			ON o.customerID = c.customerID
			WHERE OrderDate BETWEEN '2013-07-01' AND '2014-06-30'
			GROUP BY storeID)

SELECT storeID, 
		total_revenue,
		2014 - s.[Demographics].value('declare default element namespace "http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey"; 
        (/StoreSurvey/YearOpened)[1]', 'integer') AS Trading_Duration,
		s.[Demographics].value('declare default element namespace "http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey"; 
        (/StoreSurvey/AnnualSales)[1]', 'money') AS [AnnualSales],
		s.[Demographics].value('declare default element namespace "http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey"; 
        (/StoreSurvey/AnnualRevenue)[1]', 'money') AS [AnnualRevenue],
		s.[Demographics].value('declare default element namespace "http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey"; 
        (/StoreSurvey/NumberEmployees)[1]', 'integer') AS [NumberEmployees] ,
		s.[Demographics].value('declare default element namespace "http://schemas.microsoft.com/sqlserver/2004/07/adventure-works/StoreSurvey"; 
        (/StoreSurvey/SquareFeet)[1]', 'integer') AS [SquareFeet] 
		FROM cte
		INNER JOIN sales.store AS s
		ON s.BusinessEntityID=cte.storeID
		ORDER BY total_revenue DESC
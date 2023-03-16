with cte as (select TerritoryID, sum(TotalDue) as total_sales from sales.SalesOrderHeader
where OrderDate between '2013-07-01' and '2014-06-30'
group by TerritoryID)

select cte.TerritoryID,Name, total_sales,SalesYTD,SalesLastYear from cte
inner join sales.SalesTerritory as t
on t.TerritoryID = cte.TerritoryID
order by total_sales desc
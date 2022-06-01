SELECT sales.customers."Customer Names", SUM("Unit Price" * "Order Quantity") as "USD Spent"
FROM sales.sales_order
INNER JOIN sales.customers ON sales.sales_order."_CustomerID" = sales.customers."_CustomerID"
GROUP BY "Customer Names"
ORDER BY "USD Spent" DESC;

SELECT sales.store_locations."State", SUM("Order Quantity") as "Units Sold"
FROM sales.sales_order
INNER JOIN sales.store_locations ON sales.sales_order."_StoreID" = sales.store_locations."_StoreID"
Group By "State"
ORDER BY "Units Sold" DESC;

SELECT sales.store_locations."City Name", SUM("Order Quantity") as "Units Sold", sales.store_locations."State"
FROM sales.sales_order
INNER JOIN sales.store_locations ON sales.sales_order."_StoreID" = sales.store_locations."_StoreID"
WHERE "State" = 'Indiana'-- AND "Type" = 'City'
Group By "City Name", "State"
ORDER BY "Units Sold" DESC;

SELECT sales.store_locations."City Name", SUM("Unit Price" * "Order Quantity") as "USD Spent", SUM("Unit Price" * "Order Quantity"/sales.store_locations."Population") as "USD Per Capita"
FROM sales.sales_order
INNER JOIN sales.store_locations ON sales.sales_order."_StoreID" = sales.store_locations."_StoreID"
GROUP BY "City Name"
ORDER BY "USD Per Capita" DESC;

SELECT sales.products."Product Name", SUM("Order Quantity") as "Units Sold"
FROM sales.sales_order
INNER JOIN sales.products ON sales.sales_order."_ProductID" = sales.products."_ProductID"
GROUP BY "Product Name"
ORDER BY "Units Sold" DESC;

SELECT sales.products."Product Name", sales.store_locations."City Name", sales.store_locations."Water Area", SUM("Order Quantity") as "Units Sold"
FROM sales.sales_order
INNER JOIN sales.store_locations ON sales.sales_order."_StoreID" = sales.store_locations."_StoreID"
INNER JOIN sales.products ON sales.products."_ProductID" = sales.sales_order."_ProductID"
GROUP BY "City Name", "Water Area", "Product Name"
ORDER BY "Water Area" DESC, "Units Sold" DESC;

SELECT sales.sales_team."Region", AVG(date_part('day',"DeliveryDate" - "OrderDate")) as "Average Delivery Time (days)"
FROM sales.sales_order
INNER JOIN sales.sales_team ON sales.sales_team."_SalesTeamID" = sales.sales_order."_SalesTeamID"
--WHERE "Region" = 'Northeast'
GROUP BY "Region";

SELECT sales.sales_team."Sales Team", SUM("Unit Price" - "Unit Cost") as "Total Profit"
FROM sales.sales_order
INNER JOIN sales.sales_team ON sales.sales_team."_SalesTeamID" = sales.sales_order."_SalesTeamID"
GROUP BY "Sales Team"
ORDER BY "Total Profit" DESC;

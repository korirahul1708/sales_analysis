SELECT category,
SUM(quantity) AS total_sales
FROM sales_dataset_5000_rows
GROUP BY category;
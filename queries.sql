SELECT region, ROUND(SUM(sales),2) AS total_sales, ROUND(SUM(profit),2) AS total_profit
FROM orders GROUP BY region ORDER BY total_profit DESC;

SELECT customer_name, ROUND(SUM(sales),2) AS total_spent
FROM orders GROUP BY customer_name ORDER BY total_spent DESC LIMIT 10;

SELECT sub_category, ROUND(SUM(profit),2) AS total_profit
FROM orders GROUP BY sub_category HAVING total_profit < 0;

SELECT month, ROUND(SUM(sales),2) AS sales,
  ROUND(SUM(sales) - LAG(SUM(sales)) OVER (ORDER BY month), 2) AS change_vs_prev
FROM orders GROUP BY month;

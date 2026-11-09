# Retail Sales Analysis (Python + SQL)

## Problem Statement
A retail business wants to understand where it makes and loses money. This project analyses order data to find sales trends, the most and least profitable product categories and regions, top customers, and the effect of discounts on profit.

## Dataset
Sample Superstore dataset (Kaggle). Download the CSV and save it as `data/superstore.csv`.

## Tools Used
- Python (pandas, matplotlib)
- SQL (SQLite, run through Python)

## What the Project Does
1. Cleans the data (column names, date parsing, duplicates)
2. Calculates key metrics: total sales, total profit, profit margin
3. Plots the monthly sales trend and profit by sub-category
4. Analyses average profit at different discount levels
5. Runs SQL queries for regional performance, top customers, loss-making sub-categories, and month-over-month change

## Key Findings
_Fill these in after running the project, using your own results._
- Region with the highest profit: ...
- Sub-categories that lose money: ...
- Effect of high discounts on profit: ...
- Sales trend observation: ...

## Charts
Add `monthly_sales.png` and `profit_by_subcategory.png` here after running.

## How to Run
```bash
pip install -r requirements.txt
python analysis.py
```

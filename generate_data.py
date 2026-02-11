import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from pandas import date_range

#---1. first parameters
np.random.seed(42)
start_date = datetime(2023,1,1)
end_date = datetime(2024,12,31)
date_range = pd.date_range(start=start_date,end=end_date,freq='D')
# print(len(date_range))
#---2. DimDate
# print("DimDate is making")
dim_date = pd.DataFrame({'DateKey': date_range.strftime('%Y%m%d').astype(int),
                          'Date': date_range,
                           'Year': date_range.year,
                           'Quarter': date_range.quarter,
                           'Month': date_range.month,
                           'MonthName': date_range.strftime('%B'),
                           'DayOfWeek': date_range.dayofweek + 1, # 1 = Monday
                           'DayName': date_range.strftime('%A'),
                           'IsWeekend': (date_range.dayofweek >= 5).astype(int)})
dim_date.to_csv('01_Data/dim_date.csv', index=False)
# print('DimDate is made!')
#---3. DimProduct
# print('\n DimProduct is making.')
categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports']
subcategories = {
 'Electronics': ['Smartphone','Laptop','Headphone'],
 'Clothing': ['Men','Women','Kids'],
 'Home & Kitchen': ['Furniture','Cookware','Decor'],
 'Books': ['Fiction','Non-Fiction','Educational'],
 'Sports': ['Outdoor','Fitness','Team Sports']
}
products = []
product_id = 1000
for cat in categories:
 for sub in subcategories[cat]:
  for i in range(1,4):
   products.append({
    'ProductKey': product_id,
    'ProductName': f'{sub} Product {i}',
    'Category': cat,
    'SubCategory': sub,
    'UnitCost': round(np.random.uniform(10,500),2),
    'UnitPrice': round(np.random.uniform(15,600),2)
   })
   product_id += 1
dim_product = pd.DataFrame(products)
dim_product['ProfitMargin'] = ((dim_product['UnitPrice'] - dim_product['UnitCost']) /
                               dim_product['UnitPrice']).round(3)
dim_product.to_csv('01_Data/dim_product.csv',index=False)
# print('DimProduct is made!')
#---4. DimCustomer
# print('\n DimCustomer is making.')
regions = ['North','South','East','West']
customer_segments = ['Premium','Standard','Basic']
customers = []
for i in range(1,101):
 customers.append({
  'CustomerKey': 5000 + i,
  'CustomerName': f'Customer {i}',
  'Region': np.random.choice(regions),
  'SignupDate': np.random.choice(date_range[0:365]),
  'CustomerSegment': np.random.choice(customer_segments,p=[0.2,0.6,0.2])
 })
dim_customer = pd.DataFrame(customers)
dim_customer.to_csv('01_Data/dim_customer.csv',index=False)
# print('DimCustomer is made!')
#---5. FactSales
# print('FactSales is making...')
num_transactions = 5000
sales_data = []
for _ in range(num_transactions):
 date = np.random.choice(date_range)
 product = dim_product.sample(1).iloc[0]
 customer = dim_customer.sample(1).iloc[0]
 # Create Sales Cost
 quantity = np.random.randint(1,5)
 unit_price = product['UnitPrice']
 unit_cost = product['UnitCost']
 discount_pct = np.random.choice([0,0.5,0.1,0.15],p=[0.6,0.2,0.15,0.05])
 sales_amount = quantity * unit_price * (1 - discount_pct)
 total_cost = quantity * unit_cost
 profit = sales_amount - total_cost
 sales_data.append({
  'DateKey': int(pd.to_datetime(date).strftime('%Y%m%d')),
  'ProductKey': product['ProductKey'],
  'CustomerKey': customer['CustomerKey'],
  'SalesOrderNumber': f'SO{np.random.randint(10000,99999)}',
  'Quantity': quantity,
  'UnitPrice': unit_price,
  'UnitCost': unit_cost,
  'DiscountPct': discount_pct,
  'SalesAmount': round(sales_amount,2),
  'TotalCost': round(total_cost,2),
  'Profit':round(profit,2)
 })
fact_sales = pd.DataFrame(sales_data)
fact_sales.to_csv('01_Data/fact_sales.csv',index=False)
# print('FactSales is made!')

#---6. Budget
# print('\n Budget is making...')
budget_data = []
for year in [2023, 2024]:
 for month in range(1,13):
  budget_data.append({
   'Year': year,
   'Month': month,
   'Budget_Sales': np.random.uniform(80000,120000)
  })
budget = pd.DataFrame(budget_data)
budget.to_csv('01_Data/budget.csv')
# print('Budget is made!')
# print(f"   - DimDate: {dim_date.shape[0]} rows")
# print(f"   - DimProduct: {dim_product.shape[0]} rows")
# print(f"   - DimCustomer: {dim_customer.shape[0]} rows")
# print(f"   - FactSales: {fact_sales.shape[0]} rows")
# print(f"   - Budget: {budget.shape[0]} rows")

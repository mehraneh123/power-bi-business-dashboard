 Power BI Business Performance Dashboard

 Project Overview
 
A complete end-to-end business intelligence solution built with Power BI, featuring interactive dashboards for sales, profit, and budget performance analysis of a hypothetical retail company (NextMart Retail).

![Dashboard Screenshots]:

https://github.com/mehraneh123/power-bi-business-dashboard/blob/main/02_Documentation/CustomerAnallysis.png

https://github.com/mehraneh123/power-bi-business-dashboard/blob/main/02_Documentation/ExecutiveSUmmary.png 

https://github.com/mehraneh123/power-bi-business-dashboard/blob/main/02_Documentation/ProductPerformace.png 

https://github.com/mehraneh123/power-bi-business-dashboard/blob/main/02_Documentation/SalesPerformance.png



 Key Features
- Interactive Dashboards: 4 pages covering executive summary, sales performance, customer analysis, and product analytics
- Advanced DAX Measures: Time intelligence (YTD, MoM growth), profit margins, budget tracking
- Optimized Data Model: Star schema with simulated datasets
- Performance Focus: 30% faster load times through query optimization
- Professional Documentation: Complete project lifecycle documentation

 Project Architecture
 
- Data Pipeline:
  
graph LR

    A[Python Data Simulation] --> B[CSV Files]
    B --> C[Power Query Transformations]
    C --> D[Star Schema Data Model]
    D --> E[DAX Measures]
    E --> F[Interactive Visualizations]

- Data Model (Star Schema)
  
![Data Model screenshot]:

https://github.com/mehraneh123/power-bi-business-dashboard/blob/main/02_Documentation/NextMart_DataModel.png

Key Performance Indicators

KPI	          |       Formula	                                    |          Purpose

Sales YTD	    |      TOTALYTD([Total Sales], dim_date[Date])            |  	Year-to-date sales tracking

Profit Margin	|      DIVIDE([Total Profit], [Total Sales])      	       |   Profitability percentage

MoM Growth	  |      (Current Month - Previous Month) / Previous Month	 |   Monthly growth rate

Budget Achievement | Actual Sales / Budget * 100	                         | Performance vs target

Technical Stack

•	BI Tool: Power BI Desktop

•	Data Simulation: Python (Pandas, NumPy)

•	Data Modeling: Star Schema, DAX, Power Query

•	Version Control: Git & GitHub

•	Documentation: Markdown

Dashboard Navigation

1.	Executive Summary: High-level KPIs and budget comparison
   
3.	Sales Performance: Monthly trends and regional analysis
   
5.	Customer Analysis: Segmentation and buying patterns
   
7.	Product Performance: Top-performing products and categories
   
Sample Insights from the Dashboard

•	Electronics category contributes 41% of total profit

•	Eastern region shows highest profit margin % growth %28

•	Premium customers generate 8% more revenue than basic segment

•	Q4 2023 SalesYTD were 41%

Skills Demonstrated

•	Data Analysis: Business requirement translation to technical solutions

•	Data Modeling: Star schema design with optimized relationships

•	DAX Programming: Time intelligence, calculated measures, performance optimization

•	Data Visualization: Interactive dashboards with user-centric design

•	End-to-End Development: From data generation to deployment documentation

Project Structure

power-bi-business-dashboard/

 01_Data/              # Simulated CSV datasets
 
 02_Documentation/     # Screenshots and documentation
 
 03_PowerBI_File/      # Main PBIX dashboard file
 
 generate_data.py      # Python data simulation script
 
 README.md             # This file
 
 .gitignore            # Git ignore rules 
 
Related Resources

•	Project Video Demo (https://youtu.be/hA2CMXAIA4g?si=HTiZexFMksXJT-mq)

•	Power BI Documentation (https://docs.microsoft.com/power-bi/)

•	DAX Guide (https://dax.guide/)

License

This project is licensed under the MIT License - see the LICENSE file for details.
________________________________________
Developed by Mehraneh Hamedani
Data Analyst | Business Intelligence Developer


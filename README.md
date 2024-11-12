# Kalbe Sales Insight
Case Study Data Scientist from Kalbe Nutritionals. Sales Prediction and Customer Segmentation Project


## Project Overview
This project was initiated by the Inventory and Marketing teams of Kalbe Nutritionals to tackle two primary objectives:
1. **Sales Prediction:** Forecast daily sales quantities to help the inventory team maintain optimal stock levels.
2. **Customer Segmentation:** Cluster customers based on key attributes to help the marketing team provide personalized promotions and targeted sales treatment.


## Tools Used
- **Python:** For data manipulation, analysis, and modeling.
- **Jupyter Notebook:** For model development.
- **PostgreSQL:** As the database to store and query data.
- **DBeaver:** For querying and database management.
- **Tableau Public:** For creating interactive visual dashboards.


## Datasets
Four main datasets were used in this project:
- [customer.csv](/dataset/customer.csv): Contains information about customers, including their age gender, marital status, and income.
- [product.csv](/dataset/product.csv): Provides details on the products sold, such as product names and prices.
- [store.csv](/dataset/store.csv): Contains data on store locations, store types, and store groups.
- [transaction.csv](/dataset/transaction.csv): Holds transactional records with product sales data, including dates, quantities, total amounts, and store information.


## Steps Taken
1. Data Ingestion

    Imported datasets (customer.csv, product.csv, store.csv, transaction.csv) into PostgreSQL using DBeaver.

2. Exploratory Data Analysis (EDA)
    - **Average customer age by marital status:** SQL query shows average age varies slightly across marital statuses.
    - **Average customer age by gender:** Slight difference in average age between genders.
    - **Top-selling store by quantity:** Identified the store with the highest sales quantity.
    - **Best-selling product by total amount:** Identified the product generating the most revenue.

3. Data Visualization (Tableau)

    Created four worksheets and a dashboard for visualizing:
    - Monthly sales quantity trends.
    - Daily total sales amount.
    - Sales by product.
    - Sales by store.

4. Predictive Modeling (Sales Prediction)

    Built a Time Series Regression Model using Python to predict daily sales quantities.
    - Model trained on transaction data.
    - Helps the inventory team maintain optimal stock levels based on predicted daily demand.

5. Customer Segmentation (Clustering)

    <!-- - Applied K-Means Clustering to segment customers by age and income. -->
    - Applied K-Means Clustering to segment customers.
    - Resulted in 5 distinct customer segments for personalized marketing strategies.


## Results
- **Sales Prediction:** The regression model predicts daily sales quantities, aiding the inventory team in stock management.
- **Customer Segmentation:** Segments based on demographic data help the marketing team create targeted campaigns.


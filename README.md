# Skills-Bootcamp-Assignment---Bike-sales (W.I.P as of 12/11/2025)

This data analysis assignment was completed during a skills bootcamp at Gateshead college. The aim of the assignment was to take raw data from a Bike retailer (from 2022) and analyse it to discover trend in the data that would be beneficial to the retailer. This repository contains scripts that written in python, using the Pandas module.

The data provided was to be uploaded to SQLonline and consisted of 4 databases; Customers, products, sales and employees. Within each table, there would be info relevent regarding the namesake of the table.

The customers table conmtained dates of purchases, number of purchases and customer ID
The products contained product description, product ID and price
The sales table is where the bulk of the data was and included sales date, number of purchases, customer ID, employee ID
Finally, the employee table contained details regarding employees including employee ID.

First the data that was required would be joined (if from multiple tables) and extracted using SQL. For example, the sales value of each transaction does not exist and so to calculate this, the product table and sales table could be combined using product ID as the key and returning info regarding quantity and price so that total value of the transaction could be calculated later. When extracted, the data was saved as a csv file and exported to python using the Pandas module

Once different sets of data were extracted, Pandas was used to manipulate the data (such as the groupby method) so that it could be analysed, in particulr the matplotlib library was used to visualize the processed data.



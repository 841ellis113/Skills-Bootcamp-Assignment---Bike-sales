import pandas
import numpy
import matplotlib.pyplot as plt


#import file containing saledate, price, quantity, then clean it of zero value entries
#create a column for total sale value, then order it by date

data = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\SalesPriceValue.csv")
data['value']= 0
data['value']= data['price']*data['quantity']
data = data.sort_values('salesdate')
data['month']= 0
data['day']= 0

#split the date of each sale into day and month of the year
for i in range(len(data)):
    date = data.loc[i,'salesdate']
    year  = int(date.rsplit(sep='-')[0])
    month = int(date.rsplit(sep='-')[1])
    day   = int(date.rsplit(sep='-')[2])
    data.loc[i,'month']= month
    data.loc[i,'day']  = day

#remove the zero value transactions and look at them
zeros= data[data['value']==0]
data = data[data['value']!=0]
print(zeros)

#getting some basic stats from the data
basic_stats = data.describe()
print(basic_stats)

#Calculating the total amount of revenue for the year, to nearest pound
revenue = data['value'].sum()
print('\n')
print(round(revenue))



import pandas
import numpy
import matplotlib.pyplot as plt

raw = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\producttype.csv")

#then we create a copy, then a value column for total cost of each purchase
#and add a month column
data = raw.copy()
data['value']= 0
data['value']= data['quantity']*data['price']
data['month']= 0
data['day']  = 0

#split the date of each sale into day and month of the year
for i in range(len(data)):
    date = data.loc[i,'salesdate']
    year  = int(date.rsplit(sep='-')[0])
    month = int(date.rsplit(sep='-')[1])
    day   = int(date.rsplit(sep='-')[2])
    data.loc[i,'month']= month
    data.loc[i,'day']  = day

zeros   = data[data['value']==0]
data    = data[data['value']!=0]

#From this can group by product name, sum and order to get item thats sells the most, least
# and the most valuable and least valuable

values      = (data.groupby(['name','price']))[['value','quantity']].sum()
least_val   = (values.sort_values('value')).head(10)
print('\n',least_val)
most_val    = (values.sort_values('value',ascending=False)).head(10)
print('\n',most_val)
units       = (data.groupby(['name','price']))[['quantity','value']].sum()
least_sold  = (units[units['quantity']==1].sort_values('value')).head(10)
print('\n',least_sold)
most_sold   = (units.sort_values('quantity',ascending=False)).head(10)
print('\n',most_sold)


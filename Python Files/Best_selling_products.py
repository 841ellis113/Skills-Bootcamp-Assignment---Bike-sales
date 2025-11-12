import pandas
import numpy
import matplotlib.pyplot as plt

raw = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\producttype.csv")

#then we create a copy, then a value column for total cost of each purchase
#and add a month column
data = raw.copy()
data['value']=0
data['value']=data['quantity']*data['price']
data['month']=0

#then determine month of each purchase
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for i in range(len(data)):
    date = data['salesdate'][i]
    for month in months:
        if date.startswith('2022-'+month):
            data['month'][i]=int(month)
        else:
            continue

#From this can group by product name, sum and order to get item thats sells the most
#note we have not yet scrubber the zero value entries yet.
overall = data.groupby('name').sum('quantity')
overall = overall.sort_values('quantity',ascending =False)

#then isolate the 0 value items.
free = overall[overall['price']==0]
print(free)

#Scrub the data for 0 value entries and re-group, give top 10 most sold items and
#also give items that have sold only less than  in the year
removed = data[data['value']!=0]
clean   = removed.groupby('name')[['quantity','price','value']].sum()
clean_value = clean.sort_values('quantity', ascending=False)
print(clean_value.head(10))
print(clean_value[(clean_value['quantity']==1)])

#also do this for value of sales, give top 10 most sold items and
#also give items that have produced the smallest revenue
removed = data[data['value']!=0]
clean   = removed.groupby('name')[['value','quantity','price']].sum()
clean_value = clean.sort_values('value', ascending=False)
print(clean_value.head(10))
print(clean_value[(clean_value['value']<100)])








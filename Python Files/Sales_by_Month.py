import numpy
import matplotlib.pyplot as plt
import pandas

#first download data including price, quantity and salesdate
data = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\salesdate_value.csv")

#create a new column and then manipulate it to get sales value for each transaction by quantity*price
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

#remove the zero entries
clean = data[data['value']!=0]

#group by month and sum the total sales value and the number of items sold as well as the
#number of days sales were made.
units  = clean.groupby('month')['quantity'].sum()
unitsN = units.to_numpy()

sales  = clean.groupby('month')['value'].sum()
salesN = sales.to_numpy()
print(sales.describe())
days  = clean.groupby('month')['salesdate'].nunique()
daysN = days.to_numpy()

#x axis for graphs
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#graph sales value  and items sold per month
fig, ax1 = plt.subplots()
ax1.bar(months, salesN, color='xkcd:salmon', label='Revenue')
ax1.set_xlabel('Months')
ax1.set_ylabel('Revenue (£)', color='xkcd:salmon')
ax1.tick_params(axis='y', labelcolor='xkcd:salmon')
plt.legend(loc='upper left')
ax2 = ax1.twinx()
ax2.set_ylabel('Units Sold', color='xkcd:cerulean')
ax2.plot(months, units, color='xkcd:cerulean', label = 'Items')
ax2.tick_params(axis='y', labelcolor='xkcd:cerulean')
plt.legend(loc='upper right')
fig.tight_layout()
plt.show()

plt.bar(months,days)
plt.title('Number Of Days With Sales')
plt.ylim(0,25)
plt.show()

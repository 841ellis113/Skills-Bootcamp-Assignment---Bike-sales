import numpy
import matplotlib.pyplot as plt
import pandas

#first download data including price, quantity and salesdate
data = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\salesdate_value.csv")

#create a new column and then manipulate it to get sales value for each transaction by quantity*price
data['value']=0
data['value']=data['quantity']*data['price']
data['month']=0

#Need to fill month colume depending on the salesdate, iterate over sales date and then
#identify which month it is from the string, populate month column with number that indicates
#month so that they can be grouped. Gives a warning, due to slicing magic
#should make a copy of the dataframe to populate but everything works!
months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for i in range(len(data)):
          date = data['salesdate'][i]
          for month in months:
              if date.startswith('2022-'+month):
                  data['month'][i]=int(month)
              else:
                  continue

print(data)

#next filter out 0 value transactions
#will use this multiple times
clean = data[data['value']!=0]

#group by month and sum up totals and quantity to get monthly transactions and sale figures
groupedm = clean.groupby('month')
totalValue  = groupedm.sum()

#create an array of monthly revenue totals
salesfig = totalValue['value'].to_numpy()

#and do the same for the number of items sold per month
trans    = totalValue['quantity'].to_numpy()

#create data for the number of purchases per month
purchases = []
for i in range(1,13):
    purchases.append(groupedm.count()['salesdate'][i])
pdata = numpy.array(purchases)

#x axis for the graphs
xmonth   = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

#graph sales value per month
plt.bar(xmonth,salesfig)
plt.xlabel('months')
plt.ylabel('Value')
plt.title('Sales Value per Month')
plt.show()

#graphs
fig, ax1 = plt.subplots()

color = 'blue'
ax1.set_xlabel('month')
ax1.set_ylabel('Number of Transactions', color=color)
ax1.plot(xmonth, pdata, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  

color = 'red'
ax2.set_ylabel('Items sold', color=color)  # we already handled the x-label with ax1
ax2.plot(xmonth, trans, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.show()


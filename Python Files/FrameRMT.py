import numpy
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\producttype.csv")

#then we create a copy, then a value column for total cost of each purchase
#and add a month column and one for the type of product it is: category, pre-filled
data['value']=0
data['value']=data['quantity']*data['price']
data['month']=0
data['category']='Parts'

#split the date of each sale into month of the year
for i in range(len(data)):
    date  = data.loc[i,'salesdate']
    month = int(date.rsplit(sep='-')[1])
    data.loc[i,'month']= month

#label the product type for each transaction
values1 = {'1000':'Touring','2000':'Touring','3000':'Touring','Frame':'Frame'}
values2 = {'Jersey':'Clothing','Socks':'Clothing','Gloves':'Clothing','Vest':'Clothing',
          'Tights':'Clothing','Shorts':'Clothing','100':'Mountain','200':'Mountain','300':'Mountain','400':'Mountain','500':'Mountain','600':'Mountain',
          '150':'Road','250':'Road','350':'Road','450':'Road','550':'Road','650':'Road','750':'Road'}
for i in range(len(data)):
    description = data.loc[i,'name']
    for key in list(values2.keys()):
        if description.find(key)>0:
            data.loc[i,'category'] = values2[key]
            break
        else:
            continue
    for key in list(values1.keys()):
        if description.find(key)>0:
            data.loc[i,'category'] = values1[key]
            break
        else:
            continue
        
#clean the data
data = data[data['value']!=0]

#produce a overall bar charts that shows the breakdown of sales value, items sold
# by 'Bike', 'Parts' and 'Clothing'
frame     = data[data['category']=='Frame']

#then determine month of each purchase
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#working with frames and so to sort into road, mountain and touring need to re-loop above on
#subset frames rather than whine Dataframe. To do this, reset index of the subset 'frame'
#the loop over each row entry, determine frame type then re-categorize
frame = frame.reset_index()
values3 = {'Road':'Road','Mountain':'Mountain','Touring':'Touring'}
for i in range(len(frame)):
    description = frame.loc[i,'name']
    for key in list(values3.keys()):
        if description.find(key)>0:
            frame.loc[i,'category'] = values3[key]
            break
        else:
            continue

road      = frame[frame['category']=='Road']
mountain  = frame[frame['category']=='Mountain']
touring   = frame[frame['category']=='Touring']

#group all road, mountain and touring frames by month and then sum value to get total revenue
road_revenue = (road.groupby('month')['value'].sum()).sum()
mountain_revenue = (mountain.groupby('month')['value'].sum()).sum()
touring_revenue = (touring.groupby('month')['value'].sum()).sum()

#summing to get total units sold
road_units = (road.groupby('month')['quantity'].sum()).sum()
mountain_units = (mountain.groupby('month')['quantity'].sum()).sum()
touring_units = (touring.groupby('month')['quantity'].sum()).sum()

#data for month revenue and units sold per bike type. Add zero values for months
#with no sales
RMU = list((road.groupby('month')['quantity'].sum()).to_numpy())
RMU.insert(0,0)
RMU.insert(2,0)
RMU.insert(3,0)
RMU.insert(8,0)
RMU = numpy.array(RMU)
RMR = list((road.groupby('month')['value'].sum()).to_numpy())
RMR.insert(0,0)
RMR.insert(2,0)
RMR.insert(3,0)
RMR.insert(8,0)
RMR = numpy.array(RMR)

MMU = list((mountain.groupby('month')['quantity'].sum()).to_numpy())
MMU.insert(1,0)
MMU.insert(2,0)
MMU.insert(6,0)
MMU.insert(11,0)
MMU = numpy.array(MMU)
MMR = list((mountain.groupby('month')['value'].sum()).to_numpy())
MMR.insert(1,0)
MMR.insert(2,0)
MMR.insert(6,0)
MMR.insert(11,0)
MMR = numpy.array(MMR)

TMU = list((touring.groupby('month')['quantity'].sum()).to_numpy())
TMU.insert(1,0)
TMU.insert(4,0)
TMU.insert(9,0)
TMU.insert(11,0)
TMU = numpy.array(TMU)
TMR = list((touring.groupby('month')['value'].sum()).to_numpy())
TMR.insert(1,0)
TMR.insert(4,0)
TMR.insert(9,0)
TMR.insert(11,0)
TMR = numpy.array(TMR)

#plot revenue and units sold for each type of bike
fig,axs        = plt.subplots(1,3)
labels = ['Road','Mountain','Touring']
colours= ['xkcd:crimson','xkcd:red','xkcd:salmon']
axs[0].bar(labels,[road_revenue,mountain_revenue,touring_revenue],label=labels,color=colours)
axs[0].set_ylabel('Sales Value (£)')
axs[0].set_title('Sales Value by Type')
axs[0].legend(title = 'Types', loc='lower left')
axs[1].bar(labels,[road_units,mountain_units,touring_units],label=labels,color=colours)
axs[1].set_ylabel('Units Sold')
axs[1].set_title('Units sold by category')
axs[1].legend(title = 'Amount')
axs[2].pie([road_revenue,mountain_revenue,touring_revenue],labels=labels, colors=colours,autopct='%1.1f%%')
axs[2].set_title('Percentage of Revenue by Type')
plt.show()

#plot revenue and units sold per bike type per month
fig,axs        = plt.subplots(1,2)
axs[0].bar(months, RMR, label='Road',color='xkcd:crimson')
axs[0].bar(months, MMR, bottom = RMR, label='Mountain',color='xkcd:red')
axs[0].bar(months, TMR, bottom = RMR+MMR, label='Touring',color='xkcd:salmon')
axs[0].set_ylabel('Sales Value (£)')
axs[0].set_xlabel('Month')
axs[0].set_title('Sales Value by Type per Month')
axs[0].legend(title = 'Types')
axs[1].bar(months, RMU, label='Road',color='xkcd:crimson')
axs[1].bar(months, MMU, bottom = RMU, label='Mountain',color='xkcd:red')
axs[1].bar(months, TMU, bottom = RMU+MMU, label='Touring',color='xkcd:salmon')
axs[1].set_ylabel('Units Sold')
axs[1].set_xlabel('Months')
axs[1].set_title('Units Sold by Type')
axs[1].legend(title = 'Amount')
plt.show()


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

#split the data in different categories, note the subsplitting that will be used later
road      = data[data['category']=='Road']
mountain  = data[data['category']=='Mountain']
touring   = data[data['category']=='Touring']
frame     = data[data['category']=='Frame']
parts     = data[data['category']=='Parts']
clothing  = data[data['category']=='Clothing']
bikes     = pandas.concat([road,mountain,touring])
tot_parts = pandas.concat([parts, frame])

#then determine month of each purchase
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

#plot bar chart for total value of sales per category, split into bikes, frame parts
vsum           = [bikes.value.sum(),frame.value.sum(),parts.value.sum(),clothing.value.sum()]
isum           = [bikes.quantity.sum(),frame.quantity.sum(),parts.quantity.sum(),clothing.quantity.sum()]
labels         = ['Bikes','Frames','Parts','Clothing']
val_label      = ['Bikes: 58.1%','Frames: 20.8%','Parts: 20.7%','Clothing: 0.4%']
item_label     = ['391','255','769','104']
colours        = ['tab:red','tab:blue','xkcd:sky blue','tab:orange']
fig,axs        = plt.subplots(1,3)
axs[0].bar(labels,vsum,label=val_label,color=colours)
axs[0].set_ylabel('Sales Value (£)')
axs[0].set_title('Sales Value by category')
axs[0].legend(title = 'Percentages', loc='lower left')
axs[1].bar(labels,isum,label=item_label,color=colours)
axs[1].set_ylabel('Units Sold')
axs[1].set_title('Units sold by category')
axs[1].legend(title = 'Amount')
axs[2].pie(vsum,labels=['Bikes','Frames','Parts','Clothing'], colors=colours,autopct='%1.1f%%')
axs[2].set_title('Percentage of Revenue by Type')
plt.show()

#create monthly data for the different types
bike_month   = bikes.groupby(['month'])[['value','quantity']].sum()
bike_month   = numpy.transpose(bike_month.to_numpy())
bmr, bmu     = bike_month[0],bike_month[1]
frame_month  = frame.groupby(['month'])[['value','quantity']].sum()
frame_month  = numpy.transpose(frame_month.to_numpy())
fmr, fmu     = frame_month[0],frame_month[1]
parts_month  = parts.groupby(['month'])[['value','quantity']].sum()
parts_month  = numpy.transpose(parts_month.to_numpy())
pmr, pmu     = parts_month[0],parts_month[1]
cloth_month  = clothing.groupby(['month'])[['value','quantity']].sum()
wip0         = numpy.transpose(cloth_month.to_numpy())[0]
wip1         = numpy.transpose(cloth_month.to_numpy())[1]
cmr          = list(wip0)
cmu          = list(wip1)

#need to insert 0 sales for August and December
cmr.insert(7,0)
cmu.insert(7,0)
cmr.insert(11,0)
cmu.insert(11,0)
cmr = numpy.array(cmr)
cmu = numpy.array(cmu)

fig,axs        = plt.subplots(1,2)
axs[0].bar(months, bmr, label='Bikes',color='tab:red')
axs[0].bar(months, fmr, bottom = bmr, label='Frames',color='tab:blue')
axs[0].bar(months, pmr, bottom = bmr+fmr, label='Parts',color='xkcd:sky blue')
axs[0].bar(months, cmr, bottom = bmr+fmr+pmr, label='Clothing',color='tab:orange')
axs[0].set_ylabel('Sales Value (£)')
axs[0].set_xlabel('Month')
axs[0].set_title('Sales Value by Category per Month')
axs[0].legend(title = 'Types')
axs[1].bar(months, bmu, label='Bikes',color='tab:red')
axs[1].bar(months, fmu, bottom = bmu, label='Frames',color='tab:blue')
axs[1].bar(months, pmu, bottom = bmu+fmu, label='Parts',color='xkcd:sky blue')
axs[1].bar(months, cmu, bottom = bmu+fmu+pmu, label='Clothing',color='tab:orange')
axs[1].set_ylabel('Units Sold')
axs[1].set_xlabel('Months')
axs[1].set_title('Units sold by category')
axs[1].legend(title = 'Amount')
plt.show()

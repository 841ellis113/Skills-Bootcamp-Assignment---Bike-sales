import pandas
import numpy
import matplotlib.pyplot as plt

data = pandas.read_csv(r"C:\Users\44784\Desktop\Skills Bootcamp\SalesDatabase\customers.csv")

#have a quicklook at the data
data.info()

# we see that the only column with NaN is the middleinitial column, we convert this into
#a blank string

filled = data.fillna(' ')

#add columns for the value of each sale and type of product sold
filled['value']=0
filled['value']=filled['quantity']*filled['price']
filled['category']='Parts'


#split the date of each sale into month of the year
for i in range(len(filled)):
    date  = filled.loc[i,'salesdate']
    month = int(date.rsplit(sep='-')[1])
    filled.loc[i,'month']= month

#label the product type for each transaction
values1 = {'1000':'Touring','2000':'Touring','3000':'Touring','Frame':'Frame'}
values2 = {'Jersey':'Clothing','Socks':'Clothing','Gloves':'Clothing','Vest':'Clothing',
          'Tights':'Clothing','Shorts':'Clothing','100':'Mountain','200':'Mountain','300':'Mountain','400':'Mountain','500':'Mountain','600':'Mountain',
          '150':'Road','250':'Road','350':'Road','450':'Road','550':'Road','650':'Road','750':'Road'}
for i in range(len(filled)):
    description = filled.loc[i,'name']
    for key in list(values2.keys()):
        if description.find(key)>0:
            filled.loc[i,'category'] = values2[key]
            break
        else:
            continue
    for key in list(values1.keys()):
        if description.find(key)>0:
            filled.loc[i,'category'] = values1[key]
            break
        else:
            continue
        
#clean the data
filled = filled[filled['value']!=0]




#look at some of the data, first group by last,first and middle name, then count salesdate
#for these groups to get total number of different sales that person has bought
grouped = filled.groupby(['lastname','firstname','middleinitial'])['salesdate'].count()
grouped.unique()

#there are a range of 1 to 4 purchases made by a customer, count to get how many of each
#convert to an array and make a list of values for pie chart
print(grouped.value_counts().describe())
purchases = (grouped.value_counts()).to_numpy()
number    = [1,2,3,4]
fig1, sub  = plt.subplots(1,2)
plt.suptitle('Customer Spending Habits')
bar1 = sub[0].bar(number,purchases, color='xkcd:blue')
sub[0].set_xlabel('Number of Purchases')
sub[0].set_xlim(0,5)
sub[0].set_ylabel('Number of Customers')
sub[0].set_title('Total Number of purchases per Customer')
sub[0].bar_label(bar1)

#group data to get customers with biggest purchases, just to view it
most = (filled.groupby(['lastname','firstname','middleinitial'])['value'].sum()).sort_values(ascending=False)
most = most.head(11)
print(most)

#split sales values into levels of £0-£10000, £10001-£2000, >£20001 and sum them
group = filled.groupby(['lastname','firstname','middleinitial'])['value'].sum()
top   = (group>20001).sum()
bottom= (group<10001).sum()
middle= len(group)-top-bottom
print(group.describe())
bar2 = sub[1].bar(['Under £10000','£10001-£20000','Over £20001'],[bottom,middle,top],color='xkcd:blue')
sub[1].bar_label(bar2)
sub[1].set_xlabel('Expenditure (£)')
sub[1].set_ylabel('Number of Customers')
sub[1].set_title('Distribution of Customer Spending')
plt.show()




#next split in terms of expendature by the category of products purchased.
#Select purchases by category bike, then group by name and sum revenue. slit into
#expenditure bands
bikes    = filled[(filled['category']=='Road') | (filled['category']=='Touring') |(filled['category']=='Mountain')]
bikes    = bikes.groupby(['lastname','firstname','middleinitial'])['value'].sum()
top_b    = (bikes>20001).sum()
bottom_b = (bikes<10001).sum()
middle_b = len(bikes)-top_b-bottom_b
print(bikes.describe())
fig2, axs = plt.subplots(1,2)
plt.suptitle('Customer Expenditure by Type')
bars3 = axs[0].bar(['Under £10000','£10001-£20000','Over £20001'],[bottom_b,middle_b,top_b],color='xkcd:blue')
axs[0].bar_label(bars3)
axs[0].set_xlabel('Expenditure (£)')
axs[0].set_ylabel('Number of Customers')
axs[0].set_title('Bikes')

#Do the same for frames
frames    = filled[(filled['category']=='Frame')]
frames    = frames.groupby(['lastname','firstname','middleinitial'])['value'].sum()
top_f    = (frames>10001).sum()
bottom_f = (frames<5001).sum()
middle_f = len(frames)-top_f-bottom_f
print(frames.describe())
bars4 = axs[1].bar(['Under £5000','£5001-£10000','Over £10001'],[bottom_f,middle_f,top_f],color='xkcd:blue')
axs[1].bar_label(bars4)
axs[1].set_xlabel('Expenditure (£)')
axs[1].set_ylabel('Number of Customers')
axs[1].set_title('Frames')
plt.show()

#and again for parts
parts    = filled[(filled['category']=='Parts')]
parts    = parts.groupby(['lastname','firstname','middleinitial'])['value'].sum()
top_p    = (parts>5001).sum()
bottom_p = (parts<3001).sum()
middle_p = len(parts)-top_p-bottom_p
print(parts.describe())
fig3, axs1 = plt.subplots(1,2)
plt.suptitle('Customer Expenditure by Type')
bars5 = axs1[0].bar(['Under £3000','£3001-£5000','Over £5001'],[bottom_p,middle_p,top_p],color='xkcd:blue')
axs1[0].bar_label(bars5)
axs1[0].set_xlabel('Expenditure (£)')
axs1[0].set_ylabel('Number of Customers')
axs1[0].set_title('Parts')

#finally for clothing
clothing    = filled[(filled['category']=='Clothing')]
clothing    = clothing.groupby(['lastname','firstname','middleinitial'])['value'].sum()
top_c    = (clothing>401).sum()
bottom_c = (clothing<201).sum()
middle_c = len(clothing)-top_c-bottom_c
print(clothing.describe())
bars6 = axs1[1].bar(['Under £200','£201-£400','Over £401'],[bottom_c,middle_c,top_c],color='xkcd:blue')
axs1[1].bar_label(bars6)
axs1[1].set_xlabel('Expenditure (£)')
axs1[1].set_ylabel('Number of Customers')
axs1[1].set_title('Clothing')
plt.show()

import pandas as pd
import numpy as np
from decimal import Decimal
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sn
import os
import plotly.graph_objs as go
import plotly.offline as py
# py.init_notebook_mode(connected=True)
# pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 9999
pd.options.display.float_format = '{:20,.2f}'.format


DataSet = pd.read_csv('SCMS_Delivery_History_Dataset.csv').fillna(0)

TotalRowCount = len(DataSet)
print("Total Number of Data Count :", TotalRowCount)

print(DataSet.dtypes)
DataSet.head(10)

#Total 10 Country wise count with graph
DataSet = DataSet.dropna()
ItemCount = DataSet["Country"].value_counts().nlargest(10)
print("Top 10 Countries Wise Count \n")
print(ItemCount)
sn.set_context("talk",font_scale=1)
plt.figure(figsize=(22,6))
sn.countplot(DataSet['Country'],order = DataSet['Country'].value_counts().nlargest(10).index)
plt.title('Top 10 Countries Wise Count \n')
plt.ylabel('Total Count')
plt.xlabel('Country Name')
plt.show()

#Total Pack Price for Top 15 Countries with graph
TotalPrice = DataSet.groupby(['Country'])['Pack Price'].sum().nlargest(15)
print("Total Pack Price for Top 15 Countries\n")
print(TotalPrice)
plt.figure(figsize=(22,6))
GraphData=DataSet.groupby(['Country'])['Pack Price'].sum().nlargest(15)
GraphData.plot(kind='bar')
plt.ylabel('Total Pack Price')
plt.xlabel('Country Name')
plt.show()

#First Line Designation Wise Count
sn.set_context("talk",font_scale=1)
plt.figure(figsize=(5,6))
sn.countplot(DataSet['First Line Designation'],order = DataSet['First Line Designation'].value_counts().nlargest(10).index)
plt.title('First Line Designation Wise Count \n')
plt.ylabel('Total Count')
plt.xlabel('First Line Designation')
plt.show()

#Shipment Mode percentage wise Pie Chart
# ShippingMode = DataSet["Shipment Mode"].value_counts()
# labels = (np.array(ShippingMode.index))
# sizes = (np.array((ShippingMode / ShippingMode.sum())*100))
#
# trace = go.Pie(labels=labels, values=sizes)
# layout = go.Layout(title="Shipment Mode")
# dat = [trace]
# fig = go.Figure(data=dat, layout=layout)
# py.iplot(fig, filename="Shipment Mode")
# plt.show()

#Unquie Manufacturing Site Names
UniqueItem = DataSet['Manufacturing Site'].unique()
print("All Unique Manufacturing Site \n")
print(UniqueItem)

#Shipment Mode, Min and Mean value for Air
ItemData=DataSet[DataSet['Shipment Mode']=='Air']
print ("The Max Air Shipment Mode is :",ItemData['Unit of Measure (Per Pack)'].max())
print ("The Min Air Shipment is :",ItemData['Unit of Measure (Per Pack)'].min())
ItemTypeMean = ItemData['Unit of Measure (Per Pack)'].mean()
print ("The Mean Air Shipment is :", round(ItemTypeMean,2))

#Top 10 Manufacturing Site for all Shipment Mode with Graph
plt.figure(figsize=(22,6))
TopFiveManufacturingSite=DataSet.groupby('Manufacturing Site').size().nlargest(10)
print(TopFiveManufacturingSite)
TopFiveManufacturingSite.plot(kind='bar')
plt.title('Top 10 Manufacturing Site \n')
plt.ylabel('Total Count')
plt.xlabel('Manufacturing Site Name')
plt.show()

#Top 10 Manufacturing Site for Air Shipment Mode with Graph
# Top 10 Air Shipment Mode in Bar Chart
ItemData=DataSet[DataSet['Shipment Mode']=='Air']
DataSet[DataSet["Shipment Mode"]=='Air']['Manufacturing Site'].value_counts()[0:10].to_frame().plot.bar(figsize=(22,6))
ItemSupplier = DataSet[DataSet["Shipment Mode"]=='Air']['Manufacturing Site'].value_counts()[0:10]
print("Top 10 Air Manufacturing Site \n")
print(ItemSupplier)
plt.title('Top 10 Air Manufacturing Site\n')
plt.ylabel('Air Count')
plt.xlabel('Manufacturing Site')
plt.show()

#Shipment Mode and Pack Price in Bar Plot Graph
plt.subplots(figsize = (18,6))
plt.xticks(rotation = 90)
sn.barplot('Shipment Mode','Pack Price', data = DataSet)
plt.show()


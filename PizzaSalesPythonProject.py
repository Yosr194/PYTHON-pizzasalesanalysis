#!/usr/bin/env python
# coding: utf-8

# ### Importing Necessary libraries

# In[252]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ### Importing Dataset

# In[255]:


df=pd.read_csv(r"D:\pizza sales python\pizza_sales.csv")


# ### Exploring the dataset

# In[257]:


df.head()


# In[258]:


df.tail()


# In[259]:


print("The Metadata of the dataset: ", df.shape)


# In[260]:


print("The Rows of the dataset: ", df.shape[0])


# In[261]:


print("The Columns of the dataset: ", df.shape[1])


# In[262]:


df.columns


# In[266]:


df.info


# ### Data Types in Raw Data 

# In[273]:


df.dtypes


# In[275]:


df.describe ()


# ### KPI's

# In[278]:


total_revenue =df["total_price"].sum()
total_pizza_sold=df["quantity"].sum()
total_orders=df["order_id"].nunique()
Average_order_Value=total_revenue/total_orders
Average_pizza_per_order= total_pizza_sold/total_orders

print(f"Total Revenue : ${total_revenue:,.2f}")
print(f"Total Pizzas Sold : {total_pizza_sold:,}")
print(f"Total Orders : {total_orders}")
print(f"Average Order Value : ${Average_order_Value:,.2f}")
print(f"Average Pizza Per Order : {Average_pizza_per_order:,.2f}")





# ### Chart's

# #### Ingredient analysis

# In[282]:


ingredient = ( df["pizza_ingredients"].str.split(',').explode().str.strip().value_counts().reset_index().rename(columns={'index':'Count', 'pizza_ingredients':'Ingredients'}))
print(ingredient.head(15))
    


# #### Daily trend _ Total orders

# In[284]:


df['order_date']=pd.to_datetime(df['order_date'], dayfirst=True)
df['day_name']=df['order_date'].dt.day_name()
weekday_order=["Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['day_name']=pd.Categorical(df['day_name'],categories=weekday_order, ordered=True)
orders_by_day=df.groupby('day_name', observed=False)['order_id'].nunique()
ax = orders_by_day.plot(kind='bar', figsize=(8,5), color= '#FEF9E7', edgecolor='#F39C12')
print(orders_by_day)
plt.title("Total Orders by Day of Week")  
plt.xlabel("Day of Week")                 
plt.ylabel("Number of Orders")            
plt.xticks(rotation=45)  
for i, val in enumerate(orders_by_day):
    plt.text(i, val+ 20 , str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()              
    




# In[286]:


df['order_date']=pd.to_datetime(df['order_date'], dayfirst=True)
df['day_name']=df['order_date'].dt.day_name()
weekday_order=["Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['day_name']=pd.Categorical(df['day_name'],categories=weekday_order, ordered=True)
orders_by_day=df.groupby('day_name', observed=False)['total_price'].sum()
ax = orders_by_day.plot(kind='bar', figsize=(8,5), color= '#FEF9E7', edgecolor='#F39C12')
print(orders_by_day)
plt.title("Total Revenue by Day of Week")  
plt.xlabel("Day of Week")                 
plt.ylabel("Total Revenue")            
plt.xticks(rotation=45)  
for i, val in enumerate(orders_by_day):
    plt.text(i, val+ 20 , str(f" ${val:,.0f}"), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()              
    




# In[288]:


df['order_date']=pd.to_datetime(df['order_date'], dayfirst=True)
df['day_name']=df['order_date'].dt.day_name()
weekday_order=["Monday" , "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
df['day_name']=pd.Categorical(df['day_name'],categories=weekday_order, ordered=True)
orders_by_day=df.groupby('day_name', observed=False)['quantity'].sum()
ax = orders_by_day.plot(kind='bar', figsize=(8,5), color= '#FEF9E7', edgecolor='#F39C12')
print(orders_by_day)
plt.title("Total quantity by Day of Week")  
plt.xlabel("Day of Week")                 
plt.ylabel("Total quantity")            
plt.xticks(rotation=45)  
for i, val in enumerate(orders_by_day):
    plt.text(i, val+ 20 , str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()              
    




# #### Hourly Trend_Total Orders

# In[309]:


df['order_time']=pd.to_datetime(df['order_time'],format = '%H:%M:%S')
df['order_hour']=df['order_time'].dt.hour
orders_by_hour=df.groupby('order_hour',observed=False)['order_id'].nunique()
ax=orders_by_hour.plot(kind='bar', figsize=(10,5), color= '#FEF9E7', edgecolor='#F39C12')
plt.title("Total orders by Hour of Day")  
plt.xlabel("Hour of Day (24-Hour Format)")                 
plt.ylabel("Number of orders")            
plt.xticks(rotation=0)  
for i, val in enumerate(orders_by_hour):
    plt.text(i, val+ 5 , str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()          


# In[319]:


df['order_time']=pd.to_datetime(df['order_time'],format = '%H:%M:%S')
df['order_hour']=df['order_time'].dt.hour
orders_by_hour=df.groupby('order_hour',observed=False)['total_price'].sum()
ax=orders_by_hour.plot(kind='bar', figsize=(10,5), color= '#FEF9E7', edgecolor='#F39C12')
plt.title("Total Revenue by Hour of Day")  
plt.xlabel("Hour of Day (24-Hour Format)")                 
plt.ylabel("Total Revenue")            
plt.xticks(rotation=0)  
for i, val in enumerate(orders_by_hour):
    plt.text(i, val+ 5 , str(f"${val:,.0f}"), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()          


# In[321]:


df['order_time']=pd.to_datetime(df['order_time'],format = '%H:%M:%S')
df['order_hour']=df['order_time'].dt.hour
orders_by_hour=df.groupby('order_hour',observed=False)['quantity'].sum()
ax=orders_by_hour.plot(kind='bar', figsize=(10,5), color= '#FEF9E7', edgecolor='#F39C12')
plt.title("Total quantity by Hour of Day")  
plt.xlabel("Hour of Day (24-Hour Format)")                 
plt.ylabel("Total Quantity")            
plt.xticks(rotation=0)  
for i, val in enumerate(orders_by_hour):
    plt.text(i, val+ 5 , str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')
plt.tight_layout()  
plt.show()          


# #### Monthly trend _ Total orders

# In[330]:


df['order_date']=pd.to_datetime(df['order_date'], dayfirst=True)
df['month_name']=df['order_date'].dt.month_name()
month_order = ["January", "February", "March", "April", "May", "June", 
               "July", "August", "September", "October", "November", "December"]

df['month_name'] = pd.Categorical(df['month_name'], categories=month_order, ordered=True)
orders_by_month = df.groupby('month_name', observed=False)['order_id'].nunique()

plt.figure(figsize=(10, 5))

plt.fill_between(orders_by_month.index, orders_by_month.values, 
                 color="orange", alpha=0.6)

plt.plot(orders_by_month.index, orders_by_month.values, 
         color='black', linewidth=2, marker='o', markersize=8)
         
plt.title("Total Orders by Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation=45)


for i,val in enumerate(orders_by_month):
    plt.text(i, val + 20, f"{val:,}", 
             ha='center', va='bottom', fontsize=9, fontweight='bold')
           


plt.tight_layout()
plt.show()


# #### % of Sales for pizza Category

# In[339]:


category_sales=df.groupby('pizza_category')['total_price'].sum()
category_pct= category_sales/category_sales.sum()*100
plt.figure(figsize=(7,7))
colors=plt.get_cmap('tab20').colors
plt.pie(category_pct, labels=category_pct.index,autopct='%1.1f%%',startangle=90, colors=colors,wedgeprops={'edgecolor':'black','width':0.4})
plt.title("Percentage of Sales By Pizza Category")
plt.show()


# #### % of  sales by size and category

# In[353]:


sales_pivot = df.pivot_table(
    index="pizza_category",
    columns="pizza_size",
    values="total_price",
    aggfunc='sum',
    fill_value=0
)

sales_pct = sales_pivot / sales_pivot.sum().sum() * 100

plt.figure(figsize=(10,6))
sns.heatmap(sales_pct, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5)
plt.title("% of Sales by Pizza Category and Size")
plt.ylabel("Pizza Category")
plt.xlabel("Pizza Size")
plt.show()


# #### Total Pizzas Sold By Pizza Category

# In[351]:


pizzas_by_category = df.groupby("pizza_category")["quantity"].sum()

colors = list(plt.get_cmap('tab10').colors)
colors = colors[:len(pizzas_by_category)]

ax = pizzas_by_category.plot(kind="bar", figsize=(8,5), color=colors, edgecolor="black")

plt.title("Total Pizza Sold by Pizza Category")
plt.xlabel("Pizza Category")
plt.ylabel("Total Pizza's Sold")
plt.xticks(rotation=45)

for i, val in enumerate(pizzas_by_category):
    plt.text(i, val + 5, str(val), ha="center", va="bottom", fontsize=9, fontweight="bold")

plt.tight_layout()
plt.show()


# #### Top 5 best_selling Pizzas _ By total orders

# In[369]:


pizzas_by_name = df.groupby('pizza_name')['quantity'].sum()

top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("Top 5 Best-Selling Pizzas - Total Quantity")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### Top 5 best_selling Pizzas _ By number of ordered pizzas

# In[418]:


pizzas_by_name = df.groupby('pizza_name')['order_id'].nunique()

top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("Top 5  Pizzas Ordered")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas ordered")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### Top 5 best_selling Pizzas _ By total sales

# In[394]:


pizzas_by_name = df.groupby('pizza_name')['total_price'].sum()

top5 = pizzas_by_name.sort_values(ascending=False).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("Top 5 Best-Selling Pizzas - Total Revenue")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold revenue")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(f"${val:,}"), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### Bottom 5 best_selling Pizzas _ By total orders

# In[416]:


pizzas_by_name = df.groupby('pizza_name')['quantity'].sum()

top5 = pizzas_by_name.sort_values(ascending=True).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("Bottom 5 Selling Pizzas - Total quantity")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas ordered")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### Bottom 5 worst_selling Pizzas _ By number of ordered pizzas

# In[413]:


pizzas_by_name = df.groupby('pizza_name')['order_id'].nunique()

top5 = pizzas_by_name.sort_values(ascending=True).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("Bottom 5  Pizzas Ordered")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Ordered")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(val), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# #### Bottom 5 worst_selling Pizzas _ By total sales

# In[404]:


pizzas_by_name = df.groupby('pizza_name')['total_price'].sum()

top5 = pizzas_by_name.sort_values(ascending=True).head(5)

ax = top5.plot(kind='bar', figsize=(8,5), color='grey', edgecolor='black')

plt.title("bottom 5 woestt-Selling Pizzas - Total Revenue")
plt.xlabel("Pizza Name")
plt.ylabel("Total Pizzas Sold revenue")
plt.xticks(rotation=45)

for i, val in enumerate(top5):
    plt.text(i, val + 2, str(f"${val:,}"), ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.show()


# In[ ]:





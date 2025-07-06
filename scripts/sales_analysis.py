# consider sales dataset and analyse it in a proper way
#expectation:need a clarity on who is spending more money for shopping in case of gender,age_group,state,occupation,product_category,marital_status


#import all necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#read the sales data csv file
df = pd.read_csv('C:/Users/Shashi Reddy/OneDrive/Desktop/pyspiders/python_libraries/sales_data(1).csv',encoding='ISO-8859-1')
#printing all the columns
print(df.columns)

#fetching null data from amount column
print(df[df['Amount'].isnull()])

# #dropping all the unwanted columns such as status and unnamed1
df.drop(['Status','unnamed1'],axis=1,inplace=True)
print(df)


##delete all nan values from the dataframe
df.dropna(inplace=True)
print(df)


# rename the column marital_status to marital
df.rename(columns={'Marital_Status':'Marital'},inplace=True)
print(df.columns)


#change the values  of marital col 0-->single,1-->married
newmarital={0:'Single',1:'Married'}
df['Marital']=df['Marital'].replace(newmarital) #we can use replace instead of map
print(df)


#change the values of gender col F-->Memale and M-->Male
newgender={'M':'Male','F':'Female'}
df['Gender']=df['Gender'].replace(newgender) #we can use replace instead of map
print(df)


#visualize the count of males and females baseed on gender columnn using seaborn
# sns.countplot(x='Gender',data=df)
#or we can use the below code
v=sns.countplot(x=df['Gender'],data=df,hue='Gender',palette='dark')
for i in v.containers:
    v.bar_label(i)
plt.show()


#group by gender and agegroup,state,occupation,product_category,marital_status
#for age group
v1=sns.countplot(x=df['Age Group'],data=df,hue='Gender',palette='dark')
for i in v.containers:
    v1.bar_label(i)
plt.show()

#for state
v2=sns.countplot(x=df['State'],data=df,hue='Gender',palette='dark')
for i in v.containers:
    v2.bar_label(i)
plt.show()
a=df.groupby('State')['Amount'].sum()
state=pd.DataFrame(a)
plt.figure(figsize=(25,5))
sns.barplot(x=state.index,y=state.Amount)
plt.show()

#for occupation
plt.figure(figsize=(25,5))
a=df.groupby('State')['Occupation'].sum()
state=pd.DataFrame(a)
v3=sns.countplot(x='Occupation',data=df,hue='Gender',palette='bright')
for i in v3.containers:
    v3.bar_label(i)
plt.show()

#for product_category
plt.figure(figsize=(25,5))
a=df.groupby('State')['Product_Category'].sum()
state=pd.DataFrame(a)
v4=sns.countplot(x='Product_Category',data=df,hue='Gender',palette='bright')
for i in v4.containers:
    v4.bar_label(i)
plt.show()

#for marital status
plt.figure(figsize=(25,5))
v5=sns.countplot(x='Marital',data=df,hue='Gender',palette='bright')
for i in v5.containers:
    v5.bar_label(i)
plt.show()

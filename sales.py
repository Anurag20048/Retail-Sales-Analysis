import pandas as pd
import matplotlib.pyplot as plt
from unicodedata import category

# Load dataset
df = pd.read_csv(
    "C:/Users/ANURAG PAREEK/Downloads/archive (4)/Sample - Superstore.csv",
    encoding='latin1'
)

# Preview data
print("First 5 rows:\n", df.head())

# Data info
print("\nData Info:")
print(df.info())

# Statistical summary
print("\nSummary Statistics:\n", df.describe())

# Check missing values
print("\nMissing Values:\n", df.isnull().sum())

# Column names
print("\nColumns:\n", df.columns)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Check if any Ship Date is missing
print("\nMissing Ship Dates:\n", df[df['Ship Date'].isnull()])

# Create new features
df['year'] = df['Order Date'].dt.year
df['month'] = df['Order Date'].dt.month

# Group data (Year + Month)
monthly_sales = df.groupby(['year', 'month'])['Sales'].sum().reset_index()

print("\nMonthly Sales Data:\n", monthly_sales.head())
# Create proper time series
df['YearMonth'] = df['Order Date'].dt.to_period('M')

monthly_sales = df.groupby('YearMonth')['Sales'].sum()
monthly_sales.index = monthly_sales.index.to_timestamp()

# Plot clean graph
plt.figure(figsize=(12,5))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')

plt.xticks(rotation=45)
plt.grid()

plt.show()
import seaborn as sns
# Group data by Category
Category_analysis=df.groupby('Category')[['Sales','Profit']].sum().reset_index()
#plot sales by category
plt.figure(figsize=(8,5))
sns.barplot(x='Category',y='Sales',data=Category_analysis)
plt.title('Category Sales')
plt.xlabel('Category')
plt.ylabel(' total Sales')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))
sns.barplot(x='Category',y='Profit',data=Category_analysis)
plt.title('Category Profit')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.show()
sub_category =df.groupby('Sub-Category')[['Sales','Profit']].sum().reset_index()
sub_category_sorted=sub_category.sort_values(by=['Profit'])
print(sub_category_sorted)
plt.figure(figsize=(8,5))
sns.barplot(x='Profit', y='Sub-Category', data=sub_category_sorted)
plt.title('profit by sub-category')
plt.xlabel('profit')
plt.ylabel('sub-category')
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(8,5))

sns.scatterplot(
    x='Discount',
    y='Profit',
    hue='Category',
    data=df
)

plt.title("Discount vs Profit by Category")
plt.show()
top_customers=df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind='bar',figsize=(8,5))
plt.title('Top 10 Customers by Sales')
plt.xlabel('Customer Name')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.show()
import datetime as dt
today =df['Order Date'].max()
rfm=df.groupby('Customer Name').agg({'Order Date':lambda x:(today-x.max()).days,'Order ID':'count','Sales':'sum'})
rfm.columns=['Recency','Frequency','Monetary']
print(rfm.head())
def segment_customer(row):
    if row ['Monetary']>5000 and row['Frequency'] > 5:
        return 'High value'
    elif row ['Monetary']<2000:
        return 'medium value'
    else:
        return 'low value'
rfm['Segment']=rfm.apply(segment_customer, axis=1)
print(rfm.head())
sns.countplot(x='Segment',data=rfm)
plt.title("customer Segment")
plt.show()

#!/usr/bin/env python
# coding: utf-8

# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[1]:


import pandas as pd

# Creating a Pandas Series from a list
data = [4, 8, 15, 16, 23, 42]
series1 = pd.Series(data)

# Printing the Series
print("Series 1:")
print(series1)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.
# 
# 

# In[2]:


import pandas as pd

# Creating a list variable with 10 elements
list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Creating a Pandas Series from the list variable
series2 = pd.Series(list_data)

# Printing the Series
print("Series 2:")
print(series2)


# Q3. Create a Pandas DataFrame that contains the following data:
# 
# Then, print the DataFrame.

# In[3]:


import pandas as pd

# Creating a dictionary with the given data
data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}

# Creating a Pandas DataFrame
df = pd.DataFrame(data)

# Printing the DataFrame
print("DataFrame:")
print(df)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# Certainly! Here's a concise comparison between DataFrame and Series in Pandas, along with examples:
# 
# ### DataFrame:
# - **Definition**: A DataFrame in Pandas is a 2-dimensional labeled data structure with columns of potentially different types.
# - **Example**:
# ```python
# import pandas as pd
# 
# # Example DataFrame
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 27],
#     'Gender': ['Female', 'Male', 'Male']
# }
# 
# df = pd.DataFrame(data)
# print("DataFrame:")
# print(df)
# ```
# Output:
# ```
# DataFrame:
#       Name  Age  Gender
# 0    Alice   25  Female
# 1      Bob   30    Male
# 2  Charlie   27    Male
# ```
# 
# ### Series:
# - **Definition**: A Series in Pandas is a 1-dimensional labeled array capable of holding data of any type.
# - **Example**:
# ```python
# import pandas as pd
# 
# # Example Series
# ages = pd.Series([25, 30, 27])
# 
# print("Series:")
# print(ages)
# ```
# Output:
# ```
# Series:
# 0    25
# 1    30
# 2    27
# dtype: int64
# ```
# 
# **Key Differences**:
# - **Dimensionality**: DataFrame is 2-dimensional (rows and columns), while Series is 1-dimensional (single column or row).
# - **Structure**: DataFrame is tabular, Series is a single column or row of data.
# - **Usage**: DataFrame is used for structured data management and operations across columns and rows, while Series is typically used for manipulating a single column or row of data.

# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# Pandas offers a wide range of functions to manipulate data within a DataFrame. Here are some common functions along with examples of when you might use them:
# 
# ### Common Functions for DataFrame Manipulation:
# 
# 1. **`head()` and `tail()`**:
#    - **Use**: View the first or last few rows of the DataFrame.
#    - **Example**:
#      ```python
#      import pandas as pd
# 
#      # Example DataFrame
#      data = {
#          'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
#          'Age': [25, 30, 27, 22, 35],
#          'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
#      }
#      df = pd.DataFrame(data)
# 
#      # Using head() to view the first 3 rows
#      print("First 3 rows:")
#      print(df.head(3))
# 
#      # Using tail() to view the last 2 rows
#      print("\nLast 2 rows:")
#      print(df.tail(2))
#      ```
# 
# 2. **`describe()`**:
#    - **Use**: Generates descriptive statistics summary (count, mean, std, min, max, etc.) of numeric columns.
#    - **Example**:
#      ```python
#      # Using describe() to get summary statistics
#      print("\nSummary statistics:")
#      print(df.describe())
#      ```
# 
# 3. **`info()`**:
#    - **Use**: Provides a concise summary of the DataFrame, including data types, non-null values, and memory usage.
#    - **Example**:
#      ```python
#      # Using info() to get DataFrame information
#      print("\nDataFrame information:")
#      print(df.info())
#      ```
# 
# 4. **Indexing and Selection (`loc[]`, `iloc[]`)**:
#    - **Use**: Access subsets of rows and columns using labels (`loc[]`) or integer indices (`iloc[]`).
#    - **Example**:
#      ```python
#      # Using loc[] to select rows and columns by labels
#      print("\nSelecting rows and columns:")
#      print(df.loc[df['Age'] > 25, ['Name', 'Age']])
# 
#      # Using iloc[] to select rows and columns by integer indices
#      print("\nSelecting rows and columns by index:")
#      print(df.iloc[1:3, :])
#      ```
# 
# 5. **`drop()`**:
#    - **Use**: Remove rows or columns from the DataFrame.
#    - **Example**:
#      ```python
#      # Using drop() to remove columns
#      df_dropped = df.drop(['Gender'], axis=1)
#      print("\nDataFrame after dropping 'Gender' column:")
#      print(df_dropped)
#      ```
# 
# 6. **`fillna()`**:
#    - **Use**: Fill missing values with specified values or methods.
#    - **Example**:
#      ```python
#      # Example DataFrame with missing values
#      data_missing = {
#          'Name': ['Alice', 'Bob', 'Charlie', None, 'Emily'],
#          'Age': [25, 30, 27, None, 35],
#          'Gender': ['Female', 'Male', 'Male', 'Male', 'Female']
#      }
#      df_missing = pd.DataFrame(data_missing)
# 
#      # Using fillna() to fill missing values with median age
#      median_age = df_missing['Age'].median()
#      df_missing['Age'].fillna(median_age, inplace=True)
#      print("\nDataFrame after filling missing values:")
#      print(df_missing)
#      ```
# 
# 7. **`groupby()`**:
#    - **Use**: Group data by values of one or more columns and perform aggregate functions (e.g., sum, mean, count) on them.
#    - **Example**:
#      ```python
#      # Using groupby() to group by 'Gender' and calculate mean age
#      grouped_data = df.groupby('Gender')['Age'].mean()
#      print("\nMean age by gender:")
#      print(grouped_data)
#      ```
# 
# ### Example Scenario:
# 
# - **Scenario**: You have a DataFrame `sales_data` containing sales figures for different products across regions. You need to analyze the sales performance by calculating the total sales for each product.
# 
# - **Solution**:
#    ```python
#    # Example scenario: Calculate total sales by product
#    import pandas as pd
# 
#    # Example DataFrame
#    data = {
#        'Product': ['A', 'B', 'A', 'B', 'C'],
#        'Region': ['East', 'West', 'North', 'South', 'East'],
#        'Sales': [100, 150, 200, 175, 120]
#    }
#    sales_data = pd.DataFrame(data)
# 
#    # Using groupby() to group by 'Product' and calculate total sales
#    total_sales = sales_data.groupby('Product')['Sales'].sum()
#    print("\nTotal sales by product:")
#    print(total_sales)
#    ```
# 
#    Output:
#    ```
#    Total sales by product:
#    Product
#    A    300
#    B    325
#    C    120
#    Name: Sales, dtype: int64
#    ```
# 
# In this example, `groupby()` is used to group the sales data by 'Product', and `sum()` is applied to calculate the total sales for each product. These functions (`head()`, `describe()`, `groupby()`, etc.) are fundamental for data exploration, analysis, and manipulation in Pandas DataFrames.

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# Among Series, DataFrame, and Panel in Pandas, **DataFrame** is mutable in nature.
# 
# - **DataFrame**: DataFrames in Pandas are mutable, meaning you can modify their contents after creation. You can add or remove columns, change values within the DataFrame, and perform various operations that alter the structure or content of the DataFrame.
# 
# - **Series**: Series in Pandas are also mutable. You can modify elements in a Series, change the index, or append new elements to it.
# 
# - **Panel**: Panels were a 3-dimensional data structure in earlier versions of Pandas, allowing for data manipulation across three axes (items, major_axis, minor_axis). However, Panels have been deprecated since Pandas version 0.25.0 in favor of using MultiIndex or simply 3D NumPy arrays. Panels were mutable when they existed, but it's recommended to use other structures for similar functionalities now.
# 
# In summary, both Series and DataFrame are mutable in nature, whereas Panel was mutable before it was deprecated. For current data manipulation tasks in Pandas, focus on using Series and DataFrame.

# Q7. Create a DataFrame using multiple Series. Explain with an example.

# To create a DataFrame using multiple Series in Pandas, you can combine these Series into a dictionary and then convert the dictionary into a DataFrame. Here’s an example to illustrate this:
# 
# ```python
# import pandas as pd
# 
# # Creating Series for Name, Age, and Gender
# names = pd.Series(['Alice', 'Bob', 'Claire'])
# ages = pd.Series([25, 30, 27])
# genders = pd.Series(['Female', 'Male', 'Female'])
# 
# # Creating a DataFrame from these Series
# df = pd.DataFrame({
#     'Name': names,
#     'Age': ages,
#     'Gender': genders
# })
# 
# # Printing the DataFrame
# print("DataFrame:")
# print(df)
# ```
# 
# Output:
# ```
# DataFrame:
#      Name  Age  Gender
# 0   Alice   25  Female
# 1     Bob   30    Male
# 2  Claire   27  Female
# ```
# 
# ### Explanation:
# 
# 1. **Creating Series**:
#    - We first create three separate Pandas Series: `names`, `ages`, and `genders`. Each Series represents a column of data (`Name`, `Age`, `Gender`).
# 
# 2. **Creating DataFrame from Series**:
#    - We then create a dictionary where the keys are the column names (`'Name'`, `'Age'`, `'Gender'`) and the values are the corresponding Series (`names`, `ages`, `genders`).
#    - Using `pd.DataFrame()`, we convert this dictionary into a DataFrame `df`.
# 
# 3. **Printing the DataFrame**:
#    - Finally, we print the DataFrame `df`, which now contains the data from the individual Series organized into rows and columns.
# 
# This method allows you to efficiently create a DataFrame from multiple Series, leveraging the flexibility and ease of use provided by Pandas. Each Series corresponds to a column in the resulting DataFrame, making it straightforward to work with structured data in Python.

# In[ ]:





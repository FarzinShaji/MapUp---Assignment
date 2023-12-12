#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df1 = pd.read_csv('dataset-1.csv')
df2 = pd.read_csv('dataset-2.csv')


# ### Question 1

# In[4]:


def generate_car_matrix(df1):
    matrix = df1.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    matrix.values[np.arange(matrix.shape[0]), np.arange(matrix.shape[0])] = 0
    return matrix

result_matrix = generate_car_matrix(df1)
result_matrix


# ### Question 2

# In[6]:


def get_type_count(df1):
    df1['car_type'] = pd.cut(df1['car'], bins=[-np.inf, 15, 25, np.inf], labels=['low', 'medium', 'high'], right=False)
    car_type_counts = df1['car_type'].value_counts().to_dict()
    sorted_car_type_counts = dict(sorted(car_type_counts.items()))
    return sorted_car_type_counts

result_dict = get_type_count(df1)
result_dict


# ### Question 3

# In[7]:


def get_bus_indexes(df1):
    mean_bus = df1['bus'].mean()
    bus_indexes = df1[df1['bus'] > 2 * mean_bus].index.tolist()
    sorted_bus_indexes = sorted(bus_indexes)
    return sorted_bus_indexes

result_indexes = get_bus_indexes(df1)
result_indexes


# ### Question 4

# In[8]:


def filter_routes(df1):
    route_avg_truck = df1.groupby('route')['truck'].mean()
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()
    filtered_routes.sort()
    return filtered_routes

result_routes = filter_routes(df1)
result_routes


# ### Question 5

# In[10]:


def multiply_matrix(matrix):
    modified_matrix = matrix.copy()
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25
    modified_matrix = modified_matrix.round(1)
    return modified_matrix

result_matrix = generate_car_matrix(df1)
modified_result = multiply_matrix(result_matrix)
modified_result


# ### Question 6

# In[11]:


def time_check(df2):
    df2['startTime'] = pd.to_datetime(df2['startTime'])
    df2['endTime'] = pd.to_datetime(df2['endTime'])
    df2['is_condition_true'] = (df2['endTime'] - df2['startTime']) == pd.Timedelta('23:59:59')
    result_series = df2['is_condition_true']
    return result_series

result_bool_series = time_check(df2)
result_bool_series


# In[ ]:





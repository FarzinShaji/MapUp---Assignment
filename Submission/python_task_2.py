#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np


# In[2]:


df1 = pd.read_csv('dataset-1.csv')
df2 = pd.read_csv('dataset-2.csv')
df3 = pd.read_csv('dataset-3.csv')


# In[66]:


df3.head()


# ### Question 1

# In[67]:


def calculate_distance_matrix(df3):
    distances = {}
    for index, row in df3.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']
        distances[(id_start, id_end)] = distance
        distances[(id_end, id_start)] = distance 
        
        unique_ids = sorted(set(df3['id_start'].unique()) | set(df3['id_end'].unique()))
    distance_matrix = pd.DataFrame(index=unique_ids, columns=unique_ids)
    
    for id_start in unique_ids:
        for id_end in unique_ids:
            if id_start == id_end:
                distance_matrix.at[id_start, id_end] = 0
            elif (id_start, id_end) in distances:
                distance_matrix.at[id_start, id_end] = distances[(id_start, id_end)]
            else:
                known_routes = [(id_start, mid_point, id_end) for mid_point in unique_ids if (id_start, mid_point) in distances and (mid_point, id_end) in distances]
                cumulative_distance = sum(distances[(start, mid_point)] for start, mid_point, end in known_routes)
                distance_matrix.at[id_start, id_end] = cumulative_distance

    return distance_matrix

def unroll_distance_matrix(df):
    unrolled_df = df3.melt(id_vars=['id_start', 'id_end'], value_vars='distance', value_name='distance')[['id_start', 'id_end', 'distance']]
    return(unrolled_df)

result_matrix = calculate_distance_matrix(df3)
result_matrix


# ### Question 2

# In[65]:


def unroll_distance_matrix(distance_matrix):
    distance_matrix_reset = distance_matrix.reset_index()
    unrolled_df = pd.melt(distance_matrix_reset, id_vars='id_start', var_name='id_end', value_name='distance')

    unrolled_df = unrolled_df[unrolled_df['id_start'] != unrolled_df['id_end']] 
    return unrolled_df

distance_matrix = calculate_distance_matrix('dataset-3.csv')
unrolled_result = unroll_distance_matrix(distance_matrix)
unrolled_result


# ### Question 4

# In[57]:


def calculate_toll_rate(df3):
    
    df['moto'] = 0.8 * df['distance']
    df['car'] = 1.2 * df['distance']
    df['rv'] = 1.5 * df['distance']
    df['bus'] = 2.2 * df['distance']
    df['truck'] = 3.6 * df['distance']

    return df

result_df_with_toll_rates = calculate_toll_rate(df3)
result_df_with_toll_rates


# In[ ]:





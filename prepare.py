import pandas as pd
import numpy as np
import datetime

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (8,6)
import warnings
warnings.filterwarnings("ignore")

import seaborn as sns

#######  STORES DATA ########

def stores_convert_datetime():
    '''Function will take in stores, items, sales csv's, merge them and convert date column to datetime format'''

    ### load csv files ###
    stores = pd.read_csv('stores.csv')
    sales = pd.read_csv('sales.csv')
    items = pd.read_csv('items.csv')   

    ### merge into one df ### 
    # first left merge items & sales
    items_sales = items.merge(sales, left_on='item_id', right_on='item')

    #next merge stores onto items_sales to produce one df
    merged = items_sales_stores = items_sales.merge(stores, left_on='store', right_on='store_id')

    # then need to drop Unnamed columns created when merging
    merged = merged.drop(columns=(['Unnamed: 0', 'Unnamed: 0_y', 'Unnamed: 0_x']))

    # next convert date column (sales_date only date column) into datetime format
    merged.sale_date = pd.to_datetime(merged.sale_date)

    # finally, need to drop the empty time section
    merged['sale_date'] = pd.to_datetime(merged['sale_date']).dt.date
    
    return merged

def plot_sales_price(merged):
    cols = ['sale_amount', 'item_price']
    for col in cols:
        sns.distplot(merged[col])
        plt.show()

def set_datetime_index(df, target):
    df = df.set_index(target).sort_index()
    return df

def add_sales_total(merged):
    merged['sales_total'] = merged.sale_amount/merged.item_price
    return merged
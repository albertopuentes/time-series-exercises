import requests

# 1) Using the code from the lesson as a guide and the REST API from https://python.zach.lol/api/v1/items as we did in the lesson, create a dataframe named items that has all of the data for items.

def get_items():

    items_list = []

    response = requests.get('https://python.zach.lol/api/v1/items')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/items?page='+str(i)
        response = requests.get(url)
        data = response.json()
        items = data['payload']['items']
        items_list += items

    ### Convert to a dataframe

    items = pd.DataFrame(items_list)

    ### cache into csv

    items.to_csv('items.csv')
    
    return items

# 2) Do the same thing, but for stores (https://python.zach.lol/api/v1/stores)

def get_stores():
    
    stores = []

    response = requests.get('https://python.zach.lol/api/v1/stores')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/stores?page='+str(i)
        response = requests.get(url)
        data = response.json()
        stores_list = data['payload']['stores']
        stores += stores_list

    ### Convert to a dataframe

    stores = pd.DataFrame(stores) 

    ### cache into csv

    stores.to_csv('stores.csv')

    return stores

# 3) Extract the data for sales (https://python.zach.lol/api/v1/sales). There are a lot of pages of data here, so your code will need to be a little more complex. Your code should continue fetching data from the next page until all of the data is extracted.

def get_sales():

    sales_list = []

    response = requests.get('https://python.zach.lol/api/v1/sales')
    data = response.json()
    n = data['payload']['max_page']

    for i in range(1,n+1):
        url = 'https://python.zach.lol/api/v1/sales?page='+str(i)
        response = requests.get(url)
        data = response.json()
        sales_items = data['payload']['sales']
        sales_list += sales_items

    ### Convert to a dataframe

    sales = pd.DataFrame(sales_list)

    ### cache into csv

    sales.to_csv('sales.csv')

    return sales

# 4) Save the data in your files to local csv files so that it will be faster to access in the future.

#  csv cache included in previous functions


# 5) Combine the data from your three separate dataframes into one large dataframe.

def items_sales_stores():
    
    items_sales = items.merge(sales, left_on='item_id', right_on='item')
    items_sales_stores = items_sales.merge(stores, left_on='store', right_on='store_id')

    return items_sales_stores

# 6) Acquire the Open Power Systems Data for Germany, which has been rapidly expanding its renewable energy production in recent years. The data set includes country-wide totals of electricity consumption, wind power production, and solar power production for 2006-2017. You can get the data here: https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv
def power_df():
    
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    power_df = pd.read_csv(url)

    return power_df

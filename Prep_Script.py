import pandas as pd
import numpy as np
import os
import re

df_sales=pd.DataFrame()

def sales_car(df_sales):
    url='https://www.motorbeam.com/top-25-selling-cars-in-february-2023/'
    df_sales=pd.read_html(url)[0]
    df_sales['February ’22 Sales']=df_sales['February ’22 Sales'].str.extract('(\d+)')
    df_sales['February ’22 Sales']=df_sales['February ’22 Sales'].fillna(0)
    df_sales['February ’22 Sales']=df_sales['February ’22 Sales'].astype(np.int64)
    df_sales['Sale_Difference']=df_sales['February ’23 Sales']- df_sales['February ’22 Sales']
    
    return(df_sales)

def get_output_schema():
    return pd.DataFrame({
    'Rank' : prep_int(),
    'OEM' : prep_string(),
    'Model' : prep_string(),
    'February ’23 Sales' : prep_int(),
    'February ’22 Sales' : prep_int(),
    'YoY Growth' : prep_string(),
    'Sale_Difference' : prep_int()

})

import pandas as pd
def encode(input):     
  le = preprocessing.LabelEncoder()
  return pd.DataFrame({
    'Rank': le.fit_transform['Rank'],
    'OEM' : le.fit_transform(input['OEM']),
    'Model' : le.fit_transform(input['Model']),
    'February ’23 Sales' : le.fit_transform(input['February ’23 Sales']),
    'February ’22 Sales' : le.fit_transform(input['February ’22 Sales']),
    'YoY Growth' : le.fit_transform(input['YoY Growth']),
    'Sale_Difference' : le.fit_transform(input['Sale_Difference'])
})

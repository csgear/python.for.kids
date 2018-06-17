
'''
to complete a real world project 
''' 

import pandas as pd 
import numpy as np 

pd.options.mode.chained_assignment = None
pd.set_option('display.max_columns', 60)

import matplotlib.pyplot as plt 

import seaborn as sns
sns.set(font_scale= 2 )

from sklearn.model_selection import train_test_split 

def input_dataset():
    df = pd.read_csv('Energy_and_Water_Data_Disclosure_for_Local_Law_84_2017__Data_for_Calendar_Year_2016_.csv')


    df = df.replace({'Not Available': np.nan})

    for col in list(df.columns):
        if ('ft²' in col or 'kBtu' in col or 'Metric Tons CO2e' in col or 'kWh' in 
            col or 'therms' in col or 'gal' in col or 'Score' in col):
            df[col] = df[col].astype(float)
    
    return df

def drop_mission_columns(df, threshold=50):
    missing_df = missing_values_table(df)

    missing_columns = list(missing_df[ missing_df['% of Total Values' ] > threshold].index)

    df = df.drop(columns = missing_columns)

    return df

# Function to calculate missing values by column
def missing_values_table(df):
    mis_val = df.isnull().sum()
    mis_val_percent = df.isnull().sum() / len(df) * 100.00
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis = 1)

    mis_val_table_ren = mis_val_table.rename(
        columns = {0: 'Missing Values', 1: '% of Total Values'}
    )

    mis_val_table_ren = mis_val_table_ren[mis_val_table_ren.iloc[:,1] !=0].sort_values('% of Total Values', ascending=False).round(1)
    
    return mis_val_table_ren 

if __name__ == '__main__':
    data = input_dataset() 
    
    data = drop_mission_columns(data, threshold=50)
    
    
    

#%%
    
    data = data.rename(columns = {'ENERGY STAR Score': 'score'})
    

#%%
    # print(data.info())
    
    plt.style.use('fivethirtyeight')
    
    plt.hist(data['score'].dropna(), bins=100, edgecolor='k')
    

#%%
    plt.hist(data['Site EUI (kBtu/ft²)'].dropna(), bins=20, edgecolor='k')

#%%
    first_quartile = data['Site EUI (kBtu/ft²)'].describe()['25%']
    third_quartile = data['Site EUI (kBtu/ft²)'].describe()['75%']
    
    iqr = third_quartile - first_quartile 
    
    data = data[ (data['Site EUI (kBtu/ft²)'] > first_quartile - 3 * iqr) & 
                (data['Site EUI (kBtu/ft²)'] < third_quartile + 3 * iqr)] 
    
#%%
    
#%%

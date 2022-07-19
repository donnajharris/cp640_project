##################################################
#
# Final Project: CP640 Machine Learning (S22)
#
# Donna J. Harris (994042890)
# - harr2890@mylaurier.ca
#
##
# 
# Instructions to run:
#
#
##
#
# Also see: 
#
##################################################

import pandas as pd

VERBOSE = 1 #0



def CSV_to_dataframe(pd, filename):
    return pd.read_csv(filename)

def dataframe_to_CSV(df, filename):
    return df.to_csv(filename)


#### Data processing functions ####

# REMOVING columns I will never need
def remove_columns(df):
    if VERBOSE:
        print("Removing unneccesary columns:")
        
    if VERBOSE:
        print("\tRemoving SB...")    
    del df['SB']

    if VERBOSE:
        print("\tRemoving CS...")
    del df['CS']
    
    if VERBOSE:
        print("\tRemoving Pos Summary...")
    del df['Pos Summary']
    
    if VERBOSE:
        print("\tRemoving DFS(DK)...")
    del df['DFS(DK)']
    
    if VERBOSE:
        print("\tRemoving DFS(FD)...")
    del df['DFS(FD)']


    if VERBOSE:
        print("\tRemoving IBB...")
    del df['IBB']
    
    if VERBOSE:
        print("\tRemoving SF...")
    del df['SF']
    
    if VERBOSE:
        print("\tRemoving ROE...")
    del df['ROE']
    
    if VERBOSE:
        print("\tRemoving GDP...")
    del df['GDP']
    
    
    if VERBOSE:
        print("... Done removing unneccesary columns.")
    
    return df


# EXTRACTING data from columns
def extract_data(df):

    if VERBOSE:
        print("Extracting data from columns:")
        
    
    if VERBOSE:
        print("\tSplitting Rslt into Result and Score columns...")   
    df[['Result','Score']] = df['Rslt'].str.split(' ', expand=True)
    
    if VERBOSE:
        print("\tRemoving Rslt...")  
    del df['Rslt']


    if VERBOSE:
        print("\tExtracing Season year from Date...")  
    df['Season'] = df['Date'].str[:4]
    
    
    if VERBOSE:
        print("... Done extracting data.")
    return df


# REMOVE problematic rows
def remove_rows(df):
    
    print("not droping rows yet...")
    
    return df
    

def process_data(df):
    
    if VERBOSE:
        print("Pre-processing data.")
    df = remove_columns(df)
    df = extract_data(df)
    df = remove_rows(df)
    
    if VERBOSE:
        print("... Pre-processing completed.")

    return df



###


# Load local file as data source


if VERBOSE:
    print("Reading from original data file: mlbbatting1901-2021.csv")
    
original_data_source = "./data/mlbbatting1901-2021.csv"
#df = pd.read_csv(original_data_source)
df = CSV_to_dataframe(pd, original_data_source)

if VERBOSE:
    print("... Done reading original data file.")

print(df.head())


# data processing

cleaned = process_data(df)

print(cleaned.head())

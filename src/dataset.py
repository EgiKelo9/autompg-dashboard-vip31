from ucimlrepo import fetch_ucirepo 
import pandas as pd

def load_and_clean_data():
    # fetch dataset 
    auto_mpg = fetch_ucirepo(id=9) 
    
    # data (as pandas dataframes) 
    X = auto_mpg.data.features 
    y = auto_mpg.data.targets 
    
    # Combine features and target
    df = pd.concat([X, y], axis=1)
    
    # Convert data types as per variable information
    integer_cols = ['cylinders', 'model_year', 'origin']
    for col in integer_cols:
        if col in df.columns:
            df[col] = df[col].astype(int)
            
    # Fill horsepower missing values with mean
    if 'horsepower' in df.columns:
        df['horsepower'].fillna(df['horsepower'].mean(), inplace=True)
    
    # Reset index after dropping rows
    df = df.reset_index(drop=True)
    
    return df

# Load and clean the data
dataset = load_and_clean_data()

# Print basic information
print("\nDataset shape:", dataset.shape)
print("\nDataset info:")
print(dataset.info())
print("\nFirst few rows:")
print(dataset.head())
print("\nMissing values:")
print(dataset.isnull().sum())
print("\nUnique values per column:")
print(dataset.nunique())
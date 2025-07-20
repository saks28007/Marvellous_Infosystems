import pandas as pd
import numpy as np

def create_missing_values_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja', 'Rahul'],
        'Age': [25, np.nan, 28, np.nan],
        'Marks': [85, 90, np.nan, 70]
    }
    df = pd.DataFrame(data)
    return df

def drop_missing_rows(df):
    print("Original DataFrame:")
    print(df)
    df_cleaned = df.dropna()
    print("\nDataFrame after dropping rows with missing values:")
    print(df_cleaned)
    return df_cleaned

if __name__ == "__main__":
    df = create_missing_values_dataframe()
    drop_missing_rows(df)

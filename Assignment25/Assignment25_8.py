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

def fill_missing_with_mean(df):
    print("Original DataFrame:")
    print(df)
    df_filled = df.copy()
    df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())
    df_filled['Marks'] = df_filled['Marks'].fillna(df_filled['Marks'].mean())
    print("\nDataFrame after filling missing values with mean:")
    print(df_filled)
    return df_filled

if __name__ == "__main__":
    df = create_missing_values_dataframe()
    fill_missing_with_mean(df)

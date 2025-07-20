import pandas as pd

def create_duplicates_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja', 'Amit', 'Sagar'],
        'Marks': [85, 90, 78, 85, 90]
    }
    df = pd.DataFrame(data)
    return df

def remove_duplicates(df):
    print("Original DataFrame:")
    print(df)
    df_cleaned = df.drop_duplicates()
    print("\nDataFrame after removing duplicate rows:")
    print(df_cleaned)
    return df_cleaned

if __name__ == "__main__":
    df = create_duplicates_dataframe()
    remove_duplicates(df)

import pandas as pd

def create_age_dataframe():
    data = {
        'Name': ['A', 'B', 'C'],
        'Age': [21.0, 22.0, 23.0]
    }
    df = pd.DataFrame(data)
    return df

def convert_age_to_int(df):
    print("Data types before conversion:")
    print(df.dtypes)
    df['Age'] = df['Age'].astype(int)
    print("\nData types after converting 'Age' to int:")
    print(df.dtypes)
    print("\nUpdated DataFrame:")
    print(df)
    return df

if __name__ == "__main__":
    df = create_age_dataframe()
    convert_age_to_int(df)

import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    return df

def drop_english_column(df):
    df_dropped = df.drop('English', axis=1)
    print("DataFrame after dropping 'English' column:")
    print(df_dropped)
    return df_dropped

if __name__ == "__main__":
    df = create_dataframe()
    drop_english_column(df)

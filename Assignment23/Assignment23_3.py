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

def add_total_column(df):
    df['Total'] = df['Math'] + df['Science'] + df['English']
    print("DataFrame with 'Total' column:")
    print(df)

if __name__ == "__main__":
    df = create_dataframe()
    add_total_column(df)

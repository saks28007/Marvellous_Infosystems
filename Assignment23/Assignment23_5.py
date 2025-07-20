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

def replace_name(df):
    df['Name'] = df['Name'].replace('Pooja', 'Puja')
    print("DataFrame after replacing 'Pooja' with 'Puja':")
    print(df)

if __name__ == "__main__":
    df = create_dataframe()
    replace_name(df)

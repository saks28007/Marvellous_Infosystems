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

def show_basic_info(df):
    print("DataFrame:")
    print(df)
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    print("\nData Types:")
    print(df.dtypes)

if __name__ == "__main__":
    df = create_dataframe()
    show_basic_info(df)

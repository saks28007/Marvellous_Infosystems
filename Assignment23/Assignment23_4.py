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

def filter_high_science(df):
    high_science = df[df['Science'] > 85]
    print("Students with Science marks greater than 85:")
    print(high_science)

if __name__ == "__main__":
    df = create_dataframe()
    filter_high_science(df)

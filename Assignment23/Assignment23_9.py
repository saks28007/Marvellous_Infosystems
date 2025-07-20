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

def display_name_math(df):
    subset = df[['Name', 'Math']]
    print("Only 'Name' and 'Math' columns:")
    print(subset)

if __name__ == "__main__":
    df = create_dataframe()
    display_name_math(df)

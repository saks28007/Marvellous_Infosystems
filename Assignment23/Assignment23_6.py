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

def sort_by_math(df):
    sorted_df = df.sort_values(by='Math', ascending=False)
    print("DataFrame sorted by 'Math' marks (descending):")
    print(sorted_df)

if __name__ == "__main__":
    df = create_dataframe()
    sort_by_math(df)

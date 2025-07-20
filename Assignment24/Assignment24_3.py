import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82],
        'Gender': ['Male', 'Male', 'Female']
    }
    df = pd.DataFrame(data)
    return df

def group_by_gender_avg(df):
    grouped = df.groupby('Gender').mean(numeric_only=True)
    print("Average marks grouped by gender:")
    print(grouped)
    return grouped

if __name__ == "__main__":
    df = create_dataframe()
    group_by_gender_avg(df)

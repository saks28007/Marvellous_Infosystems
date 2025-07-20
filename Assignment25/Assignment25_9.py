import pandas as pd

def create_duplicates_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja', 'Amit', 'Sagar'],
        'Marks': [85, 90, 78, 85, 90]
    }
    df = pd.DataFrame(data)
    return df

def detect_duplicates(df):
    print("Original DataFrame:")
    print(df)
    duplicates = df[df.duplicated()]
    print("\nDetected duplicate rows:")
    print(duplicates)
    return duplicates

if __name__ == "__main__":
    df = create_duplicates_dataframe()
    detect_duplicates(df)

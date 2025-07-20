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

def one_hot_encode_gender(df):
    df_encoded = pd.get_dummies(df, columns=['Gender'])
    print("DataFrame after one-hot encoding 'Gender':")
    print(df_encoded)
    return df_encoded

if __name__ == "__main__":
    df = create_dataframe()
    one_hot_encode_gender(df)

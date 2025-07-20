import pandas as pd
from sklearn.model_selection import train_test_split

def create_age_purchased_dataframe():
    data = {
        'Age': [22, 25, 47, 52, 46, 56],
        'Purchased': [0, 1, 1, 0, 1, 0]
    }
    df = pd.DataFrame(data)
    return df

def split_train_test(df):
    X = df[['Age']]
    y = df['Purchased']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    print("X_train:")
    print(X_train)
    print("\nX_test:")
    print(X_test)
    print("\ny_train:")
    print(y_train)
    print("\ny_test:")
    print(y_test)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = create_age_purchased_dataframe()
    split_train_test(df)

import pandas as pd

def create_department_dataframe():
    data = {'Department': ['HR', 'IT', 'Finance', 'HR', 'IT']}
    df = pd.DataFrame(data)
    return df

def one_hot_encode_department(df):
    df_encoded = pd.get_dummies(df, columns=['Department'])
    print("DataFrame after One-Hot Encoding 'Department':")
    print(df_encoded)
    return df_encoded

if __name__ == "__main__":
    df = create_department_dataframe()
    one_hot_encode_department(df)

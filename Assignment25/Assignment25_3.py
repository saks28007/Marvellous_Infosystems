import pandas as pd
from sklearn.preprocessing import LabelEncoder

def create_city_dataframe():
    data = {'City': ['Pune', 'Mumbai', 'Delhi', 'Pune', 'Delhi']}
    df = pd.DataFrame(data)
    return df

def label_encode_city(df):
    le = LabelEncoder()
    df['City_Label'] = le.fit_transform(df['City'])
    print("DataFrame after Label Encoding 'City':")
    print(df)
    return df

if __name__ == "__main__":
    df = create_city_dataframe()
    label_encode_city(df)

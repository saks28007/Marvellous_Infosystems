import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def create_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    return df

def normalize_math_scores(df):
    scaler = MinMaxScaler()
    df['Math_Normalized'] = scaler.fit_transform(df[['Math']])
    print("DataFrame with normalized 'Math' scores:")
    print(df)
    return df

if __name__ == "__main__":
    df = create_dataframe()
    normalize_math_scores(df)

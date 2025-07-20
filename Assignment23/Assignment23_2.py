import pandas as pd

def createdataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    return df

def show_descriptive_stats(df):
    print("Descriptive Statistics:")
    print(df.describe())

if __name__ == "__main__":
    df = createdataframe()
    show_descriptive_stats(df)

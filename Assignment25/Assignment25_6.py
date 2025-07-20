import pandas as pd

def create_grade_dataframe():
    data = {'Grade': ['A+', 'A', 'B+', 'B', 'C']}
    df = pd.DataFrame(data)
    return df

def replace_grades(df):
    replace_dict = {
        'A+': 'Excellent',
        'A': 'Very Good',
        'B+': 'Good',
        'B': 'Average',
        'C': 'Poor'
    }
    df['Grade'] = df['Grade'].replace(replace_dict)
    print("DataFrame after replacing grades:")
    print(df)
    return df

if __name__ == "__main__":
    df = create_grade_dataframe()
    replace_grades(df)

import pandas as pd

def create_salary_dataframe():
    data = {'Salary': [25000, 27000, 29000, 31000, 50000, 100000]}
    df = pd.DataFrame(data)
    return df

def detect_outliers_iqr(df):
    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df['Salary'] < lower_bound) | (df['Salary'] > upper_bound)]
    print("Detected outliers in 'Salary' column using IQR method:")
    print(outliers)
    return outliers

if __name__ == "__main__":
    df = create_salary_dataframe()
    detect_outliers_iqr(df)

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

def add_status_column(df):
    df['Total'] = df['Math'] + df['Science'] + df['English']
    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >= 250 else 'Fail')
    return df

def count_passed_students(df):
    passed_count = df[df['Status'] == 'Pass'].shape[0]
    print(f"Number of students who passed: {passed_count}")
    return passed_count

if __name__ == "__main__":
    df = create_dataframe()
    df = add_status_column(df)
    count_passed_students(df)

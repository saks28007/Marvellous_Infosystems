import pandas as pd

def create_dataframe():
    data = {
        'Name': ['Amit', 'Sagar', 'Pooja'],
        'Math': [85, 90, 78],
        'Science': [92, 88, 80],
        'English': [75, 85, 82]
    }
    df = pd.DataFrame(data)
    return df

def save_to_csv(df, student_marks.csv):
    df.to_csv(student_marks, index=False)
    print(f"DataFrame saved to '{student_marks}'")

if __name__ == "__main__":
    df = create_dataframe()
    save_to_csv(df, 'student_marks.csv')

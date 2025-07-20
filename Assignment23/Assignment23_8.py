import pandas as pd

def read_from_csv():
    df = pd.read_csv('student_marks.csv')
    print(f"DataFrame loaded from student_marks: ")
    print(df)
    return df

if __name__ == "__main__":
    df_loaded = read_from_csv('student_marks.csv')

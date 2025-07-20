import pandas as pd

def read_grouped_avg_csv(student_marks):
    df_grouped = pd.read_csv('student_marks.csv')
    print(f"Grouped average marks loaded from '{student_marks}':")
    print(df_grouped)
    return df_grouped

if __name__ == "__main__":
    read_grouped_avg_csv('gender_average_marks.csv')

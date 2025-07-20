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

def save_grouped_avg_to_csv(df, student_marks):
    grouped = df.groupby('Gender').mean(numeric_only=True)
    grouped.to_csv(student_marks)
    print(f"Grouped average marks saved to '{student_marks}'")

if __name__ == "__main__":
    df = create_dataframe()
    save_grouped_avg_to_csv(df, 'gender_average_marks.csv')

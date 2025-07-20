import pandas as pd
import matplotlib.pyplot as plt

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

def plot_pie_for_sagar(df):
    sagar_row = df[df['Name'] == 'Sagar']
    if not sagar_row.empty:
        subjects = ['Math', 'Science', 'English']
        marks = sagar_row[subjects].iloc[0]
        plt.figure(figsize=(6,6))
        plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=140)
        plt.title("Subject Marks Distribution for Sagar")
        plt.show()
    else:
        print("No student named 'Sagar' found!")

if __name__ == "__main__":
    df = create_dataframe()
    plot_pie_for_sagar(df)

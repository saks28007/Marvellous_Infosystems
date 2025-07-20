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

def plot_avg_marks_by_gender(df):
    grouped = df.groupby('Gender').mean(numeric_only=True)
    grouped[['Math', 'Science', 'English']].plot(kind='bar')
    plt.title('Average Marks by Gender')
    plt.ylabel('Average Marks')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    df = create_dataframe()
    plot_avg_marks_by_gender(df)

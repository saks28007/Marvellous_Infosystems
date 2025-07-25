
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Step 1: Load Data
    df = pd.read_csv('Advertising (1).csv')
    print("\nDataset Head:\n", df.head())

    # Step 2: Prepare Data
    X = df[['TV', 'Radio', 'Newspaper']]  # Or 'Television' if that's the column name
    y = df['Sales']

    # Step 3: Split Data (50% train, 50% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    # Step 4: Train Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Step 5: Test Model
    y_pred = model.predict(X_test)

    # Display Results
    results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print("\nResults:\n", results.head(10))

    # Additional metrics
    print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
    print("R2 Score:", r2_score(y_test, y_pred))

if __name__ == "__main__":
    main()

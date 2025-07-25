

import pandas as pd
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():

    data = pd.read_csv('PlayPredictor.csv')
    print("\nDataset:\n", data)

    
    X = data[['Wether', 'Temperature']]
    y = data['Play']

    
    le_weather = preprocessing.LabelEncoder()
    le_temp = preprocessing.LabelEncoder()
    le_play = preprocessing.LabelEncoder()

    X['Wether'] = le_weather.fit_transform(X['Wether'])
    X['Temperature'] = le_temp.fit_transform(X['Temperature'])
    y = le_play.fit_transform(y)

    print("\nEncoded Features:\n", X)
    print("\nEncoded Target:\n", y)

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    
    y_pred = model.predict(X_test)
    print("\nAccuracy:", accuracy_score(y_test, y_pred))

    
    weather_input = le_weather.transform(['Sunny'])[0]
    temp_input = le_temp.transform(['Cool'])[0]
    prediction = model.predict([[weather_input, temp_input]])

    print("\nShould play (Sunny & Cool)?", le_play.inverse_transform(prediction)[0])

if __name__ == "__main__":
    main()

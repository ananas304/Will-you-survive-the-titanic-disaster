# prediction/preprocessing.py
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def add_title_and_encode(data):
    # One-hot encoding for categorical features
    data = pd.get_dummies(data, columns=['Title', 'Embarked', 'Sex', 'Pclass'], drop_first=True)

    # Ensure all required columns are present
    required_columns = ['SibSp', 'Parch', 'Fare', 'Title_Miss', 'Title_Mr', 'Title_Mrs', 'Title_Rare', 'Embarked_Q', 'Embarked_S', 'Sex_male', 'Pclass_2', 'Pclass_3']
    for col in required_columns:
        if col not in data.columns:
            data[col] = 0

    # Reorder columns to match model expectations
    data = data[required_columns]
    
    return data

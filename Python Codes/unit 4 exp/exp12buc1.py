import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():

    data = {
        "PassengerId": [1, 2, 3, 4, 5, 6, 7],
        "Survived": [0, 1, 1, 1, 0, 0, 1],
        "Pclass": [3, 1, 3, 1, 3, 3, 1],
        "Name": ["Braund, Mr. Owen Harris", "Cumings, Mrs. John Bradley (Florence Briggs Thayer)",
                 "Heikkinen, Miss. Laina", "Futrelle, Mrs. Jacques Heath (Lily May Peel)",
                 "Allen, Mr. William Henry", "Moran, Mr. James", "McCarthy, Mr. Timothy J"],
        "Age": [22, 38, 26, 35, 35, np.nan, 54],
        "Sex": ["male", "female", "female", "female", "male", "male", "male"],
        "Fare": [7.25, 71.2833, 7.925, 53.1, 8.05, 8.4583, 51.8625],
        "Embarked": ["S", "C", "S", "C", "S", "Q", "S"]
    }
    df = pd.DataFrame(data)
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], kde=True, color='blue', bins=10)
    plt.title('Distribution of Passenger Ages', fontsize=16)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()
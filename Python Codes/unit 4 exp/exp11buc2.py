import pandas as pd

def main():
    data = {
        "Name": ["Jack", "Bob", "Joe", None, "Max"],
        "Age": [25, 30, None, 22, 29],
        "Salary": [50000, None, 45000, 48000, None]
    }
    df = pd.DataFrame(data)
    print(df)
    missing_columns = df.columns[df.isnull().any()]
    print("Columns with missing values:")
    print(missing_columns)

if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()
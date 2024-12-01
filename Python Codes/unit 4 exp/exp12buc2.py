import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    data = {
        "ApplicantID": [1, 2, 3, 4, 5, 6, 7],
        "LoanAmount": [5000, 20000, 15000, 30000, 25000, 35000, 4000],
        "Income": [50000, 60000, 75000, 80000, 95000, 120000, 55000],
        "CreditScore": [650, 700, 720, 680, 750, 780, 600],
        "EmploymentStatus": ["Employed", "Self-Employed", "Employed", "Employed", "Self-Employed", "Employed", "Unemployed"],
        "Default": ["No", "Yes", "No", "No", "Yes", "No", "Yes"]
    }
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x="LoanAmount", hue="Default", multiple="stack", bins=10)
    plt.title('Distribution of Loan Amounts for Approved vs Defaulted Loans', fontsize=16)
    plt.xlabel('Loan Amount', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()


if __name__ == "__main__":
    print("_________________________________________")
    print("SY-5, VedantBarhate, Rno-59")
    print("_________________________________________")
    main()
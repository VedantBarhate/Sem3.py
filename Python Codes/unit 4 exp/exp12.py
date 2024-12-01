import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create a sample customer churn DataFrame
data = {
    "CustomerID": [101, 102, 103, 104, 105, 106, 107],
    "Gender": ["Male", "Female", "Female", "Male", "Female", "Male", "Female"],
    "Age": [25, 34, 45, np.nan, 29, 40, 35],
    "Tenure": [2, 5, 8, 1, np.nan, 7, 3],
    "MonthlyCharges": [29.85, 56.95, 53.85, 42.30, 70.35, 89.10, np.nan],
    "TotalCharges": [150.5, 500.2, 430.8, 180.0, 350.6, 630.3, np.nan],
    "Churn": ["No", "Yes", "No", "No", "Yes", "Yes", "No"]
}

df = pd.DataFrame(data)

# 1. Preview the dataset
print("Dataset Head:\n", df.head())
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:\n", df.isnull().sum())
print("\nDescriptive Statistics:\n", df.describe())

# 2. Handle missing values
# Fill numerical columns with their mean and categorical columns with the mode
for column in df.columns:
    if df[column].dtype == 'object':
        df[column].fillna(df[column].mode()[0], inplace=True)
    else:
        df[column].fillna(df[column].mean(), inplace=True)

print("\nMissing Values after handling:\n", df.isnull().sum())

# 3. Categorical vs Numerical Analysis
categorical_cols = df.select_dtypes(include=['object']).columns
numerical_cols = df.select_dtypes(include=['number']).columns
print("\nCategorical Columns:", categorical_cols)
print("\nNumerical Columns:", numerical_cols)

# 4. Visualization of categorical data
plt.figure(figsize=(10, 6))
for col in categorical_cols:
    plt.figure()
    sns.countplot(data=df, x=col)
    plt.title(f"Distribution of {col}")
    plt.xticks(rotation=45)
    plt.show()

# 5. Visualize numerical data
plt.figure(figsize=(10, 6))
for col in numerical_cols:
    plt.figure()
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

# 6. Correlation analysis for numerical features
plt.figure(figsize=(12, 8))
correlation_matrix = df[numerical_cols].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# 7. Outlier detection using boxplots
plt.figure(figsize=(10, 6))
for col in numerical_cols:
    plt.figure()
    sns.boxplot(data=df, y=col)
    plt.title(f"Outliers in {col}")
    plt.show()

# 8. Relationship between features
plt.figure(figsize=(12, 8))
sns.pairplot(df, hue="Churn")  # Assuming 'Churn' is the target column
plt.show()

# 9. Data Cleaning
# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove outliers (using Z-Score method)
from scipy.stats import zscore

z_scores = np.abs(zscore(df[numerical_cols]))
df = df[(z_scores < 3).all(axis=1)]

# 10. Encode categorical features
df = pd.get_dummies(df, drop_first=True)

print("\nCleaned Dataset Head:\n", df.head())

# Save cleaned data
df.to_csv("cleaned_customer_churn_sample.csv", index=False)
print("Cleaned dataset saved as 'cleaned_customer_churn_sample.csv'")

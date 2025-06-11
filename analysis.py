Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    """Loads data from a CSV file."""
    return pd.read_csv(file_path)

def plot_churn_distribution(df):
    """Plots the distribution of the churn column."""
    df['churn'].value_counts().plot(kind='bar')
    plt.title('Customer Churn Distribution')
    plt.xlabel('Churn')
    plt.ylabel('Count')
    plt.show()

print("Added data visualization function.")

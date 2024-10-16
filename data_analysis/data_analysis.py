import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into a pandas DataFrame
file_path = './ITNETUSERP2ZAF.csv'
df = pd.read_csv(file_path)

# Data Cleaning
# Convert 'DATE' to datetime format
df['DATE'] = pd.to_datetime(df['DATE'], errors='coerce')

# Check for duplicates and remove them
df.drop_duplicates(inplace=True)

# Display basic information about the dataset
def basic_info(df):
    print("Dataset Information:")
    print(df.info())
    print("\nDataset Shape: ", df.shape)
    print("\nSample Data:\n", df.head())
    print("\nSummary Statistics:\n", df.describe())

# Visualizing Data Distributions
def visualize_distributions(df):
    # Histogram of ITNETUSERP2ZAF column
    plt.figure(figsize=(8,6))
    sns.histplot(df['ITNETUSERP2ZAF'], bins=10, kde=True)
    plt.title('Distribution of Internet Users (%) in South Africa')
    plt.xlabel('Internet Users (%)')
    plt.ylabel('Frequency')
    plt.show()

    # Time Series Plot
    plt.figure(figsize=(10,6))
    sns.lineplot(x='DATE', y='ITNETUSERP2ZAF', data=df, marker="o")
    plt.title('Internet Users (%) Over Time in South Africa')
    plt.xlabel('Year')
    plt.ylabel('Internet Users (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Exploratory Data Analysis (EDA)
def explore_data(df):
    print("\nDescriptive Statistics:\n", df.describe())
    print("\nChecking for Missing Data:\n", df.isnull().sum())

    # Correlation matrix (since we have only one numeric column, this is just illustrative)
    plt.figure(figsize=(6,4))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix')
    plt.show()

# Main execution flow
if __name__ == "__main__":
    # Display basic info
    basic_info(df)

    # Explore the data and visualize
    explore_data(df)
    visualize_distributions(df)


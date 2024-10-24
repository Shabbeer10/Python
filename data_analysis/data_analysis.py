import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset into DataFrame ----------------------
file_path = './INTERNETUSERS.csv'
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Data Cleaning ---------------------------------------
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

# Visualizing Data ----------------------------------------------
def visualize_distributions(df):
    # Histogram of INTERNETUSERS column
    plt.figure(figsize=(8,6))
    sns.histplot(df['INTERNETUSERS'], bins=10, kde=True)
    plt.title('Distribution of Internet Users (%) in South Africa')
    plt.xlabel('Internet Users (%)')
    plt.ylabel('Frequency')
    plt.show()

    # Time Series Plot
    plt.figure(figsize=(10,6))
    sns.lineplot(x='DATE', y='INTERNETUSERS', data=df, marker="o")
    plt.title('Internet Users (%) Over Time in South Africa')
    plt.xlabel('Year')
    plt.ylabel('Internet Users (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()

# Exploratory Data Analysis (EDA)
def explore_data(df):
    print("\nChecking for Missing Data:\n", df.isnull().sum())

# Main execution flow
if __name__ == "__main__":
    # Display basic info
    basic_info(df)

    # Explore the data and visualize
    explore_data(df)
    visualize_distributions(df)


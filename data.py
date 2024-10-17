import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = './data_analysis/ITNETUSERP2ZAF.csv'
data_file = pd.read_csv(file_path)

# Data Cleaning, converting 'DATE' to datetime
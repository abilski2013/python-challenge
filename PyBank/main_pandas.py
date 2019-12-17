import os
import pandas as pd
data_file = "resources/budget_data.csv"
data_file_pd = pd.read_csv(data_file)
print(data_file_pd.head())


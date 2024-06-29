import csv
import pandas as pd

# Importing CSV
data_file = pd.read_csv('data.csv')

# Good panda frame
data_file = data_file[["Annual_Income", "Monthly_Inhand_Salary", "ID", "Occupation", "Outstanding_Debt", "Amount_invested_monthly", "Monthly_Balance"]]

# Export to CSV file
data_file.to_csv('proper_data.csv')
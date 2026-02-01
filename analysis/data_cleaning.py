import pandas as pd

df = pd.read_csv("../data/student_data.csv")

print(df.info())
print(df.isnull().sum())

# No missing values – dataset clean

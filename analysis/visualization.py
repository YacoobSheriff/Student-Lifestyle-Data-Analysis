import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("../data/student_data.csv")

sns.scatterplot(x="Study_Hours", y="Score", data=df)
plt.title("Study Hours vs Score")
plt.show()

sns.barplot(x="Sleep_Hours", y="Score", data=df)
plt.title("Sleep Hours vs Score")
plt.show()

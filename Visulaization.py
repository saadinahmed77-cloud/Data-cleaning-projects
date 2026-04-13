import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_titanic.csv")

# 1. Survival count (Bar chart)
df['Survived'].value_counts().plot(kind='bar')
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.show()

# 2. Survival by Gender (Bar chart)
df.groupby('Sex')['Survived'].sum().plot(kind='bar')
plt.title("Survival by Gender")
plt.xlabel("Sex (0 = Male, 1 = Female)")
plt.ylabel("Survivors")
plt.show()

# 3. Age Distribution (Histogram)
df['Age'].plot(kind='hist')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

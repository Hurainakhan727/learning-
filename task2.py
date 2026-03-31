import pandas as pd

# 1. Data load karna
df = pd.read_csv('internship_data.csv')

# 2. Data ka structure dekhna (Variables aur types) [cite: 31]
print("--- Data ki Pehli 5 Rows ---")
print(df.head())

print("\n--- Data Information ---")
print(df.info())

# 3. Trends aur patterns pehchanna [cite: 32]
# Hum check karenge ke kis author ne sab se zyada quotes likhay hain
author_counts = df['Author'].value_counts()
print("\n--- Top Authors aur unke Quotes ki Tadad ---")
print(author_counts)

# 4. Anomalies ya issues detect karna [cite: 33]
missing_data = df.isnull().sum()
print("\n--- Missing Values Check ---")
print(missing_data)
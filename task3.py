import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data load karna
df = pd.read_csv('internship_data.csv')

# 2. Visual design karna (Bar Chart)
plt.figure(figsize=(10, 6))
# Top authors dikhanay ke liye visualization design karein [cite: 36]
sns.countplot(data=df, x='Author', palette='magma')

# 3. Insights wazeh karne ke liye titles lagayein [cite: 36]
plt.title('Author-wise Quote Distribution', fontsize=14)
plt.xlabel('Author Name', fontsize=12)
plt.ylabel('Number of Quotes', fontsize=12)
plt.xticks(rotation=45)

# 4. Final chart save karna [cite: 38]
plt.tight_layout()
plt.savefig('task3_visualization.png')
plt.show()

print("Mubarak ho! Task 3 bhi complete. 'task3_visualization.png' check karein.")
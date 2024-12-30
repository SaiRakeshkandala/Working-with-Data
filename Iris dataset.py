# Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (Iris dataset)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display the first few rows of the dataset
print("Dataset Overview:")
print(df.head())

# Data Manipulation
# 1. Filtering rows where petal_length > 1.5
filtered_data = df[df['petal_length'] > 1.5]
print("\nFiltered Data (Petal Length > 1.5):")
print(filtered_data.head())

# 2. Grouping by species and calculating mean of each numeric column
grouped_data = df.groupby('species').mean()
print("\nGrouped Data (Mean Values by Species):")
print(grouped_data)

# 3. Aggregating: Count of samples per species
species_count = df['species'].value_counts()
print("\nCount of Samples Per Species:")
print(species_count)

# Data Visualization
# 1. Bar plot of average sepal length by species
plt.figure(figsize=(8, 5))
sns.barplot(x=grouped_data.index, y=grouped_data['sepal_length'], palette="viridis")
plt.title('Average Sepal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Sepal Length')
plt.show()

# 2. Scatter plot for sepal length vs petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species', palette='deep')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

# 3. Heatmap of correlations between numeric columns
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

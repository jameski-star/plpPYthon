# Task: Data Analysis and Visualization with pandas, matplotlib, seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set seaborn style for better visuals
sns.set(style="whitegrid")

# Task 1: Load and Explore the Dataset
try:
    # Load Iris dataset from sklearn
    iris = load_iris()
    
    # Convert to DataFrame for easier handling
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    
    # Add target column with species names
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display first 5 rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check data types
    print("\nData types:")
    print(df.dtypes)
    
    # Check missing values
    print("\nMissing values per column:")
    print(df.isnull().sum())
    
    # Clean data (if any missing values were present)
    # Here no missing values, but let's show the code to drop or fill missing values.
    if df.isnull().values.any():
        # Example: fill missing numerical values with column mean
        for col in df.select_dtypes(include='number').columns:
            df[col].fillna(df[col].mean(), inplace=True)
        # Drop rows with any remaining missing values
        df.dropna(inplace=True)
        print("\nMissing values handled.")
    else:
        print("\nNo missing values to handle.")
    
except Exception as e:
    print(f"Error loading or cleaning dataset: {e}")

# Task 2: Basic Data Analysis
try:
    # Basic statistics for numerical columns
    stats = df.describe()
    print("\nBasic statistics of numerical columns:")
    print(stats)
    
    # Grouping: mean petal length by species
    group_mean = df.groupby('species')['petal length (cm)'].mean()
    print("\nMean petal length per species:")
    print(group_mean)
    
    # Insight:
    print("\nInsight:")
    print("Setosa species has the smallest average petal length, while Virginica has the largest.")
    
except Exception as e:
    print(f"Error during basic analysis: {e}")

# Task 3: Data Visualization
try:
    # 1. Line chart - simulate a 'trend over time' using sample index since iris lacks date/time
    plt.figure(figsize=(8,4))
    for species in df['species'].unique():
        subset = df[df['species'] == species]
        plt.plot(subset.index, subset['sepal length (cm)'], label=species)
    plt.title('Sepal Length Trend per Species (by index)')
    plt.xlabel('Sample Index')
    plt.ylabel('Sepal Length (cm)')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # 2. Bar chart - average petal length per species
    plt.figure(figsize=(6,4))
    sns.barplot(x=group_mean.index, y=group_mean.values, palette='pastel')
    plt.title('Average Petal Length per Species')
    plt.xlabel('Species')
    plt.ylabel('Average Petal Length (cm)')
    plt.tight_layout()
    plt.show()
    
    # 3. Histogram - distribution of sepal width
    plt.figure(figsize=(6,4))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True, color='skyblue')
    plt.title('Distribution of Sepal Width')
    plt.xlabel('Sepal Width (cm)')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    # 4. Scatter plot - sepal length vs petal length colored by species
    plt.figure(figsize=(7,5))
    sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', hue='species', palette='deep')
    plt.title('Sepal Length vs Petal Length by Species')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Petal Length (cm)')
    plt.legend(title='Species')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error during visualization: {e}")

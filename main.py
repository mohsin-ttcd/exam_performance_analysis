
# Import pandas and saved give it a nick name pd
import pandas as pd

# Import full table as DataFrame
df = pd.read_csv("Student-Data/StudentsPerformance.csv")

# 1. What are the average marks in Math, Reading, and Writing?

# convert string into integer inside math score
df["math score"] = pd.to_numeric(df["math score"], errors="coerce")
df["reading score"] = pd.to_numeric(df["reading score"], errors="coerce")
df["writing score"] = pd.to_numeric(df["writing score"], errors="coerce")

# cleaning unexpected string
df["math score"] = df["math score"].fillna(0)
df["reading score"] = df["reading score"].fillna(0)
df["writing score"] = df["writing score"].fillna(0)

# average marks in Math, Reading, and Writing
print(f"Average marks in Math: {df['math score'].mean():.2f}")
print(f"Average marks in Reading: {df['reading score'].mean():.2f}")
print(f"Average marks in Writing: {df['writing score'].mean():.2f}")






# Import pandas and saved give it a nick name pd
import pandas as pd

# Import full table as DataFrame
df = pd.read_csv("Student-Data/StudentsPerformance.csv")

# 1. What are the average marks in Math, Reading, and Writing?

# convert string into integer inside score column
df = df.assign(
    **{
        "math score" : pd.to_numeric(df["math score"], errors='coerce').dropna(),
        "reading score" : pd.to_numeric(df["reading score"], errors='coerce').dropna(),
        "writing score" : pd.to_numeric(df["writing score"], errors='coerce').dropna()
    }
)

# average marks in Math, Reading, and Writing
print(f"Average marks in Math: {df['math score'].mean():.2f}")
print(f"Average marks in Reading: {df['reading score'].mean():.2f}")
print(f"Average marks in Writing: {df['writing score'].mean():.2f}")





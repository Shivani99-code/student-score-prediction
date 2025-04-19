import pandas as pd

# Data define karna
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
}

# Data ko DataFrame me convert karna
df = pd.DataFrame(data)

# DataFrame ko CSV file me save karna
df.to_csv('student_scores.csv', index=False)

print("CSV file saved successfully!")

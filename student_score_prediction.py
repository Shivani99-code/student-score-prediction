# Import libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('student_scores.csv')

# Features and Labels
X = data[['Hours']]  # independent variable
y = data['Score']    # dependent variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict the scores
y_pred = model.predict(X_test)

# Compare Actual vs Predicted
print("Actual Scores: ", y_test.values)
print("Predicted Scores: ", y_pred)

# Model Accuracy
print("Model Accuracy (R^2 Score): ", model.score(X_test, y_test))

# Visualization
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.show()

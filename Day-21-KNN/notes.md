# Day 21 - K-Nearest Neighbors (KNN)

## What is K-Nearest Neighbors (KNN)?

K-Nearest Neighbors (KNN) is a **Supervised Machine Learning algorithm**.

It can be used for:

- Classification
- Regression

Unlike Linear Regression or Logistic Regression, KNN does **not** learn an equation or model parameters. Instead, it stores the training data and predicts the output based on the nearest training samples.

---

# Why is it called K-Nearest Neighbors?

```text
K
↓
Number of Neighbors
```

```text
Nearest
↓
Closest according to a distance measure
```

```text
Neighbors
↓
Training samples closest to the new sample
```

Example:

```text
K = 3

Look at the 3 closest neighbors.
```

---

# KNN Workflow

```text
Training Data
      ↓
Store the Data
      ↓
New Sample Arrives
      ↓
Calculate Distance
      ↓
Find K Nearest Neighbors
      ↓
Majority Vote
      ↓
Prediction
```

Unlike many Machine Learning algorithms:

```text
No Equation

No Gradient Descent

No Weight Updates
```

KNN simply stores the training data.

---

# Why is Feature Scaling Important?

KNN is a **distance-based algorithm**.

Suppose we have:

| Person | Age | Salary |
|--------|----:|--------:|
| A | 25 | 30,000 |
| B | 26 | 80,000 |

Differences:

```text
Age Difference = 1

Salary Difference = 50,000
```

Without Feature Scaling, Salary dominates the distance calculation.

After scaling:

```text
Age → 0 to 1

Salary → 0 to 1
```

Now both features contribute fairly.

Therefore, Feature Scaling is usually performed before applying KNN.

---

# Distance Calculation

The most commonly used distance measure in KNN is **Euclidean Distance**.

### Formula

```text
d = √[(x₂ - x₁)² + (y₂ - y₁)²]
```

Example:

Student A:

```text
Hours = 2

Attendance = 70
```

Student B:

```text
Hours = 5

Attendance = 74
```

Distance:

```text
√[(5 - 2)² + (74 - 70)²]

= √(9 + 16)

= √25

= 5
```

A smaller distance means the samples are more similar.

---

# KNN Classification

Suppose we have:

| Hours | Result |
|------:|--------|
|2|Fail|
|3|Fail|
|4|Pass|
|5|Pass|
|6|Pass|

A new student studies:

```text
Hours = 3.8
```

Choose:

```text
K = 3
```

Nearest neighbors:

```text
3 → Fail

4 → Pass

5 → Pass
```

Votes:

```text
Pass = 2

Fail = 1
```

Prediction:

```text
Pass
```

KNN Classification predicts the class receiving the **majority vote**.

---

# Choosing the Value of K

Choosing the correct value of **K** is important.

## Small K

Example:

```text
K = 1
```

Advantages:

- Very flexible
- Captures local patterns

Disadvantages:

- Sensitive to noise
- May overfit

---

## Large K

Example:

```text
K = 25
```

Advantages:

- More stable
- Less affected by noise

Disadvantages:

- May ignore local patterns
- May underfit

---

## Rule of Thumb

A common starting point is:

```text
K ≈ √N
```

Where:

```text
N = Number of Training Samples
```

This is only a guideline.

The best value of **K** is usually selected using validation techniques.

---

# Odd vs Even K

Suppose:

```text
K = 4
```

Votes:

```text
Pass = 2

Fail = 2
```

Tie!

To reduce ties in binary classification, odd values are commonly used.

Examples:

```text
3

5

7

9
```

---

# KNN for Regression

KNN can also solve regression problems.

Suppose nearby house prices are:

```text
₹20 Lakhs

₹22 Lakhs

₹24 Lakhs
```

Prediction:

```text
Average

↓

₹22 Lakhs
```

### Difference

Classification:

```text
Majority Vote
```

Regression:

```text
Average of Neighbor Values
```

---

# Why is KNN called Lazy Learning?

Most Machine Learning algorithms learn a mathematical model during training.

Example:

```text
Linear Regression
↓

Learns an Equation
```

```text
Logistic Regression
↓

Learns Model Weights
```

KNN:

```text
Training
↓

Stores the Training Data
```

Most of the computation happens during prediction.

Therefore, KNN is called a **Lazy Learning Algorithm**.

---

# Scikit-Learn Implementation

## Import

```python
from sklearn.neighbors import KNeighborsClassifier
```

## Create Model

```python
model = KNeighborsClassifier(
    n_neighbors=3
)
```

## Train

```python
model.fit(X_train, y_train)
```

## Predict

```python
predictions = model.predict(X_test)
```

---

# KNN for Regression

```python
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(
    n_neighbors=3
)
```

---

# Complete Workflow

```text
Create Dataset
      ↓
Separate Features (X) and Target (y)
      ↓
Train-Test Split
      ↓
Feature Scaling
      ↓
Create KNN Model
      ↓
Train Model
      ↓
Predict
      ↓
Evaluate
```

---

# Evaluation Metrics

For Classification, common evaluation metrics are:

- Accuracy
- Confusion Matrix
- Classification Report

Example:

```python
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print(accuracy_score(y_test, predictions))

print(confusion_matrix(y_test, predictions))

print(classification_report(y_test, predictions))
```

---

# Advantages

- Easy to understand
- No complex mathematical training
- Works for both Classification and Regression
- Performs well on small datasets

---

# Disadvantages

- Prediction becomes slow for large datasets
- Requires Feature Scaling
- Sensitive to irrelevant features
- Choosing the correct value of **K** is important

---

# When Should We Use KNN?

KNN works well when:

- Dataset size is small or medium.
- Features are properly scaled.
- Similar samples tend to have similar outputs.

KNN is generally not preferred for very large datasets because it compares the new sample with many training samples during prediction.

---

# Quick Revision

```text
KNN
↓
Supervised Learning Algorithm
```

```text
Can Solve
↓

Classification
Regression
```

```text
Training
↓

Stores Training Data
```

```text
Prediction
↓

Calculate Distance
```

```text
Find K Nearest Neighbors
↓

Majority Vote
↓

Classification
```

```text
Average of Neighbor Values
↓

Regression
```

```text
Feature Scaling
↓

Very Important
```

```text
Small K
↓

May Overfit
```

```text
Large K
↓

May Underfit
```

---

# Interview Questions

## 1. What is KNN?

KNN (K-Nearest Neighbors) is a supervised Machine Learning algorithm that predicts the output by looking at the nearest training samples. It can be used for both classification and regression.

---

## 2. Why is KNN called a Lazy Learning algorithm?

KNN does not learn a mathematical model during training. It simply stores the training data and performs most of its computation during prediction.

---

## 3. Why is Feature Scaling important for KNN?

KNN uses distance calculations. If features have different numerical ranges, larger-valued features dominate the distance, leading to poor predictions.

---

## 4. What is the role of K in KNN?

K represents the number of nearest neighbors considered while making a prediction.

---

## 5. Why are odd values of K commonly used?

Odd values help reduce the chances of a tie during majority voting in binary classification.

---

## 6. What happens if K is too small?

The model becomes sensitive to noise and may overfit the training data.

---

## 7. What happens if K is too large?

The model may ignore local patterns and underfit the data.

---

## 8. What is the difference between KNN Classification and KNN Regression?

- **KNN Classification** predicts the class using majority voting among the nearest neighbors.
- **KNN Regression** predicts the output by taking the average of the nearest neighbors' target values.

---

## 9. Which distance metric is commonly used in KNN?

The most commonly used distance metric is **Euclidean Distance**.

Formula:

```text
d = √[(x₂ - x₁)² + (y₂ - y₁)²]
```

---

## 10. What is the complete KNN workflow?

```text
Dataset
    ↓
Train-Test Split
    ↓
Feature Scaling
    ↓
Train KNN
    ↓
Predict
    ↓
Evaluate
```
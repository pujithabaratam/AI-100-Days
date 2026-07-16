# Day 20 - Feature Scaling

## Why Do We Need Feature Scaling?

Feature Scaling is important when there is a large difference between the numerical ranges of features.

Example:

```text
Experience : 1 → 10
Salary     : 30,000 → 120,000
```

Without scaling, features with larger values dominate distance calculations.

### Important

Not every Machine Learning algorithm requires Feature Scaling.

Algorithms that use **distance** are highly affected.

Examples:

- K-Nearest Neighbors (KNN)
- K-Means Clustering
- Support Vector Machine (SVM)
- Neural Networks
- Principal Component Analysis (PCA)

Algorithms like Decision Trees and Random Forests generally do not require Feature Scaling.

---

# What is Feature Scaling?

Feature Scaling transforms feature values into a similar numerical range while preserving the relative information within each feature.

Example:

### Before Scaling

```text
Experience : 1 → 10
Salary     : 30,000 → 120,000
```

### After Scaling

```text
Experience : 0 → 1
Salary     : 0 → 1
```

Now both features contribute more fairly to distance-based calculations.

---

# Types of Feature Scaling

There are two main Feature Scaling techniques:

1. Normalization (Min-Max Scaling)
2. Standardization (Z-Score Scaling)

---

# Normalization (Min-Max Scaling)

Normalization converts feature values into a fixed range.

Usually:

```text
0 → 1
```

### Formula

```text
x' = (x - min(x)) / (max(x) - min(x))
```

### Scikit-Learn

```python
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)
```

---

# Standardization (Z-Score Scaling)

Standardization transforms the data so that:

```text
Mean = 0

Standard Deviation = 1
```

### Formula

```text
z = (x - μ) / σ
```

Where:

```text
μ → Mean

σ → Standard Deviation
```

### Scikit-Learn

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)
```

---

# MinMaxScaler vs StandardScaler

| MinMaxScaler | StandardScaler |
|--------------|----------------|
| Range usually 0 to 1 | Mean = 0, Standard Deviation = 1 |
| Uses Minimum and Maximum values | Uses Mean and Standard Deviation |
| More sensitive to outliers | Often more robust to moderate outliers |
| Useful for bounded scaling | Common default for many ML algorithms |

---

# Why `fit_transform()` and `transform()`?

## fit()

`fit()` learns the parameters from the training data.

### MinMaxScaler learns:

```text
Minimum

Maximum
```

### StandardScaler learns:

```text
Mean

Standard Deviation
```

---

## transform()

`transform()` uses the learned parameters to scale new data.

---

## Correct Workflow

```text
Training Data
      ↓
fit_transform()
```

```text
Testing Data
      ↓
transform()
```

Example:

```python
X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

---

# Why Not Use `fit_transform()` on Test Data?

If we use:

```python
scaler.fit_transform(X_test)
```

the scaler learns information from the test data.

This causes **Data Leakage**, because the model indirectly gains information about the test set before evaluation.

The correct approach is:

```python
scaler.fit(X_train)

X_train = scaler.transform(X_train)

X_test = scaler.transform(X_test)
```

or simply:

```python
X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)
```

---

# Quick Revision

```text
Large Difference in Feature Values
                ↓
Feature Scaling
```

```text
Feature Scaling
        ↓
Normalization
        +
Standardization
```

```text
Normalization
↓
Range usually 0 → 1
```

```text
Standardization
↓
Mean = 0
Standard Deviation = 1
```

```text
Training Data
↓
fit_transform()
```

```text
Testing Data
↓
transform()
```

---

# Interview Questions

## 1. Why is Feature Scaling important?

Feature Scaling ensures that features with larger numerical values do not dominate distance calculations.

---

## 2. Which algorithms require Feature Scaling?

Distance-based algorithms such as KNN, K-Means, SVM, Neural Networks, and PCA benefit from Feature Scaling.

---

## 3. What is the difference between Normalization and Standardization?

Normalization scales values to a fixed range (usually 0 to 1), whereas Standardization transforms the data to have a mean of 0 and a standard deviation of 1.

---

## 4. Why do we use `fit_transform()` for training data but only `transform()` for testing data?

`fit_transform()` learns the scaling parameters and applies them to the training data. `transform()` applies those same learned parameters to the test data without learning new ones.

---

## 5. What is Data Leakage?

Data Leakage occurs when information from the test data is used during training or preprocessing, leading to overly optimistic model evaluation.
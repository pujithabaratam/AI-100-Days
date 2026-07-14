# Day 18 - Classification and Logistic Regression

## What is Classification?

Classification is used when the target represents a **category or class**.

Examples:

```text
Spam / Not Spam
Pass / Fail
Disease / Healthy
Fraud / Not Fraud
PCOS / No PCOS
```

Unlike Regression, Classification predicts a **class or category**.

```text
Regression
↓
Predicts Continuous Values

Classification
↓
Predicts Classes
```

---

## Binary Classification

When the target has only **two possible classes**, it is called **Binary Classification**.

Examples:

```text
0 → Fail
1 → Pass
```

```text
0 → No PCOS
1 → PCOS
```

```text
0 → Not Spam
1 → Spam
```

Usually, binary classes are represented using `0` and `1`.

---

## Why Not Use Linear Regression for Classification?

Linear Regression uses:

```text
ŷ = wx + b
```

Its output can range from:

```text
-∞ to +∞
```

Example predictions:

```text
-0.5
0.3
0.8
1.7
```

But in Binary Classification, we need to predict:

```text
0 or 1
```

If we want to interpret the model output as a probability, the value should be between:

```text
0 and 1
```

Therefore, Logistic Regression uses the **Sigmoid Function** to convert a linear score into a probability.

---

## Logistic Regression Starts With a Linear Equation

Linear Regression uses:

```text
ŷ = wx + b
```

Logistic Regression first calculates a linear score:

```text
z = wx + b
```

For multiple features:

```text
z = w₁x₁ + w₂x₂ + w₃x₃ + b
```

Example:

```text
z =
    w₁ × Hours
  + w₂ × Attendance
  + b
```

The value of `z` can be any real number.

Therefore, Logistic Regression sends `z` through the **Sigmoid Function**.

```text
Input Features
      ↓
z = wx + b
      ↓
Sigmoid Function
      ↓
Probability
      ↓
Decision Threshold
      ↓
Predicted Class
```

---

## Sigmoid Function

The Sigmoid Function is:

```text
σ(z) = 1 / (1 + e⁻ᶻ)
```

The main purpose of the Sigmoid Function is:

```text
Any Real Number
       ↓
Sigmoid
       ↓
Value Between 0 and 1
```

Examples:

```text
z = -10 → Probability close to 0

z = -2  → Probability ≈ 0.119

z = 0   → Probability = 0.5

z = 2   → Probability ≈ 0.881

z = 10  → Probability close to 1
```

The Sigmoid curve has an **S shape**.

### Important

```text
Large Negative z
↓
Probability close to 0
```

```text
z = 0
↓
Probability = 0.5
```

```text
Large Positive z
↓
Probability close to 1
```

---

## Probability in Logistic Regression

Suppose:

```text
Class 0 → Fail
Class 1 → Pass
```

If Logistic Regression produces:

```text
Probability of Class 1 = 0.82
```

It means:

> The model estimates an 82% probability for the positive class, which is Pass in this example.

The probability must then be converted into a predicted class.

---

## Decision Threshold

A common default decision threshold for binary Logistic Regression is:

```text
0.5
```

The decision rule is:

```text
Probability >= 0.5
        ↓
Class 1
```

```text
Probability < 0.5
        ↓
Class 0
```

Examples:

```text
0.20 → Class 0

0.45 → Class 0

0.50 → Class 1

0.78 → Class 1

0.95 → Class 1
```

### Example

Suppose:

```text
Class 0 → Fail
Class 1 → Pass
```

The model predicts:

```text
Probability = 0.82
```

Since:

```text
0.82 >= 0.5
```

The predicted class is:

```text
Class 1 → Pass
```

---

## Train-Test Split for Classification

We can split classification data using:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
```

For Classification problems, `stratify=y` is very useful.

---

## What is `stratify`?

Suppose we have:

```text
100 Samples

90 → Class 0
10 → Class 1
```

This is an **imbalanced dataset**.

During a random split, we do not want a poor class distribution such as:

```text
Training Data:

90 → Class 0
0  → Class 1
```

```text
Testing Data:

0  → Class 0
10 → Class 1
```

The model cannot properly learn Class `1` if the training data contains no Class `1` samples.

`stratify=y` tries to preserve approximately the same target class proportion in the training and testing datasets.

Original dataset:

```text
90% → Class 0
10% → Class 1
```

After stratified splitting, approximately:

```text
Training Data:

90% → Class 0
10% → Class 1
```

```text
Testing Data:

90% → Class 0
10% → Class 1
```

### Definition

> `stratify=y` preserves approximately the same target class distribution during the train-test split.

---

## Training Logistic Regression

Import the model:

```python
from sklearn.linear_model import LogisticRegression
```

Create the model:

```python
model = LogisticRegression()
```

Train the model:

```python
model.fit(X_train, y_train)
```

The basic Scikit-learn workflow is:

```text
Create Model
     ↓
fit()
     ↓
predict()
```

---

## Making Class Predictions

```python
predictions = model.predict(X_test)

print(predictions)
```

`predict()` returns the predicted class.

For Binary Classification:

```text
0 or 1
```

Example:

```text
[1, 0, 1, 1]
```

---

## `predict()` vs `predict_proba()`

### `predict()`

Returns the predicted class.

```python
model.predict(X_test)
```

Example:

```text
[1, 0, 1]
```

### `predict_proba()`

Returns the estimated probability for each class.

```python
model.predict_proba(X_test)
```

Example:

```text
[0.10, 0.90]
```

This means:

```text
Probability of Class 0 = 0.10

Probability of Class 1 = 0.90
```

The probabilities sum to:

```text
0.10 + 0.90 = 1
```

---

## Getting Only Class 1 Probabilities

```python
class_1_probabilities = model.predict_proba(X_test)[:, 1]
```

Here:

```text
:
↓
Select all rows
```

```text
1
↓
Select the second column
```

The second column represents the probability of Class `1`.

---

## Inspecting Logistic Regression Weights

```python
print("Weights:", model.coef_)

print("Bias:", model.intercept_)
```

For multiple features:

```text
z = w₁x₁ + w₂x₂ + b
```

Example:

```text
z =
    Hours Weight × Hours
  + Attendance Weight × Attendance
  + Bias
```

The linear score `z` is passed through the Sigmoid Function.

```text
Features
   ↓
Weighted Linear Score
   ↓
Sigmoid
   ↓
Probability
   ↓
Class
```

---

# Quick Revision

```text
Classification
↓
Predicts Categories or Classes
```

```text
Binary Classification
↓
Two Classes
```

```text
Logistic Regression
↓
Calculates Linear Score z
↓
Applies Sigmoid
↓
Gets Probability
↓
Uses Decision Threshold
↓
Predicts Class
```

```text
Sigmoid
↓
Converts any real number into a value between 0 and 1
```

```text
Default Binary Threshold
↓
Probability >= 0.5 → Class 1
Probability < 0.5  → Class 0
```

```text
stratify=y
↓
Preserves approximately the same target class proportions during splitting
```

```text
predict()
↓
Predicted Class
```

```text
predict_proba()
↓
Estimated Class Probabilities
```

---

# Interview Questions

## 1. What is Classification?

Classification is a Machine Learning task used to predict a category or class.

## 2. What is Binary Classification?

Binary Classification is a classification problem with two possible target classes.

## 3. Why is Linear Regression not directly suitable for Binary Classification?

Linear Regression can produce values outside the range `0` to `1`, so its output cannot directly represent class probabilities.

## 4. What is the purpose of the Sigmoid Function?

The Sigmoid Function converts any real-valued linear score into a value between `0` and `1`.

## 5. What is a Decision Threshold?

A Decision Threshold converts a predicted probability into a class.

## 6. What does `stratify=y` do?

It preserves approximately the same target class distribution in the training and testing datasets.

## 7. What is the difference between `predict()` and `predict_proba()`?

`predict()` returns the predicted class, while `predict_proba()` returns the estimated probabilities for each class.
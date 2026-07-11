# Day 16 - Train-Test Split and Linear Regression Basics

## ML Feature Data Shape

When selecting features, even if we have only one feature, we usually write:

```python
students[["Hours"]]
```

instead of:

```python
students["Hours"]
```

### Why?

```python
students[["Hours"]]
```

returns a **DataFrame** with shape:

```text
(10, 1)
```

Where:

```text
10 → Number of samples
1  → Number of features
```

Machine Learning models generally expect feature data in the following form:

```text
(samples, features)
```

This is an important Machine Learning data-shape concept.

---

## Why Do We Split Data?

If we train and evaluate a model using the same complete dataset, the model may perform very well on the data it has already seen.

However, this does not tell us whether the model can perform well on new, unseen data.

We split the dataset into:

```text
Training Data
      ↓
Used to train the model

Testing Data
      ↓
Used to evaluate the model on unseen data
```

The main goal is to check the model's **generalization ability**.

---

## `train_test_split()`

Import:

```python
from sklearn.model_selection import train_test_split
```

Usage:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### `test_size=0.2`

This means:

```text
80% → Training Data
20% → Testing Data
```

We can check the shapes using:

```python
print("X Train Shape:", X_train.shape)
print("X Test Shape:", X_test.shape)

print("y Train Shape:", y_train.shape)
print("y Test Shape:", y_test.shape)
```

The number of samples must match:

```text
X_train rows = y_train values

X_test rows = y_test values
```

---

## Why Does `train_test_split()` Randomize Data?

Without randomization, the split may look like:

```text
First 80% → Training Data
Last 20%  → Testing Data
```

Suppose the dataset is ordered by study hours:

```text
1 hour
2 hours
3 hours
...
9 hours
10 hours
```

The training data may contain students studying from 1 to 8 hours.

The testing data may contain only students studying for 9 and 10 hours.

The model is then evaluated only on the highest-hour students.

This may produce a biased evaluation.

Therefore, Scikit-learn shuffles the samples before splitting by default.

---

## What is `random_state`?

`random_state` controls the random number generation used during the split.

Without `random_state`:

```python
train_test_split(X, y, test_size=0.2)
```

Different runs may produce different splits.

Example:

```text
Run 1 → Test: Students 2 and 9

Run 2 → Test: Students 4 and 7

Run 3 → Test: Students 1 and 10
```

This happens because the split is random.

By using:

```python
random_state=42
```

every run produces the same split.

This is called **reproducibility**.

The value `42` is not special.

We can also use:

```python
random_state=10
```

or:

```python
random_state=100
```

### Important

`random_state` does not inherently improve model performance.

It ensures reproducible random operations.

---

## Data Leakage

Data Leakage occurs when information that should not be available at prediction time, or information derived from the target, enters model training.

### Example

Suppose we want to predict student marks.

Features:

```text
Hours
Attendance
Final Result
```

Target:

```text
Marks
```

Imagine `Final Result` is calculated using `Marks`.

Now the model receives information derived from the answer itself.

This is Data Leakage.

The model may show:

```text
Accuracy = 99%
```

However, the model is not genuinely learning a useful pattern.

It has indirectly seen information about the target.

### Definition

> Data Leakage occurs when information unavailable at prediction time, or information derived from the target, enters model training.

---

## Importing the Linear Regression Model

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
```

Train the model:

```python
model.fit(X_train, y_train)
```

### What Does `fit()` Do?

We often say:

> `fit()` trains the model.

More specifically, for Linear Regression:

> `fit()` estimates the coefficients and intercept that minimize the residual sum of squares between actual and predicted target values on the training data.

---

## What is Linear Regression Trying to Learn?

The equation of a straight line is:

```text
y = mx + c
```

In Machine Learning, we commonly write:

```text
ŷ = wx + b
```

Where:

```text
x → Input Feature

w → Weight

b → Bias

ŷ → Predicted Value
```

### Important

```text
y → Actual Value

ŷ → Predicted Value
```

Linear Regression finds values for `w` and `b` such that its predictions are as close as possible to the actual values.

---

## Inspecting Learned Parameters

```python
print("Weight:", model.coef_)
print("Bias:", model.intercept_)
```

### `coef_`

Contains the learned weights or coefficients.

### `intercept_`

Contains the learned bias or intercept.

---

## Linear Regression With One Feature

For one feature:

```text
ŷ = w₁x₁ + b
```

Example:

```text
Predicted Salary = Weight × Experience + Bias
```

---

## Linear Regression With Multiple Features

For multiple features:

```text
ŷ = w₁x₁ + w₂x₂ + w₃x₃ + b
```

Example:

```text
Marks =
    w₁ × Hours
  + w₂ × Attendance
  + w₃ × Assignments
  + b
```

Each feature has its own weight.

---

## Measuring Prediction Error

Suppose:

```text
Actual Value    = 80
Predicted Value = 70
```

The error is:

```text
Error = Actual - Predicted

Error = 80 - 70

Error = 10
```

Mathematically:

```text
Error = y - ŷ
```

We need a way to measure the total prediction error across all training samples.

One common error metric is **Mean Squared Error (MSE)**.

```text
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

Where:

```text
yᵢ       → Actual Value

ŷᵢ       → Predicted Value

yᵢ - ŷᵢ → Prediction Error

(...)²   → Squared Error

Σ        → Sum of all squared errors

1/n      → Calculate the mean
```

The goal is:

```text
Find the best w and b
          ↓
Make the error as small as possible
```

This process is called **Optimization**.

---

## Linear Regression vs Gradient Descent

Linear Regression is a **model or mathematical problem**.

Gradient Descent is an **optimization algorithm**.

```text
Linear Regression
        ↓
Find a linear relationship between features and target

Gradient Descent
        ↓
An iterative method used to minimize a loss function
```

Gradient Descent can be used to optimize a Linear Regression objective.

### Important

> Linear Regression is not Gradient Descent.

Gradient Descent is one possible optimization method for training a Linear Regression model.

Scikit-learn's `LinearRegression` solves the Ordinary Least Squares problem using numerical linear algebra rather than teaching the model through a Gradient Descent loop.

---

## Prediction

After training the model:

```python
predictions = model.predict(X_test)
```

The model uses the learned equation:

```text
ŷ = wx + b
```

to calculate predictions for the test samples.

---

## Predicting a New Sample

Example:

```python
new_student = pd.DataFrame({
    "Hours": [7.5]
})

predicted_marks = model.predict(new_student)

print("Predicted Marks:", predicted_marks[0])
```

The new input should have the same feature structure used during model training.

---

## Visualizing the Learned Regression Line

```python
import matplotlib.pyplot as plt

plt.scatter(
    students["Hours"],
    students["Marks"]
)

plt.plot(
    students["Hours"],
    model.predict(students[["Hours"]])
)

plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")

plt.show()
```

### Scatter Points

The scatter points represent the **actual data**.

### Regression Line

The line represents the **relationship learned by the Linear Regression model**.

The model tries to find a line that minimizes the overall squared prediction errors.

---

# Quick Revision

```text
X → Features

y → Target

X_train → Features used for training

X_test → Features used for testing

y_train → Actual training targets

y_test → Actual testing targets
```

```text
test_size → Percentage of testing data

random_state → Reproducible random split

Data Leakage → Model indirectly receives forbidden or future information

fit() → Learns model parameters

coef_ → Learned weights

intercept_ → Learned bias

predict() → Makes predictions using learned parameters

MSE → Measures average squared prediction error

Optimization → Finding parameters that minimize the objective

Gradient Descent → An iterative optimization algorithm
```

---

# Interview Questions

## 1. Why do we split a dataset into training and testing data?
We split data to evaluate how well the model performs on unseen data and measure its generalization ability.

## 2. What does `random_state` do?

`random_state` ensures reproducibility by generating the same random split on every run.

## 3. Does `random_state=42` improve accuracy?

No. It only ensures reproducibility. The number `42` has no special Machine Learning property.

## 4. What is Data Leakage?

Data Leakage occurs when information unavailable at prediction time, or information derived from the target, is included during model training.

## 5. What does `fit()` do in Linear Regression?

It estimates the coefficients and intercept that minimize the residual sum of squares on the training data.

## 6. What is the difference between `y` and `ŷ`?

`y` represents the actual target value, while `ŷ` represents the predicted target value.

## 7. What is the difference between Linear Regression and Gradient Descent?

Linear Regression is a model that learns a linear relationship. Gradient Descent is an optimization algorithm that can be used to minimize a model's loss function.
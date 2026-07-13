# Day 17 - Multiple Linear Regression and Model Evaluation

## Simple Linear Regression

When we use a **single feature** to predict a target, it is called **Simple Linear Regression**.

Example:

```text
Experience → Salary
```

The equation is:

```text
ŷ = wx + b
```

Where:

- `x` → Input Feature
- `w` → Weight
- `b` → Bias
- `ŷ` → Predicted Value

---

## Multiple Linear Regression

In real-world Machine Learning problems, a target usually depends on multiple features.

When we use **multiple features** to predict a target, it is called **Multiple Linear Regression**.

Example:

```text
Experience ──┐
             │
Skill Score ─┼──> Salary
             │
Education ───┘
```

The equation is:

```text
ŷ = w₁x₁ + w₂x₂ + w₃x₃ + b
```

For multiple features:

- Each feature has its own weight.
- There are multiple weights.
- There is a single bias or intercept.

Example:

```text
Salary =
    w₁ × Experience
  + w₂ × SkillScore
  + b
```

---

## Why Does Every Feature Need Its Own Weight?

Every feature does not contribute equally to predicting the target.

Therefore, each feature has its own weight.

The weight represents how a feature contributes to the model's prediction.

Example:

```text
Experience Weight = 7000

Skill Score Weight = 500
```

An Experience weight of `7000` means:

> For a one-unit increase in Experience, the predicted Salary changes by approximately ₹7,000, while holding the other features constant.

### Important

The model learns the weights from the training data.

We do not manually assign the weights.

---

## Inspecting Weights

```python
print(model.coef_)
```

For multiple features:

```python
X = employees[["Experience", "SkillScore"]]
```

The order of weights follows the order of feature columns.

```text
model.coef_[0] → Experience Weight

model.coef_[1] → SkillScore Weight
```

A better way to display feature weights is:

```python
for feature, weight in zip(X.columns, model.coef_):
    print(feature, ":", weight)
```

---

# Regression Evaluation Metrics

Regression models are evaluated using metrics such as:

- MAE - Mean Absolute Error
- MSE - Mean Squared Error
- RMSE - Root Mean Squared Error
- R² Score

These metrics help us understand how well a regression model performs.

---

## MAE - Mean Absolute Error

MAE calculates the average absolute difference between the actual and predicted values.

Formula:

```text
MAE = (1/n) Σ |yᵢ - ŷᵢ|
```

Example errors:

```text
-5000
2000
7000
```

Absolute errors:

```text
5000
2000
7000
```

MAE calculates the average of these absolute errors.

### Interpretation

If:

```text
MAE = ₹4,000
```

It means:

> On average, the model's predictions are off by approximately ₹4,000.

### Python

```python
from sklearn.metrics import mean_absolute_error

mae = mean_absolute_error(y_test, predictions)
```

### When to Use MAE?

Use MAE when we want an **easily interpretable average prediction error**.

---

## MSE - Mean Squared Error

MSE calculates the average squared difference between actual and predicted values.

Formula:

```text
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

Example:

```text
Error = 2

Squared Error = 2² = 4
```

For a larger error:

```text
Error = 10

Squared Error = 10² = 100
```

Therefore, MSE gives a larger penalty to large prediction errors.

### Python

```python
from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, predictions)
```

### Limitation of MSE

If the target is measured in:

```text
Rupees
```

MSE is measured in:

```text
Rupees²
```

Therefore, MSE is not always easy to interpret directly.

---

## RMSE - Root Mean Squared Error

RMSE is the square root of MSE.

Formula:

```text
RMSE = √MSE
```

### Python

```python
import numpy as np

rmse = np.sqrt(mse)
```

RMSE returns the error to the same unit as the target variable.

Example:

```text
Target → Salary in Rupees

RMSE → Rupees
```

### When to Use RMSE?

Use RMSE when **large prediction errors should be penalized more strongly**.

RMSE is more sensitive to large errors and outliers than MAE.

---

## MAE vs RMSE

| MAE | RMSE |
|---|---|
| Uses absolute errors | Uses squared errors internally |
| Easy to interpret | Penalizes large errors more |
| Less sensitive to large errors | More sensitive to large errors |
| Gives average error magnitude | Highlights larger prediction mistakes |

### Remember

```text
MAE
↓
How far are predictions from actual values on average?

RMSE
↓
Measures error while giving more importance to large prediction mistakes.
```

Neither metric is always better.

The correct metric depends on the problem.

---

## R² Score

R² measures how well a regression model explains the variation in the target compared with simply predicting the mean target value.

The main question asked by R² is:

> How much better is my regression model at explaining target variation compared with just predicting the mean?

Formula:

```text
R² = 1 - (SSres / SStot)
```

Where:

```text
SSres → Model's remaining squared error

SStot → Squared error when predicting the target mean
```

---

## Understanding the R² Baseline

Suppose actual marks are:

```text
40
60
80
```

The mean is:

```text
60
```

A simple baseline model predicts:

```text
60
60
60
```

The baseline does not learn any pattern.

It simply predicts the mean target value for every sample.

R² compares our Machine Learning model with this mean baseline.

---

## Understanding R² Values

### R² = 1

```text
Perfect prediction on the evaluated data.
```

### R² = 0

```text
The model performs the same as predicting the mean target value.
```

### R² < 0

```text
The model performs worse than simply predicting the mean.
```

### Example

```text
R² = 0.95
```

This means:

> The model explains approximately 95% of the variation in the target variable.

### Important

R² is **not accuracy**.

Do not say:

```text
R² = 0.95 means 95% accuracy.
```

Instead say:

```text
The model explains approximately 95% of the variation in the target.
```

### Python

```python
from sklearn.metrics import r2_score

r2 = r2_score(y_test, predictions)
```

---

# Quick Revision

```text
Simple Linear Regression
↓
One Feature → One Weight
```

```text
Multiple Linear Regression
↓
Multiple Features → Multiple Weights
```

```text
MAE
↓
Average absolute prediction error
```

```text
MSE
↓
Average squared prediction error
```

```text
RMSE
↓
Square root of MSE
Penalizes large errors more strongly
```

```text
R²
↓
Compares the model with predicting the target mean
```

### R² Values

```text
R² = 1  → Perfect prediction

R² = 0  → Same as predicting mean

R² < 0  → Worse than predicting mean
```

---

# Interview Questions

## 1. What is Multiple Linear Regression?

Multiple Linear Regression is used when multiple input features are used to predict a continuous target variable.

## 2. Why does every feature have a separate weight?

Each feature may contribute differently to the target prediction. Therefore, the model learns a separate weight for each feature.

## 3. What does a Linear Regression coefficient represent?

A coefficient represents the expected change in the predicted target for a one-unit increase in a feature, while holding other features constant.

## 4. What is MAE?

MAE is the average absolute difference between actual and predicted values.

## 5. Why is RMSE more sensitive to large errors than MAE?

RMSE uses squared errors internally. Therefore, large errors receive a much larger penalty.

## 6. What does R² measure?

R² measures how well a regression model explains the variation in the target compared with predicting the mean target value.

## 7. Can R² be negative?

Yes. A negative R² means the model performs worse than simply predicting the mean target value.

## 8. Is R² the accuracy of a regression model?

No. R² measures explained variation and is not classification accuracy.
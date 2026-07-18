# Day 22 - Decision Trees

## What is a Decision Tree?

A Decision Tree is a **Supervised Machine Learning algorithm**.

It can be used for:

- Classification
- Regression

Unlike Linear Regression (equations) or KNN (distance), a Decision Tree makes predictions by asking a sequence of **if-else questions**.

Example:

```text
Is Hours Studied > 5?

      Yes
      ↓
    Pass

      No
      ↓
Study More
```

A Decision Tree continues asking questions until it reaches a final prediction.

---

# Real-Life Analogy

Suppose you are deciding whether to carry an umbrella.

```text
Is it raining?

      Yes
      ↓
Take Umbrella

      No
      ↓
Is it cloudy?

      Yes
      ↓
Maybe Carry It

      No
      ↓
Don't Carry
```

This is exactly how a Decision Tree works.

---

# Tree Structure

A Decision Tree consists of three main parts.

```text
          Root Node
              │
      ┌───────┴───────┐
      │               │
 Decision Node   Decision Node
      │               │
   Leaf Node      Leaf Node
```

---

# Root Node

The Root Node is the first question asked by the tree.

Example:

```text
Attendance > 75?
```

The tree chooses the question that best separates the classes.

---

# Decision Node

A Decision Node is an internal node that asks another question.

Example:

```text
Attendance > 75?

      Yes
      ↓
Hours > 5?
```

---

# Leaf Node

A Leaf Node contains the final prediction.

Example:

```text
Attendance > 75?

      Yes
      ↓
Hours > 5?

      Yes
      ↓
Pass
```

Once a Leaf Node is reached, prediction stops.

---

# How Does a Decision Tree Choose the Best Split?

A Decision Tree has many possible questions.

Example:

```text
Hours > 4?

Hours > 5?

Hours > 6?

Attendance > 70?

Attendance > 80?
```

The algorithm selects the question that produces the **purest groups**.

To measure purity, Decision Trees use:

- Entropy
- Information Gain
- Gini Index

---

# Entropy

Entropy measures the amount of **impurity (disorder)** in a dataset.

### Pure Dataset

```text
⚪ ⚪ ⚪ ⚪ ⚪
```

All samples belong to the same class.

```text
Entropy = 0
```

---

### Mixed Dataset

```text
⚪ ⚫ ⚪ ⚫ ⚪ ⚫
```

Classes are mixed.

Entropy is high.

---

### Interpretation

```text
Entropy = 0
↓

Perfectly Pure Dataset
```

```text
Higher Entropy
↓

More Mixed Classes
```

---

# Entropy Formula

For Binary Classification:

```text
Entropy = -p₁ log₂(p₁) - p₂ log₂(p₂)
```

Where:

```text
p₁ = Probability of Class 1

p₂ = Probability of Class 0
```

### Important

You do **not** need to memorize the formula.

Just remember:

```text
More Mixed Classes
↓

Higher Entropy
```

---

# Information Gain

Information Gain measures how much impurity decreases after splitting the data.

Formula:

```text
Information Gain

=

Parent Entropy

-

Weighted Child Entropy
```

Higher Information Gain means a better split.

---

## Example

Before Split:

```text
10 Students

5 Pass

5 Fail
```

Mixed classes.

Entropy is high.

Split using:

```text
Attendance > 80
```

After Split:

Left:

```text
5 Pass
```

Right:

```text
5 Fail
```

Both groups become pure.

Entropy decreases.

Information Gain becomes high.

---

# Gini Index

Another measure of impurity used by Decision Trees.

Formula:

```text
Gini = 1 − Σ(pi²)
```

Where:

```text
pi = Probability of each class
```

Interpretation:

```text
Gini = 0
↓

Pure Node
```

Higher Gini means higher impurity.

---

# Entropy vs Gini

| Entropy | Gini Index |
|----------|------------|
| Measures impurity | Measures impurity |
| Uses logarithms | Simpler mathematical calculation |
| Slightly slower | Slightly faster |
| Used with `criterion="entropy"` | Default in Scikit-learn |

Example:

```python
DecisionTreeClassifier(
    criterion="entropy"
)
```

Default:

```python
DecisionTreeClassifier()
```

uses **Gini Index**.

---

# When Does the Tree Stop Growing?

A Decision Tree does not grow forever.

Common stopping conditions:

- Maximum depth reached
- Minimum samples required for splitting
- Node becomes pure
- No useful split remains

---

# Overfitting

A very deep Decision Tree may memorize the training data.

Example:

```text
Training Accuracy = 100%

Testing Accuracy = 70%
```

The model performs extremely well on training data but poorly on unseen data.

This is called **Overfitting**.

---

# Reducing Overfitting

Common techniques:

- Limit `max_depth`
- Increase `min_samples_split`
- Increase `min_samples_leaf`
- Pruning (removing unnecessary branches)

---

# Training Accuracy vs Testing Accuracy

### Training Accuracy

Measures how well the model performs on the training data.

Formula:

```text
Training Accuracy

=

Correct Predictions on Training Data

/

Total Training Samples
```

---

### Testing Accuracy

Measures how well the model performs on unseen data.

Formula:

```text
Testing Accuracy

=

Correct Predictions on Testing Data

/

Total Testing Samples
```

---

### Interpretation

#### Good Model

```text
Training Accuracy = 95%

Testing Accuracy = 93%
```

The model generalizes well.

---

#### Overfitting

```text
Training Accuracy = 100%

Testing Accuracy = 72%
```

The model memorizes the training data.

---

#### Underfitting

```text
Training Accuracy = 65%

Testing Accuracy = 60%
```

The model is too simple to learn the underlying patterns.

---

# Feature Importance

Decision Trees can estimate how useful each feature was while creating the tree.

Example:

```text
Hours Studied

0.72
```

```text
Attendance

0.28
```

A larger value means the feature contributed more to the decision-making process.

Scikit-Learn:

```python
print(model.feature_importances_)
```

---

# Scikit-Learn Implementation

## Import

```python
from sklearn.tree import DecisionTreeClassifier
```

## Create Model

```python
model = DecisionTreeClassifier(
    random_state=42
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

## Evaluate

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

# Compare Different Tree Depths

```python
model1 = DecisionTreeClassifier(
    max_depth=1,
    random_state=42
)

model2 = DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)
```

Training Accuracy:

```python
print(model.score(X_train, y_train))
```

Testing Accuracy:

```python
print(model.score(X_test, y_test))
```

---

# Advantages

- Easy to understand
- Easy to visualize
- No Feature Scaling required
- Works for Classification and Regression
- Provides Feature Importance

---

# Disadvantages

- Can easily overfit
- Sensitive to small changes in data
- Deep trees may generalize poorly

---

# Quick Revision

```text
Decision Tree
↓

Supervised Learning
```

```text
Works For
↓

Classification
Regression
```

```text
Tree Structure
↓

Root Node
↓

Decision Node
↓

Leaf Node
```

```text
Entropy
↓

Measures Impurity
```

```text
Information Gain
↓

Chooses the Best Split
```

```text
Gini Index
↓

Default Criterion in Scikit-Learn
```

```text
Deep Tree
↓

Overfitting
```

```text
Limit max_depth
↓

Reduce Overfitting
```

```text
Feature Importance
↓

Shows the Contribution of Each Feature
```

---

# Interview Questions

## 1. What is a Decision Tree?

A Decision Tree is a supervised Machine Learning algorithm that predicts outcomes by asking a sequence of if-else questions.

---

## 2. What are the three main parts of a Decision Tree?

- Root Node
- Decision Node
- Leaf Node

---

## 3. What is Entropy?

Entropy is a measure of impurity or disorder in a dataset.

Lower Entropy indicates purer data.

---

## 4. What is Information Gain?

Information Gain measures the reduction in impurity after splitting the data.

The split with the highest Information Gain is preferred.

---

## 5. What is the Gini Index?

The Gini Index measures impurity and is the default splitting criterion used in Scikit-Learn's `DecisionTreeClassifier`.

---

## 6. What is Overfitting?

Overfitting occurs when a Decision Tree becomes too deep and memorizes the training data, leading to poor performance on unseen data.

---

## 7. How can Overfitting be reduced?

- Limit `max_depth`
- Increase `min_samples_split`
- Increase `min_samples_leaf`
- Use pruning

---

## 8. Does a Decision Tree require Feature Scaling?

No. Decision Trees are not distance-based algorithms, so Feature Scaling is generally not required.

---

## 9. What is Feature Importance?

Feature Importance indicates how much each feature contributed to building the Decision Tree.

---

## 10. Why can increasing `max_depth` improve training accuracy but reduce testing accuracy?

A deeper tree can memorize the training data, increasing Training Accuracy. However, it may fail to generalize to new data, reducing Testing Accuracy due to overfitting.
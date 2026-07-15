# Day 19 - Classification Evaluation and Threshold Analysis

## Confusion Matrix

A Confusion Matrix compares:

```text
Actual Class
     VS
Predicted Class
```

For Binary Classification, there are four possible results:

| Actual | Predicted | Result |
| ------ | --------- | ------ |
| 1 | 1 | True Positive |
| 0 | 0 | True Negative |
| 0 | 1 | False Positive |
| 1 | 0 | False Negative |

### True Positive (TP)

The model correctly predicted the positive class.

```text
Actual = Positive
Predicted = Positive
```

### True Negative (TN)

The model correctly predicted the negative class.

```text
Actual = Negative
Predicted = Negative
```

### False Positive (FP)

The model incorrectly predicted the negative class as the positive class.

```text
Actual = Negative
Predicted = Positive
```

### False Negative (FN)

The model incorrectly predicted the positive class as the negative class.

```text
Actual = Positive
Predicted = Negative
```

### Easy Way to Remember

```text
True / False
↓
Was the prediction correct or wrong?

Positive / Negative
↓
What class did the model predict?
```

---

# Accuracy

Accuracy asks:

> Out of all predictions, how many were correct?

Formula:

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

Correct predictions:

```text
TP + TN
```

Total predictions:

```text
TP + TN + FP + FN
```

### Important

High Accuracy does not always mean a good Classification model.

Example:

```text
100 Patients

95 → No PCOS
5  → PCOS
```

Suppose the model predicts:

```text
No PCOS for everyone
```

The model gets:

```text
95% Accuracy
```

But it identifies:

```text
0 PCOS Patients
```

Therefore, Accuracy can be misleading for imbalanced datasets.

---

# Precision

Precision asks:

> Out of all samples predicted as Positive, how many were actually Positive?

Formula:

```text
Precision = TP / (TP + FP)
```

The denominator:

```text
TP + FP
```

represents all **Predicted Positive samples**.

### Important

Precision focuses on:

```text
Predicted Positives
```

Precision is important when **False Positives are costly**.

```text
More False Positives
        ↓
Lower Precision
```

---

# Recall

Recall asks:

> Out of all actual Positive samples, how many did the model correctly identify?

Formula:

```text
Recall = TP / (TP + FN)
```

The denominator:

```text
TP + FN
```

represents all **Actual Positive samples**.

High Recall means the model finds a high proportion of actual Positive cases.

```text
More False Negatives
        ↓
Lower Recall
```

### Precision vs Recall

```text
Precision
↓
Focuses on Predicted Positives
```

```text
Recall
↓
Focuses on Actual Positives
```

### Easy Way to Remember

```text
Precision → FP Problem

Recall → FN Problem
```

---

# Can We Have High Precision and Low Recall?

Yes, it is possible.

The model may be very careful before predicting the Positive class.

```text
Few Positive Predictions
        ↓
Most Positive Predictions are Correct
        ↓
High Precision
```

But the model may miss many actual Positive samples.

```text
More False Negatives
        ↓
Low Recall
```

---

# Can We Have High Recall and Low Precision?

Yes, it is possible.

The model may predict many samples as Positive.

```text
More Positive Predictions
        ↓
Finds Most Actual Positives
        ↓
High Recall
```

But it may also incorrectly predict many Negative samples as Positive.

```text
More False Positives
        ↓
Low Precision
```

This relationship is called the **Precision-Recall Trade-off**.

---

# F1 Score

F1 Score considers both Precision and Recall.

It uses the **Harmonic Mean** of Precision and Recall.

Formula:

```text
F1 = (2 × Precision × Recall) / (Precision + Recall)
```

F1 Score becomes high when both Precision and Recall are reasonably high.

Example:

```text
Precision = 1.0
Recall = 0.1
```

Even though Precision is very high, Recall is poor.

Therefore, the F1 Score will also be relatively low.

### When to Use F1 Score?

Use F1 Score when we need a balance between:

```text
Precision
    +
Recall
```

It is especially useful when class imbalance makes Accuracy less informative.

---

# Classification Report

Instead of calculating every metric separately, we can use:

```python
from sklearn.metrics import classification_report

print(
    classification_report(
        y_test,
        predictions
    )
)
```

The Classification Report displays:

```text
Precision
Recall
F1 Score
Support
```

## What is Support?

Support means:

> The number of actual samples belonging to a particular class.

Example:

```text
Class 0 Support = 20
```

This means:

```text
20 actual Class 0 samples exist in the evaluated data.
```

---

# Decision Threshold

Logistic Regression produces estimated class probabilities.

A decision threshold converts the probability into a class.

The common default binary threshold is:

```text
0.5
```

Decision rule:

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

However:

> 0.5 is not a universal Machine Learning law.

The threshold can be changed depending on the problem and the cost of different errors.

---

# Precision-Recall Trade-off and Threshold

| Threshold | Positive Predictions | Typical Effect |
| --------- | -------------------- | -------------- |
| Lower | More | Recall tends to increase |
| Higher | Fewer | Precision may increase |

## Lower Threshold

```text
Threshold ↓
     ↓
More Positive Predictions
     ↓
False Negatives may decrease
     ↓
Recall may increase
```

But:

```text
More Positive Predictions
     ↓
False Positives may increase
     ↓
Precision may decrease
```

## Higher Threshold

```text
Threshold ↑
     ↓
Fewer Positive Predictions
     ↓
False Positives may decrease
     ↓
Precision may increase
```

But:

```text
Fewer Positive Predictions
     ↓
False Negatives may increase
     ↓
Recall may decrease
```

These are typical effects. The exact metric changes depend on the dataset and model scores.

---

# Manually Apply a Decision Threshold

Get the probability of Class `1`:

```python
probabilities = model.predict_proba(X_test)[:, 1]
```

Apply a threshold of `0.5`:

```python
predictions_05 = (
    probabilities >= 0.5
).astype(int)
```

Apply a threshold of `0.3`:

```python
predictions_03 = (
    probabilities >= 0.3
).astype(int)
```

Example:

```text
Probabilities:

[0.91, 0.72, 0.48, 0.35, 0.12]
```

For threshold `0.5`:

```text
[1, 1, 0, 0, 0]
```

For threshold `0.3`:

```text
[1, 1, 1, 1, 0]
```

### How Does `.astype(int)` Work?

The comparison:

```python
probabilities >= 0.5
```

produces:

```text
True
False
```

Then:

```python
.astype(int)
```

converts:

```text
True  → 1
False → 0
```

---

# Why Do We Need ROC?

We can manually test different thresholds:

```text
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
```

But we need a way to examine model discrimination across many thresholds.

One important tool is the **ROC Curve**.

---

# ROC - Receiver Operating Characteristic

The ROC Curve plots:

```text
x-axis → False Positive Rate (FPR)

y-axis → True Positive Rate (TPR)
```

True Positive Rate is also known as:

```text
Recall
```

Formula:

```text
TPR = TP / (TP + FN)
```

---

# False Positive Rate - FPR

FPR asks:

> Out of all actual Negative samples, how many did we incorrectly predict as Positive?

Formula:

```text
FPR = FP / (FP + TN)
```

The denominator:

```text
FP + TN
```

represents all **Actual Negative samples**.

Example:

```text
100 Actual Negative Samples

20 → Incorrectly Predicted Positive
80 → Correctly Predicted Negative
```

Therefore:

```text
FP = 20
TN = 80
```

FPR:

```text
FPR = 20 / (20 + 80)

FPR = 0.2
```

So:

```text
FPR = 20%
```

---

# How Does the ROC Curve Work?

The ROC Curve evaluates the classifier across different decision thresholds.

Conceptually:

```text
Threshold = 1.0
Threshold = 0.9
Threshold = 0.8
Threshold = 0.7
...
Threshold = 0.1
Threshold = 0.0
```

At different thresholds:

```text
Predictions Change
        ↓
TP, TN, FP and FN Change
        ↓
TPR and FPR Change
        ↓
Plot FPR vs TPR
        ↓
ROC Curve
```

Therefore:

> The ROC Curve shows the classifier's trade-off between detecting Positive cases and producing False Positive alarms across different thresholds.

---

# ROC Curve in Python

First get Class `1` probabilities:

```python
probabilities = model.predict_proba(X_test)[:, 1]
```

Calculate ROC values:

```python
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(
    y_test,
    probabilities
)
```

Plot the ROC Curve:

```python
import matplotlib.pyplot as plt

plt.plot(fpr, tpr)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.show()
```

### Why Does ROC Use Probabilities Instead of Final Predictions?

ROC evaluates the classifier across **multiple decision thresholds**.

Probabilities contain the model's score information.

Final predictions contain only:

```text
0 or 1
```

Therefore, final predictions have already discarded much of the ranking information needed for ROC analysis.

---

# Understanding a Good ROC Curve

The ideal ROC point is:

```text
FPR = 0
TPR = 1
```

Meaning:

```text
No False Positive Alarms
        +
All Positive Cases Detected
```

This is the top-left region of the ROC graph.

Therefore:

> The closer the ROC Curve bends toward the top-left, the stronger the classifier's ranking or discrimination performance.

A random classifier approximately follows the diagonal.

```text
TPR ≈ FPR
```

---

# AUC Score - Area Under the Curve

AUC means:

```text
Area Under the ROC Curve
```

It summarizes ROC Curve performance into a single number.

The score generally ranges from:

```text
0 to 1
```

### AUC = 1.0

```text
Perfect ranking separation on the evaluated data.
```

### AUC = 0.5

```text
No better than random ranking.
```

### AUC < 0.5

```text
Ranking is worse than random orientation.
```

---

# Understanding AUC

Suppose we randomly select:

```text
One Actual Positive Sample
```

and:

```text
One Actual Negative Sample
```

The model produces:

```text
Positive Sample Score = 0.85

Negative Sample Score = 0.30
```

The model correctly gives a higher Positive-class score to the actual Positive sample.

A useful interpretation of ROC-AUC is:

> AUC measures the probability that a randomly selected Positive sample receives a higher model score than a randomly selected Negative sample.

Example:

```text
AUC = 0.90
```

This means the model has approximately a `90%` chance of ranking a randomly selected Positive sample above a randomly selected Negative sample.

### Important

```text
AUC = 0.90
```

does **not** mean:

```text
90% Accuracy
```

AUC measures ranking or discrimination ability.

---

# Calculate ROC-AUC

```python
from sklearn.metrics import roc_auc_score

auc = roc_auc_score(
    y_test,
    probabilities
)

print("ROC-AUC:", auc)
```

We use:

```text
Probabilities / Scores
```

instead of final class predictions because ROC-AUC evaluates ranking performance across decision thresholds.

---

# Class Imbalance

Class Imbalance occurs when one class contains significantly more samples than another class.

Example:

```text
1000 Transactions

990 → Normal
10  → Fraud
```

Class distribution:

```text
99% → Class 0

1% → Class 1
```

A model that predicts:

```text
Normal
```

for every transaction gets:

```text
99% Accuracy
```

But:

```text
Fraud Detected = 0
```

Therefore, Accuracy alone is not enough for highly imbalanced classification problems.

We should also examine:

```text
Confusion Matrix
Precision
Recall
F1 Score
ROC-AUC
```

For rare Positive classes, Precision-Recall analysis can also be especially useful.

---

# `class_weight="balanced"`

We can create Logistic Regression using:

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(
    class_weight="balanced"
)
```

Suppose:

```text
Class 0 → 900 Samples

Class 1 → 100 Samples
```

Scikit-learn automatically gives:

```text
Majority Class
↓
Smaller Relative Weight Per Sample
```

```text
Minority Class
↓
Larger Relative Weight Per Sample
```

It uses inverse class-frequency weighting.

The goal is to make mistakes on the minority class matter more during model training.

---

# `class_weight="balanced"` vs SMOTE

## class_weight="balanced"

```text
Dataset Remains the Same
        ↓
No New Samples Created
        ↓
Classes Receive Different Training Weights
```

## SMOTE

```text
Minority Class
        ↓
Creates Synthetic Minority Samples
        ↓
Changes the Training Dataset
```

### Main Difference

```text
class_weight
↓
Changes the importance of class errors during training
```

```text
SMOTE
↓
Changes the training data distribution by creating synthetic minority samples
```

---

# Quick Revision

```text
Confusion Matrix
↓
Actual vs Predicted
```

```text
Accuracy
↓
How many total predictions were correct?
```

```text
Precision
↓
Of all Predicted Positives,
how many were actually Positive?
```

```text
Recall
↓
Of all Actual Positives,
how many did the model identify?
```

```text
F1 Score
↓
Balances Precision and Recall
```

```text
Lower Threshold
↓
More Positive Predictions
↓
Recall tends to increase
```

```text
Higher Threshold
↓
Fewer Positive Predictions
↓
Precision may increase
```

```text
ROC Curve
↓
TPR vs FPR across thresholds
```

```text
ROC-AUC
↓
Measures ranking or discrimination ability
```

```text
class_weight="balanced"
↓
Gives relatively more training importance to minority-class samples
```

---

# Interview Questions

## 1. What is the difference between Precision and Recall?

Precision focuses on Predicted Positive samples, while Recall focuses on Actual Positive samples.

## 2. Why can Accuracy be misleading?

Accuracy can be misleading when the dataset is imbalanced because a model may predict only the majority class and still achieve high Accuracy.

## 3. What happens when we decrease the decision threshold?

The model predicts more samples as Positive. Recall tends to increase, but Precision may decrease.

## 4. Why does the ROC Curve use probabilities?

ROC evaluates the classifier across multiple thresholds. Probabilities or model scores contain the ranking information required to test different thresholds.

## 5. What does AUC = 0.90 mean?

It means the model has approximately a 90% probability of ranking a randomly selected Positive sample above a randomly selected Negative sample.

It does not mean 90% Accuracy.

## 6. What is the difference between class weighting and SMOTE?

Class weighting changes the importance of class errors during training, while SMOTE creates synthetic minority-class samples and changes the training dataset.
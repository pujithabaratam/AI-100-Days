# AI-100 Days – Day 23
# 🌲 Random Forest

# 🌳 Why is a Single Decision Tree Not Enough?

A Decision Tree is one of the simplest Machine Learning algorithms.

It works by repeatedly asking questions and splitting the data until a prediction is made.

Although Decision Trees are easy to understand, they have some important limitations.

## Problems with Decision Trees

### 1. Overfitting

Decision Trees can easily memorize the training data instead of learning general patterns.

Example:

Training Accuracy = 100%

Testing Accuracy = 75%

The model performs well on training data but poorly on unseen data.

This is called **Overfitting**.

---

### 2. High Variance

A very small change in the dataset can create an entirely different Decision Tree.

Example:

Dataset A

↓

Tree A

Dataset B (only one row changed)

↓

Tree B

This makes Decision Trees unstable.

---

### Real-Life Analogy

Imagine asking only one doctor for a diagnosis.

If the doctor makes a mistake, the final answer is wrong.

Instead, ask 100 doctors.

Take the majority opinion.

The result is usually much more reliable.

This is exactly how Random Forest works.

---

# 🤝 Ensemble Learning

## Definition

Ensemble Learning is a Machine Learning technique where multiple models are combined to produce better predictions.

Instead of relying on one model,

we combine several models.

```
One Weak Model
       ❌

Many Models
       ↓
Combined Prediction
       ✅
```

The idea is that a group of models usually performs better than a single model.

---

## Types of Ensemble Learning

### 1. Bagging

- Models are trained independently.
- Predictions are combined.

Example:

- Random Forest

---

### 2. Boosting

- Models are trained one after another.
- Each new model corrects previous mistakes.

Examples:

- AdaBoost
- Gradient Boosting
- XGBoost

---

# 📦 Bootstrap Sampling

Random Forest does **not** train every tree using the same dataset.

Instead, it creates multiple datasets.

This process is called **Bootstrap Sampling**.

## Definition

Bootstrap Sampling is **random sampling with replacement**.

"With replacement" means the same sample can appear multiple times.

---

Original Dataset

```
A
B
C
D
E
```

Bootstrap Sample 1

```
A
C
C
E
D
```

Notice:

- C appears twice.
- B is missing.

Both are completely normal.

---

Bootstrap Sample 2

```
B
B
A
D
E
```

Every Decision Tree receives a different bootstrap sample.

---

## Advantages

- Reduces overfitting
- Increases diversity among trees
- Improves generalization

---

# 🗳️ Bagging (Bootstrap Aggregating)

Bagging = Bootstrap + Aggregation

## Steps

```
Original Dataset
        ↓
Bootstrap Samples
        ↓
Train Multiple Trees
        ↓
Combine Predictions
        ↓
Final Prediction
```

---

### Diagram

```
Original Data

      |

Bootstrap Samples

 /    |    \

Tree1 Tree2 Tree3

 \     |     /

 Final Prediction
```

---

## Advantages

- Reduces variance
- Stable predictions
- Better accuracy
- Less overfitting

---

# 🌲 What is Random Forest?

## Definition

Random Forest is an ensemble learning algorithm that builds many Decision Trees and combines their predictions.

Instead of one tree,

we create

- 100 Trees
- 200 Trees
- 500 Trees

Each tree is different.

The final prediction comes from combining all trees.

---

## Formula

```
Random Forest

=

Many Decision Trees

+

Bagging

+

Random Feature Selection
```

---

## Example

Tree 1

Predicts

Cat

Tree 2

Predicts

Dog

Tree 3

Predicts

Cat

Tree 4

Predicts

Cat

Tree 5

Predicts

Dog

Majority Vote

↓

Cat

---

# 🎲 Random Feature Selection

Another reason Random Forest performs well is that every tree uses only a subset of features while splitting.

Suppose our dataset has:

- Age
- Salary
- Experience
- City
- Gender
- Education
- Credit Score

Decision Tree

Uses every feature.

Random Forest

Each split randomly selects only a few features.

Example

Tree 1

```
Age
Salary
Gender
```

Tree 2

```
Education
Experience
City
```

Tree 3

```
Credit Score
Age
Salary
```

Because each tree uses different features,

the trees become more diverse.

---

## Why is this useful?

Without random feature selection,

every tree might become almost identical.

Random feature selection increases diversity,

which improves performance.

---

# 🗳️ Voting Mechanism (Classification)

For classification,

every tree predicts a class.

Example

Tree 1 → Dog

Tree 2 → Dog

Tree 3 → Cat

Tree 4 → Dog

Tree 5 → Cat

Votes

```
Dog = 3

Cat = 2
```

Final Prediction

```
Dog
```

This is called

**Majority Voting**.

---

# 📊 Averaging (Regression)

Regression predicts numerical values.

Example

House Price

Tree Predictions

```
40 Lakhs

42 Lakhs

39 Lakhs

41 Lakhs

43 Lakhs
```

Average

```
41 Lakhs
```

Final Prediction

```
41 Lakhs
```

---

# 🌟 Out-of-Bag (OOB) Score

Bootstrap Sampling leaves out some training samples.

Those unused samples are called

**Out-of-Bag (OOB) Samples.**

Example

Original Data

```
A B C D E
```

Bootstrap Sample

```
A C C D E
```

Unused Sample

```
B
```

B becomes the OOB sample.

---

## Why is OOB Score useful?

Trees that never saw sample B during training can predict it.

These predictions estimate model performance.

This allows Random Forest to evaluate itself without needing a separate validation set.

---

## Advantages

- No validation dataset required
- Saves time
- Reliable performance estimate

---

# ⚙️ Scikit-learn Implementation

## Classification

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## Regression

```python
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

X, y = fetch_california_housing(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

rmse = mean_squared_error(y_test, y_pred) ** 0.5

print("RMSE:", rmse)
```

---

## Important Parameters

```python
RandomForestClassifier(
    n_estimators=100,
    max_depth=None,
    max_features="sqrt",
    min_samples_split=2,
    min_samples_leaf=1,
    bootstrap=True,
    oob_score=False,
    random_state=42
)
```

| Parameter | Description |
|------------|-------------|
| n_estimators | Number of trees |
| max_depth | Maximum depth of each tree |
| max_features | Number of features considered at each split |
| min_samples_split | Minimum samples required to split a node |
| min_samples_leaf | Minimum samples required in a leaf |
| bootstrap | Enables bootstrap sampling |
| oob_score | Computes Out-of-Bag score |
| random_state | Ensures reproducible results |

---

# 📈 Feature Importance

Random Forest tells us which features are most useful.

Example

```
Salary         0.30
Credit Score   0.27
Experience     0.18
Age            0.14
City           0.06
Gender         0.05
```

Higher importance means the feature contributes more to making good predictions.

---

Python Example

```python
import pandas as pd

importance = pd.Series(
    model.feature_importances_,
    index=[
        "Age",
        "Salary",
        "Experience",
        "Credit Score"
    ]
)

print(importance.sort_values(ascending=False))
```

---

Applications

- Feature Selection
- Model Interpretation
- Understanding important variables

---

# 🌳 Decision Tree vs Random Forest

| Feature | Decision Tree | Random Forest |
|----------|--------------|---------------|
| Number of Trees | One | Many |
| Accuracy | Lower | Higher |
| Overfitting | High | Low |
| Variance | High | Low |
| Stability | Low | High |
| Training Speed | Faster | Slower |
| Prediction Speed | Faster | Slightly Slower |
| Feature Selection | All Features | Random Subset |
| Robustness | Lower | Higher |

---

# 🎯 Advantages of Random Forest

- High Accuracy
- Reduces Overfitting
- Handles Large Datasets
- Works for Classification and Regression
- Robust to Noise
- Provides Feature Importance
- Handles Missing Values Better
- Less Sensitive to Outliers

---

# ❌ Disadvantages

- Slower than Decision Trees
- Higher Memory Usage
- Less Interpretable
- Large models consume more storage

---

# 💡 When Should You Use Random Forest?

Use Random Forest when:

- High prediction accuracy is required.
- Dataset contains many features.
- Overfitting is a concern.
- Feature importance is needed.
- A strong baseline model is desired.

Avoid Random Forest when:

- Model interpretability is essential.
- Prediction latency must be extremely low.
- Memory resources are limited.

---

# 📝 Summary

Today we learned:

- Why a single Decision Tree is not enough
- Ensemble Learning
- Bootstrap Sampling
- Bagging
- Random Forest
- Random Feature Selection
- Majority Voting
- Averaging
- Out-of-Bag Score
- Scikit-learn Implementation
- Feature Importance
- Decision Tree vs Random Forest

Random Forest is one of the most powerful and widely used Machine Learning algorithms because it combines multiple Decision Trees to produce accurate, stable, and robust predictions.

---

# 🧠 Interview Questions

### 1. Why is Random Forest better than a Decision Tree?

Because it combines multiple Decision Trees, reducing overfitting and improving accuracy.

---

### 2. What is Bootstrap Sampling?

Random sampling with replacement.

---

### 3. What is Bagging?

Training multiple models on different bootstrap samples and combining their predictions.

---

### 4. Why is it called Random Forest?

Because each tree uses both random training samples and random feature subsets.

---

### 5. How does Random Forest perform classification?

Using Majority Voting.

---

### 6. How does Random Forest perform regression?

Using Averaging.

---

### 7. What is the OOB Score?

An internal validation score calculated using samples that were not used to train a particular tree.

---

### 8. What is Feature Importance?

A measure of how much each feature contributes to the model's predictions.

---


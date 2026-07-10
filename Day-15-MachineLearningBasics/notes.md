# Day 15 - Machine Learning Basics

## What is Artificial Intelligence (AI)?

Artificial Intelligence (AI) is the ability of a machine to perform tasks that normally require human intelligence.

### Examples

- ChatGPT
- Siri
- Google Translate
- Self-driving Cars
- Face Recognition

---

# What is Machine Learning (ML)?

Machine Learning is a subset of Artificial Intelligence.

Instead of writing rules manually, we provide the computer with data. The machine learns patterns from the data and makes predictions.

---

# What is Deep Learning (DL)?

Deep Learning is a subset of Machine Learning.

It uses **Artificial Neural Networks (ANNs)** to solve complex problems.

### Examples

- Image Recognition
- Speech Recognition
- ChatGPT
- Medical Diagnosis

---

# Relationship Between AI, ML, and DL

```text
Artificial Intelligence
        │
        ▼
Machine Learning
        │
        ▼
Deep Learning
```

---

# Types of Machine Learning

## 1. Supervised Learning

In Supervised Learning, we have:

- Input (Features)
- Correct Output (Target)

The model learns the relationship between features and target.

### Examples

- House Price Prediction
- PCOS Prediction
- Spam Detection

---

## 2. Unsupervised Learning

In Unsupervised Learning, we only have input data.

There are no target values.

The model discovers hidden patterns or groups in the data.

### Example

- Customer Segmentation in an online shopping website

---

## 3. Reinforcement Learning

The model learns through **Rewards** and **Punishments**.

### Examples

- Chess AI
- Robots
- Self-driving Cars

---

# Features vs Target

This is one of the most important concepts in Machine Learning.

Example:

| Hours | Attendance | Marks |
|------:|-----------:|------:|
| 2 | 80 | 40 |
| 5 | 90 | 70 |
| 8 | 95 | 95 |

### Features

- Hours
- Attendance

### Target

- Marks

The model uses the **Features** to predict the **Target**.

---

# Machine Learning Workflow

```text
Collect Data
      │
      ▼
Load Dataset
      │
      ▼
Clean Data
      │
      ▼
Explore Data (EDA)
      │
      ▼
Select Features
      │
      ▼
Split Train/Test Data
      │
      ▼
Train Model
      │
      ▼
Evaluate Model
      │
      ▼
Predict
```

---

# Training Data vs Testing Data

Suppose we have **100 students**.

- 80 Students → Training Data
- 20 Students → Testing Data

The model learns using the **training data**.

The **testing data** is used to evaluate how well the model performs on unseen data.

---

# What is an Instance (Sample)?

Every row in a dataset is called an **Instance** or **Sample**.

Example:

| Hours | Attendance | Marks |
|------:|-----------:|------:|
| 2 | 80 | 40 | ← Sample 1

---

# What is a Feature Vector?

A **Feature Vector** is the collection of all feature values for a single sample.

Example:

```
Hours = 6
Attendance = 90

Feature Vector = [6, 90]
```

The Machine Learning model receives feature vectors as input.

---

# Types of Features

## Numerical Features

Continuous numerical values.

### Examples

- Age
- Salary
- Height
- Weight

---

## Categorical Features

Text or category-based values.

These cannot be directly given to most Machine Learning algorithms.

They are converted into numbers using **Encoding**.

### Examples

- City
- Gender
- Blood Group

---

## Binary Features

Features having only two possible values.

### Examples

- Yes / No
- 0 / 1
- True / False

---

# Types of Target Variables

## Regression

The target is continuous.

Regression predicts **numerical values**.

### Examples

- House Price
- Salary
- Temperature
- Marks

---

## Classification

The target is categorical.

Classification predicts **categories or classes**.

### Examples

- Spam / Not Spam
- Disease / Healthy
- PCOS (Yes / No)

---

# What is a Machine Learning Model?

A Machine Learning Model is a mathematical function that learns patterns from data and makes predictions.

---

# Generalization

A good Machine Learning model should perform well on **unseen data**.

Example:

Training Accuracy = 100%

Testing Accuracy = 60%

This means the model has **poor generalization**.

A good model has a **small difference** between training accuracy and testing accuracy.

---

# Overfitting

Overfitting occurs when the model memorizes the training data instead of learning general patterns.

Example:

A student memorizes previous question papers but fails to answer new questions.

---

# Underfitting

Underfitting occurs when the model fails to learn meaningful patterns from the data.

Example:

A student does not study at all and performs poorly in every exam.

---


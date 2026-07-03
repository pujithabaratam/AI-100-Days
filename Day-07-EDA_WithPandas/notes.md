# Day 07 - Exploratory Data Analysis (EDA) with Pandas

## What is Exploratory Data Analysis (EDA)?

**Exploratory Data Analysis (EDA)** is the process of understanding, exploring, and summarizing a dataset before building a Machine Learning model.

EDA helps us:

* Understand the structure of the dataset.
* Find missing values and duplicates.
* Discover patterns and relationships.
* Prepare clean data for Machine Learning.

---

## Sorting Data

`sort_values()` is used to sort a DataFrame based on one or more columns.

### Sort in Ascending Order

```python
df.sort_values("Salary")
```

### Sort in Descending Order

```python
df.sort_values("Salary", ascending=False)
```

---

## Unique Values

`unique()` returns all unique values in a column.

```python
df["City"].unique()
```

Example Output:

```text
['Hyderabad' 'Vizag' 'Delhi']
```

---

## Number of Unique Values

`nunique()` returns the count of unique values.

```python
df["City"].nunique()
```

Example Output:

```text
3
```

---

## Value Counts

`value_counts()` counts how many times each value appears in a column.

```python
df["City"].value_counts()
```

Example Output:

```text
Hyderabad    3
Vizag        2
Delhi        1
```

This function is very useful for analyzing categorical data.

---

## Renaming Columns

`rename()` is used to rename one or more columns.

```python
df = df.rename(columns={"Salary": "MonthlySalary"})
```

---

## Adding a New Column

Create a new column using an existing column.

Example: Calculate a 10% bonus.

```python
df["Bonus"] = df["Salary"] * 0.10
```

---

## Deleting a Column

Remove a column from the DataFrame and returns a new DataFrame.

```python
df = df.drop("Bonus", axis=1)
```

* `axis=1` → Columns
* `axis=0` → Rows

---

## Basic Data Cleaning Workflow

A typical Machine Learning workflow is:

```text
Load Dataset
        ↓
Understand Dataset
        ↓
Check Missing Values
        ↓
Handle Missing Values
        ↓
Remove Duplicate Records
        ↓
Check Data Types
        ↓
Explore Statistics
        ↓
Filter Useful Data
        ↓
Feature Engineering
        ↓
Train Machine Learning Model
```

---

## Functions Learned Today

* `sort_values()`
* `unique()`
* `nunique()`
* `value_counts()`
* `rename()`
* `drop()`

---

## Interview Questions

### 1. What is Exploratory Data Analysis (EDA)?

**Answer:**

EDA is the process of exploring, understanding, and summarizing a dataset before building a Machine Learning model. It helps identify missing values, duplicates, patterns, and useful insights.

---

### 2. What is the difference between `unique()` and `nunique()`?

**Answer:**

* `unique()` returns all unique values in a column.
* `nunique()` returns the total number of unique values.

---

## Key Takeaways

* EDA is the first step after loading a dataset.
* Sorting helps organize data for analysis.
* `unique()` and `value_counts()` help analyze categorical columns.
* `rename()` makes column names more meaningful.
* New columns can be created using existing columns.
* The data cleaning workflow should be completed before training a Machine Learning model.

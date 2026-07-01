# Day 05 - Introduction to Pandas

## What is Pandas?

Pandas is a Python library used for:

* Data Analysis
* Data Cleaning
* Data Manipulation
* Working with tabular data (similar to Excel)

A Machine Learning Engineer spends a significant amount of time exploring and cleaning data before training a model. Pandas is the primary library used for these tasks.

---

## Why Do We Need Pandas?

Suppose we have student data stored in a NumPy array. To access the **Marks** column, we must remember its column index.

With Pandas, every column has a meaningful name, making the data easier to understand and work with.

---

## What is a Series?

A **Series** is a one-dimensional labeled array (a single column of data).

Example:

```python
import pandas as pd

marks = pd.Series([80, 90, 75, 88])

print(marks)
```

---

## What is a DataFrame?

A **DataFrame** is a two-dimensional table consisting of rows and columns.

A DataFrame can be thought of as a collection of multiple Series.

Example:

```python
import pandas as pd

students = pd.DataFrame({
    "Name": ["Rahul", "Anita", "John"],
    "Marks": [85, 91, 76],
    "Age": [20, 21, 19]
})

print(students)
```

---

## Reading a CSV File

Reading data from a CSV file is one of the most common tasks in AI and Machine Learning.

```python
import pandas as pd

df = pd.read_csv("students.csv")
```

---

## Exploring the Dataset

### First 5 Rows

```python
df.head()
```

### Last 5 Rows

```python
df.tail()
```

### Shape

```python
df.shape
```

Returns:

```text
(rows, columns)
```

### Column Names

```python
df.columns
```

### Information

```python
df.info()
```

Displays:

* Data types
* Missing values
* Number of rows and columns

### Statistical Summary

```python
df.describe()
```

Displays:

* Mean
* Minimum
* Maximum
* Standard Deviation
* Quartiles

---

## Difference Between Series and DataFrame

| Series                     | DataFrame                                  |
| -------------------------- | ------------------------------------------ |
| One-dimensional            | Two-dimensional                            |
| Represents a single column | Represents multiple columns                |
| Can store one type of data | Can store multiple columns of related data |

---

## Functions Learned Today

* `pd.Series()`
* `pd.DataFrame()`
* `pd.read_csv()`
* `head()`
* `tail()`
* `shape`
* `columns`
* `info()`
* `describe()`

---
## Methods Learned Today

* `students["Marks"].sum()`
* `students["Marks].mean()`
* `students["Marks].max()`
* `students["Marks].min()`
* `students["Marks].count()`

---


## Interview Question

### What is the difference between a Series and a DataFrame?

**Answer:**

A **Series** is a one-dimensional labeled array that represents a single column of data, whereas a **DataFrame** is a two-dimensional table made up of multiple rows and columns. A DataFrame can be considered a collection of Series.

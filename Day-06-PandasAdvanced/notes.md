# Day 06 - Pandas Filtering and Indexing

## What I Learned

Today I learned how to select specific data from a Pandas DataFrame using column names, conditions, `loc`, and `iloc`. These operations are commonly used while cleaning and preparing datasets for Machine Learning.

---

## Selecting a Single Column

Selecting a single column returns a **Series**.

```python
print(employees["Name"])
```

---

## Selecting Multiple Columns

Selecting multiple columns returns a **DataFrame**.

```python
print(employees[["Name", "Salary"]])
```

---

## Boolean Filtering

Boolean filtering returns only the rows that satisfy a given condition.

Example: Employees earning more than ₹50,000.

```python
print(employees[employees["Salary"] > 50000])
```

---

## Multiple Conditions

Use `&` for **AND** and `|` for **OR** while combining conditions.

Example:

```python
print(
    employees[
        (employees["Salary"] > 40000) &
        (employees["Age"] < 30)
    ]
)
```

---

## loc

`loc` selects data using **row labels** and **column names**.

* `:` → Select all rows
* Column names are used for selection

Example:

```python
print(employees.loc[:, ["Name", "Salary"]])
```

```python
print(employees.loc[0:2, ["Name", "Age"]])
```

---

## iloc

`iloc` selects data using **row numbers** and **column positions**.

Example:

```python
print(employees.iloc[:, 1:3])
```

---

## Difference Between loc and iloc

| loc                 | iloc                |
| ------------------- | ------------------- |
| Uses row labels     | Uses row positions  |
| Uses column names   | Uses column indexes |
| Example: `"Salary"` | Example: `2`        |

---

## Difference Between Selecting One Column and Multiple Columns

| Single Column        | Multiple Columns        |
| -------------------- | ----------------------- |
| Returns a **Series** | Returns a **DataFrame** |

---

## Missing Values (Preview)

### What is NaN?

**NaN (Not a Number)** represents a missing or undefined value in a dataset.

---

### Checking Missing Values

```python
df.isnull()
```

Returns `True` for missing values and `False` for available values.

Count missing values in each column:

```python
df.isnull().sum()
```

---
Print only the rows that contains at least one missing value.
```python
df.isnull().any(axis=1)
```

---


### Filling Missing Values

Replace missing values with a specific value:

```python
df.fillna(0)
```

Replace missing salary values with the average salary:

```python
df["Salary"].fillna(df["Salary"].mean())
```

This technique is widely used during data preprocessing in Machine Learning.
It does not modify the original DataFrame.
Instead, it returns a new Series with the missing values filled.

df["Salary"] = df["Salary"].fillna(0)

---

### Removing Missing Values

Remove rows containing missing values:

```python
df.dropna()
```

---

## Duplicates

Find duplicate rows:

```python
df.duplicated()
```

Remove duplicate rows:

```python
df.drop_duplicates()
```

---

## Functions Learned Today

* `loc`
* `iloc`
* `isnull()`
* `fillna()`
* `dropna()`
* `duplicated()`
* `drop_duplicates()`

---

## Interview Question

### What is the difference between `loc` and `iloc`?

**Answer:**

* `loc` selects data using row labels and column names.
* `iloc` selects data using integer row and column positions.

---

## Key Takeaways

* A single column returns a **Series**.
* Multiple columns return a **DataFrame**.
* Boolean filtering helps retrieve rows that satisfy a condition.
* Use `&` and `|` to combine multiple conditions.
* `loc` works with labels, while `iloc` works with positions.
* Missing values should be handled before training a Machine Learning model.
* Removing duplicates improves data quality and prevents repeated records from affecting analysis.

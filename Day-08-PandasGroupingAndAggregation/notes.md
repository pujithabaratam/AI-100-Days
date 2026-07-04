# Day 08 - Pandas Grouping & Aggregation

## What is `groupby()`?

`groupby()` is used to split the data into groups based on one or more columns and then perform calculations on each group.

Example:

```python
employees.groupby("Department")
```

---

## Average Salary in Each Department

Calculate the average salary of employees in each department.

```python
employees.groupby("Department")["Salary"].mean()
```

---

## Total Salary in Each Department

Calculate the total salary paid in each department.

```python
employees.groupby("Department")["Salary"].sum()
```

---

## Count Employees in Each Department

Count the number of employees in each department.

```python
employees.groupby("Department")["Name"].count()
```

---

## Maximum Salary in Each Department

Find the highest salary in each department.

```python
employees.groupby("Department")["Salary"].max()
```

---

## Minimum Salary in Each Department

Find the lowest salary in each department.

```python
employees.groupby("Department")["Salary"].min()
```

---

## Multiple Aggregations on the Same Column

Perform multiple calculations on a single column at once.

```python
employees.groupby("Department")["Salary"].agg(
    ["mean", "max", "min", "sum", "count"]
)
```

---

## Group By Multiple Columns

Group data using more than one column.

```python
employees.groupby(["Department", "City"])["Salary"].mean()
```

This is useful for generating more detailed reports.

---

## Multiple Aggregations on Multiple Columns

Perform different aggregations on multiple columns simultaneously.

```python
employees.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Age": ["mean", "max"]
})
```

---

## Sorting GroupBy Results

Find departments with the highest or lowest average salary.

Ascending order:

```python
employees.groupby("Department")["Salary"].mean().sort_values()
```

Descending order:

```python
employees.groupby("Department")["Salary"].mean().sort_values(ascending=False)
```

---

## `reset_index()`

After using `groupby()`, the grouped column becomes the index.

Use `reset_index()` to convert it back into a normal DataFrame.

```python
group = employees.groupby("Department")["Salary"].mean()

group.reset_index()
```

---

## Sorting by Multiple Columns

Sort data using multiple columns.

```python
employees.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
)
```

This sorts:

* Department in ascending order.
* Salary in descending order within each department.

---

## `nlargest()` and `nsmallest()`

These functions efficiently retrieve the highest or lowest values without sorting the entire DataFrame.

Top 3 highest salaries:

```python
employees.nlargest(3, "Salary")
```

Lowest 2 salaries:

```python
employees.nsmallest(2, "Salary")
```

---

## Functions Learned Today

* `groupby()`
* `mean()`
* `sum()`
* `count()`
* `max()`
* `min()`
* `agg()`
* `reset_index()`
* `sort_values()`
* `nlargest()`
* `nsmallest()`

---

## Interview Questions

### 1. What is `groupby()` in Pandas?

**Answer:**

`groupby()` is used to group rows in a DataFrame based on one or more columns and perform calculations on each group.

---

### 2. Why do we use aggregation functions?

**Answer:**

Aggregation functions summarize grouped data by performing calculations such as average, sum, maximum, minimum, and count.

---

### 3. What is the advantage of using `agg()` instead of calling `mean()`, `max()`, and `min()` separately?

**Answer:**

`agg()` allows us to perform multiple aggregation operations in a single statement, making the code shorter, cleaner, and more efficient.

---

## Real-World Use

Suppose a company wants to know:

* Average salary in each department.
* Number of employees in each department.
* Highest-paid employee in each department.

Using `groupby()` and aggregation functions, these insights can be generated with just a few lines of code.

---

## Quick Revision

✅ `groupby()` → Split data into groups.

✅ `mean()` → Average value.

✅ `sum()` → Total value.

✅ `count()` → Number of records.

✅ `max()` → Highest value.

✅ `min()` → Lowest value.

✅ `agg()` → Perform multiple aggregations together.

✅ `reset_index()` → Convert grouped index back to a normal DataFrame.

✅ `nlargest()` → Return top *n* highest values.

✅ `nsmallest()` → Return bottom *n* lowest values.

# Day 04 - NumPy Indexing, Filtering & Real Dataset Operations

## Student Dataset

```python
import numpy as np

students = np.array([
    [101, 85, 20],
    [102, 72, 21],
    [103, 91, 19],
    [104, 65, 22]
])
```

| Column Index | Description |
| -----------: | ----------- |
|            0 | Student ID  |
|            1 | Marks       |
|            2 | Age         |

---

## Row Indexing

### First Student

```python
print(students[0])
```

### Last Student

```python
print(students[-1])
```

---

## Column Indexing

### Marks Column

```python
print(students[:, 1])
```

`:` means **all rows**, and `1` represents the **Marks** column.

### Student IDs

```python
print(students[:, 0])
```

### Age

```python
print(students[:, 2])
```

---

## Access Multiple Columns

To access the **Marks** and **Age** columns:

```python
students[:, 1:]
```

---

## Boolean Filtering

Extract the marks column:

```python
marks = students[:, 1]
```

Print students scoring more than 80 marks:

```python
print(students[marks > 80])
```

Boolean filtering returns only the rows that satisfy the given condition.

---

## Multiple Conditions

Students with:

* Marks greater than 70
* Age less than 21

```python
print(students[(students[:, 1] > 70) & (students[:, 2] < 21)])
```

**Note:** Use `&` for AND and `|` for OR with NumPy arrays.

---

## Modify Values

Add 5 grace marks to every student:

```python
students[:, 1] += 5
```

---

## Conditional Replacement

Replace marks below 35 with 35:

```python
marks[marks < 35] = 35
```

---

## Functions Learned Today

* Array Indexing
* Column Selection
* Boolean Filtering
* Multiple Conditions (`&`, `|`)
* Conditional Replacement
* Vectorized Updates

---

## Real AI Example

Imagine you're working on a loan approval dataset.

Before training the model, you want only customers:

Age > 21
Salary > ₹50,000

You'll write code similar to:

```filtered = customers[
    (customers[:, 1] > 50000) &
    (customers[:, 2] > 21)
]```

This kind of filtering is done before feeding data into machine learning models.

## Interview Question

### Why do we use `&` instead of `and` in NumPy?

`and` works with single Boolean values, whereas `&` performs element-wise logical operations on NumPy arrays. That's why `&` is used when combining multiple conditions in NumPy.

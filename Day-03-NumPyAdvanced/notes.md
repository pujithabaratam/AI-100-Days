# Day 03 - NumPy Advanced: Multi-Dimensional Arrays & Matrix Operations

## Why Multi-Dimensional Arrays?

In AI, data is rarely one-dimensional.

Most Machine Learning datasets are represented as **2D arrays**, where:

* **Rows** represent records (Students, Customers, Employees, etc.)
* **Columns** represent features (Age, Salary, Marks, Attendance, etc.)

---

## Creating a 2D Array

```python
import numpy as np

students = np.array([
    [20, 85, 90],
    [21, 92, 95],
    [19, 76, 88]
])
```

---

## Shape and Size

`shape` returns the number of rows and columns in an array.
`size` returns the total number of elements in an array

```python
print(students.shape)
print(students.size)
```

Output:

```text
(3, 3)
9
```

This means:

* 3 Rows
* 3 Columns

---

## Accessing Elements

### First Row

```python
print(students[0])
```

### Second Row, Third Column

```python
print(students[1][2])
```

---

## Reshape (1D → 2D)

`reshape()` changes the shape of an array without changing its values.

```python
nums = np.array([1, 2, 3, 4, 5, 6])

matrix = nums.reshape(2, 3)
```

---

## Flatten (2D → 1D)

`flatten()` converts a multi-dimensional array back into a one-dimensional array.

```python
matrix.flatten()
```

---

## Axis

The `axis` parameter is one of the most important concepts in NumPy. It is used extensively in **Pandas**, **Machine Learning**, and **Deep Learning**.

```python
marks = np.array([
    [80, 90, 70],
    [60, 75, 85]
])
```

### Sum of Each Column (`axis = 0`)

```python
np.sum(marks, axis=0)
```

### Sum of Each Row (`axis = 1`)

```python
np.sum(marks, axis=1)
```

### Easy to Remember

* `axis = 0` → Column-wise operation
* `axis = 1` → Row-wise operation

---

## Random Numbers

NumPy can generate random numbers, which are often used to create sample datasets for testing.

```python
np.random.randint(1, 10, size=(3, 3))
```

---

## What I Learned Today

* Learned how to create 2D NumPy arrays.
* Understood the difference between 1D and 2D arrays.
* Learned how to use `shape` to determine array dimensions.
* Learned to convert arrays using `reshape()` and `flatten()`.
* Understood how `axis=0` and `axis=1` work.
* Learned how to generate random matrices using NumPy.



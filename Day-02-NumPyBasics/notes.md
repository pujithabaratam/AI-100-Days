# Day 02 - NumPy Basics

## What is NumPy?

If Python is the language of AI, **NumPy is the foundation of AI programming**.

Almost every AI library internally uses NumPy, including:

* Scikit-learn
* Pandas
* TensorFlow
* PyTorch
* OpenCV

---

## Why Do We Use NumPy?

Python lists work well for small datasets, but they become slower when working with large amounts of numerical data.

NumPy performs mathematical operations much faster because it is optimized for numerical computation and supports vectorized operations.

---

## What is a NumPy Array?

A **NumPy array** is similar to a Python list, but it is:

* Faster
* More memory-efficient
* Designed for mathematical operations

### Example

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])

print(numbers)
```

---

## Vectorized Operations

Instead of using a loop:

```python
numbers = [1, 2, 3]

result = []

for n in numbers:
    result.append(n * 2)
```

NumPy allows us to perform the operation on the entire array at once:

```python
import numpy as np

numbers = np.array([1, 2, 3])

result = numbers * 2

print(result)
```

Applying an operation to an entire array without using explicit loops is called **Vectorization**. This is one of the main reasons why NumPy is much faster than Python lists.

---

## What I Learned Today

* NumPy is the foundation of numerical computing in AI.
* NumPy arrays are faster and more memory-efficient than Python lists.
* NumPy provides built-in mathematical functions like `np.max()`, `np.min()`, `np.mean()`, and `np.sum()`.
* Vectorized operations eliminate the need for explicit loops and improve performance.
* Boolean indexing allows us to filter data efficiently.

---
What is Standard Deviation?

It tells us how spread out the values are from the average.

Small standard deviation → Marks are close to the average.
Large standard deviation → Marks are spread far from the average.

## Functions Practiced Today

* `np.array()`
* `np.max()`
* `np.min()`
* `np.mean()`
* `np.sum()`
* `np.std()`
* `np.argmax()`-it returns the index of maximum value,not the value itself
* `np.argmin()`
* Boolean Indexing (`marks > 60`)
* Vectorized Operations (`marks + 5`)

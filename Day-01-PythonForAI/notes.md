# Python for AI

## What I learned Today

### Why Python for AI?

- Python is simple and easy to learn.
- It has many AI libraries like NumPy, Pandas, Scikit-learn, PyTorch, and TensorFlow.
- It allows developers to focus on solving AI problems instead of writing a lot of code.

Python
│
├── NumPy        → Mathematical Operations
├── Pandas       → Data Analysis
├── Matplotlib   → Charts
├── Scikit-learn → Machine Learning
├── PyTorch      → Deep Learning
├── Hugging Face → LLM Models
├── LangChain    → Build AI Apps
├── ChromaDB     → Vector Database
└── FastAPI      → Deploy AI Models

### Dictionary

A dictionary stores data as key-value pairs.

Example:

```python
student = {
    "name": "Pujitha",
    "marks": 90
}
```

---

### List Comprehension

List comprehension creates a new list in a single line.

Example:

```python
numbers = [1,2,3]

squares = [x*x for x in numbers]
```

---

### zip()

`zip()` combines multiple lists together.

Example:

```python
names = ["A","B"]

marks = [80,90]

for name, mark in zip(names, marks):
    print(name, mark)
```

---

### enumerate()

`enumerate()` provides both the index and the value while iterating.

Example:

```python
names = ["A","B"]

for index, value in enumerate(names):
    print(index, value)
```

---

## Summary

Today I revised Python concepts that are commonly used in AI development. I also learned why Python is the preferred language for AI and refreshed important concepts like dictionaries, list comprehensions, zip(), and enumerate().


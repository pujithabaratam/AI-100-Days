# Day 11 - Mini Project 1: Student Performance Analysis System (Part 1)

## What is a CSV File?

CSV (Comma-Separated Values) is a file format used to store tabular data.

Each row represents a record, and each column represents a field.

Example:

```csv
ID,Name,Math,Science,English,City,Attendance
101,Rahul,85,90,78,Hyderabad,92
102,Anita,92,88,95,Vizag,96
```

---

# Why do we use CSV in AI?

CSV is one of the most commonly used file formats because it is:

- Simple to create
- Easy to read
- Lightweight
- Supported by almost every Machine Learning library
- Easy to import and export

---

# Real-World AI Example

In Machine Learning projects, the first step is usually:

```python
df = pd.read_csv("dataset.csv")
```

Then we:

- Explore the dataset using `head()` and `info()`
- Understand statistics using `describe()`
- Create new features
- Filter useful data
- Prepare the dataset for model training

This is the standard workflow followed in most AI projects.

---

# Correlation

Sometimes two variables are related.
For example Attendance increases Average Marks increases 
This is called Positive correlation

```python
students[["Attendance", "Average"]].corr()
```

How to interpret it?
Correlation	Meaning
1.0	Perfect positive relationship
0.8	Strong positive relationship
0.5	Moderate relationship
0	No relationship
-1	Perfect negative relationship

# idxmax() 
It is very useful in interviews
idxmax() returns the index (city name) corresponding to the maximum value.
```python
    print(
        students.groupby("City")["Average"]
        .mean()
        .idxmax()
    )
```

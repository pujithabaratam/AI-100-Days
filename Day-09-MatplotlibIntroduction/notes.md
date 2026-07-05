# Day 09 - Data Visualization with Matplotlib

## What is Data Visualization?

Until now, we analyzed data using Pandas. Data Visualization helps us represent that data graphically so that it is easier to understand and interpret.

- A **Data Analyst** explains insights using charts.
- An **AI Engineer** visualizes data before training Machine Learning models.

---

# What is Matplotlib?

Matplotlib is one of the most popular Python libraries used for creating graphs and charts.

Import Matplotlib:

```python
import matplotlib.pyplot as plt
```

---

# Why do we use Matplotlib?

- Understand patterns
- Compare values
- Detect trends
- Find outliers
- Present data visually

---

# Line Chart

A Line Chart is used to show **trends over time**.

Syntax:

```python
plt.plot(x, y)
```

Example:
- Monthly Sales
- Temperature over a week
- Stock prices

---

# Bar Chart

A Bar Chart is used to **compare different categories**.

Syntax:

```python
plt.bar(x, y)
```

Example:
- Employees in each department
- Students in each class

---

# Scatter Plot

A Scatter Plot shows the **relationship between two numerical variables**.

Syntax:

```python
plt.scatter(x, y)
```

Example:
- Age vs Salary
- Height vs Weight

If the points move upward together, there may be a **positive relationship** between the two variables.

---

# Histogram

A Histogram shows the **distribution of numerical data**.

Syntax:

```python
plt.hist(x)
```

By default, Matplotlib automatically chooses a reasonable number of **bins** based on the amount and spread of the data.

### Specify the Number of Bins

```python
plt.hist(x, bins=5)
```

### Bin Width Formula

```
Bin Width = (Maximum Value - Minimum Value) / Number of Bins
```

A histogram counts how many values fall into each bin (interval).

---

# Pie Chart

A Pie Chart shows the **proportion or percentage** of each category in the whole dataset.

Syntax:

```python
plt.pie(y, labels=x, autopct="%1.1f%%")
```

Example:
- Employees by department
- Students by city

---

# Improving Charts

## Add a Title

```python
plt.title("Chart Title")
```

## Label the X-axis

```python
plt.xlabel("X-axis")
```

## Label the Y-axis

```python
plt.ylabel("Y-axis")
```

## Add Grid Lines

```python
plt.grid(True)
```

or

```python
plt.grid(False)
```

## Add Legend

```python
plt.plot(months, sales, label="Sales")
plt.legend()
```

### What is `label`?

`label` stores the name of the plotted data.

### What does `legend()` do?

`legend()` displays all the labels in a small box on the graph, making it easy to identify different plotted datasets.

---

# Functions Learned Today

- `plot()`
- `bar()`
- `scatter()`
- `hist()`
- `pie()`
- `title()`
- `xlabel()`
- `ylabel()`
- `grid()`
- `legend()`

---

# Interview Questions

## 1. What is Matplotlib?

**Answer:**

Matplotlib is a Python library used to create graphs and charts for visualizing data.

---

## 2. When should you use a Line Chart?

**Answer:**

A Line Chart is used to show trends or changes over time.

---

## 3. When should you use a Bar Chart?

**Answer:**

A Bar Chart is used to compare values across different categories.

---

## 4. What is a Scatter Plot used for?

**Answer:**

A Scatter Plot is used to show the relationship between two numerical variables.

---

## 5. What is a Histogram?

**Answer:**

A Histogram displays the distribution of numerical data by grouping values into intervals called bins.

---

## 6. What is a Pie Chart?

**Answer:**

A Pie Chart shows the percentage or proportion of each category in the dataset.

---

## 7. What is `legend()` in Matplotlib?

**Answer:**

`legend()` displays a box on the graph that identifies different plotted datasets using their labels. It helps readers understand what each line, bar, or marker represents.

---

# Real-World AI Example

Suppose you are analyzing a PCOS dataset.

You can create:

- Histogram → Age distribution
- Scatter Plot → Age vs BMI
- Pie Chart → PCOS vs Non-PCOS patients
- Bar Chart → Number of patients in each hospital

Visualization helps us understand the data before building Machine Learning models.

---

# Quick Revision

✅ `plot()` → Line Chart (Trend)

✅ `bar()` → Compare Categories

✅ `scatter()` → Relationship between two numerical variables

✅ `hist()` → Distribution of numerical data

✅ `pie()` → Percentage / Proportion

✅ `title()` → Add chart title

✅ `xlabel()` → Label X-axis

✅ `ylabel()` → Label Y-axis

✅ `grid()` → Add grid lines

✅ `legend()` → Display labels for plotted data
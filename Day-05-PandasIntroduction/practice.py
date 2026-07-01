#Task1:
import pandas as pd
marks=pd.Series([85,90,76,88,95])
print(marks)

#Task2:
students = pd.DataFrame({
    "Name": ["Rahul", "Anita", "John", "Sara"],
    "Marks": [85, 92, 76, 89],
    "Age": [20, 21, 19, 22]
})
print(students)

#Task3:
print("Shape:",students.shape)
print("Column Names:",students.columns)
print("Information:",students.info())
print("Describe:",students.describe())

#Task4:
print(students.head())
print(students.tail())

#Task5: print only marks column
print(students["Marks"])

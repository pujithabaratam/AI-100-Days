import pandas as pd
students=pd.DataFrame({
    "Name":["Rahul","Anitha","John","Sara","David"],
    "Marks":[85,92,76,89,60],
    "Age":[20,21,19,22,20],
    "City":["Hyderabad","Vizag","Delhi","Chennai","Mumbai"]
})

print(students["Name"])
print("----------")
print(students[["Name","Marks"]])
print("----------")
print("Students scoring above 80")
print(students[students["Marks"]>80])
print("----------")
print("Students younger than 21")
print(students[students["Age"]<21])
print("----------")
print("Students scoring above 80 and younger than 21")
print(students[(students["Marks"]>80) & (students["Age"]<21)])
print("----------")
print("Name and city using loc")
print(students.loc[:,["Name","City"]])
print("----------")
print("print Marks and Age using iloc")
print(students.iloc[:,1:3])
print("----------")
print(students.iloc[:,[1,2]])
print("----------")

import pandas as pd
import numpy as np

employees = pd.DataFrame({
    "ID": [1, 2, 2, 4, 5, 6],
    "Name": ["Amit", "Riya", "Riya", "Sara", "David", "John"],
    "Salary": [50000, np.nan, 70000, 90000, 30000, np.nan],
    "Age": [26, 32, 32, np.nan, 22, 28]
})

print(employees)

print(employees.isnull())
print(employees.isnull().sum())
print(employees.fillna(0))
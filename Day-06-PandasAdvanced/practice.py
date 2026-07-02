#Task 1:
import pandas as pd
employees=pd.DataFrame({
    "ID":[1,2,3,4,5],
    "Name":["Amit","Riya","John","Sara","David"],
    "Salary":[50000,70000,45000,90000,30000],
    "Age":[26,32,24,40,22]
})
print("Employee Names")
print(employees["Name"])
print("-------")

#Task2:
print("Employee Name and Salary")
print(employees[["Name","Salary"]])
print("-------------")

#Task3: Employee earning more than 50000
print(employees[employees["Salary"]>50000])
print("-------------")

#Task4: Employee younger than 30
print(employees[employees["Age"]<30])
print("-------------")

#Task5: Employees: Salary > ₹40,000, Age < 30
print(employees[(employees["Salary"]>40000) & (employees["Age"]<30)])
print("-------------")

#Task6: Using loc print Name and Salary
print(employees.loc[:,["Name","Salary"]])
print("-------------")

#Task7: Using iloc, print Name and Salary
print(employees.iloc[:,1:3])
print("-------------")


import numpy as np
df=pd.DataFrame({
    "Name":["Amit","Riya","John"],
    "Salary":[50000,np.nan,70000]
})
print(df)

print("Check Null values")
print(df.isnull())
print("Count missing values")
print(df.isnull().sum())
print("Replace Null Value")
df["Salary"]=df["Salary"].fillna(0)
print(df["Salary"])
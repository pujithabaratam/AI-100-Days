import pandas as pd
import numpy as np
employees=pd.DataFrame({
    "ID":[1,2,3,4,5],
    "Name":["Amit","Riya","John","Sara","David"],
    "Salary":[50000,70000,45000,90000,30000],
    "Age":[26,32,24,40,22]
})
print("Employee Names")
print(employees["Name"])
print("----------")
print("Employee Salaries")
print(employees["Salary"])
print("----------")
print("Average Salaries:")
print(employees["Salary"].mean())
print("----------")
print("Maximum Salary:")
print(employees["Salary"].max())
print("----------")
print("Minimum Salary:")
print(employees["Salary"].min())
print("----------")
print("Shape:",employees.shape)
print("Columns:",employees.columns)
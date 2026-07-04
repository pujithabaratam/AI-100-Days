import pandas as pd

employees = pd.DataFrame({
    "Name": ["Amit","Riya","John","Sara","David","Priya"],
    "Department": ["IT","HR","IT","HR","Finance","IT"],
    "Salary": [50000,60000,70000,65000,55000,80000],
    "Age": [25,30,28,32,27,29]
})

print(employees)

employees=employees.sort_values(
    ["Department","Salary"],
    ascending=[True,False]
)
print(employees)
print("-------------")

print(employees.nlargest(3,"Salary"))

print("--------------")

# Task 1: Print the average salary for each department.
print(employees.groupby("Department")["Salary"].mean())

# Task 2: Print the total salary for each department.
print(employees.groupby("Department")["Salary"].sum())

# Task 3: Print the highest salary for each department.
print(employees.groupby("Department")["Salary"].max())

# Task 4: Print the lowest salary for each department.
print(employees.groupby("Department")["Salary"].min())

# Task 5: Count employees in each department.
print(employees.groupby("Department")["Name"].count())

# Task 6: Use agg() for Salary column.
print(employees.groupby("Department")["Salary"].agg(["mean","max","min","sum","count"]))

# Task 7: Print the average salary by Department and City
group=employees.groupby(["Department","Age"])["Salary"].mean()
print(group)

# Task 8: Reset_Index
print(group.reset_index())
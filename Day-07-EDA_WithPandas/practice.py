import pandas as pd
employees=pd.DataFrame({
    "ID":[1,2,3,4,5],
    "Name":["Amit","Riya","John","Sara","David"],
    "Salary":[50000,70000,45000,90000,30000],
    "Age":[26,32,24,40,22],
    "City":["Hyderabad","Vizag","Hyderabad","Delhi","Vizag"]
})

# Task1: Sort employees by Salary
employees=employees.sort_values("Salary")
print(employees)
print("-----------")
employees=employees.sort_values("Salary",ascending=False)
print(employees)

# Task2: Unique values
print(employees["City"].unique())

# Task3: Count employees from each city
print(employees["City"].value_counts())

# Task4: Rename
employees=employees.rename(columns={"Salary":"MonthlySalary"})
print(employees)

# Task5:Create a new column
employees["Bonus"]=employees["MonthlySalary"] * 0.1
print(employees)

# Task 6: Delete the bonus column
employees=employees.drop("Bonus",axis=1)
print(employees)
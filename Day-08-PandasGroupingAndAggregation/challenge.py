import pandas as pd

employees = pd.DataFrame({
    "ID":[101,102,103,104,105,106,107,108],
    "Name":["Amit","Riya","John","Sara","David","Priya","Kiran","Meena"],
    "Department":["IT","HR","IT","HR","Finance","IT","Finance","HR"],
    "City":["Hyderabad","Vizag","Hyderabad","Delhi","Vizag","Hyderabad","Delhi","Vizag"],
    "Salary":[50000,60000,70000,65000,55000,80000,72000,62000],
    "Age":[25,30,28,32,27,29,31,26],
    "Experience":[2,5,4,6,3,7,5,2]
})

# Level1:
print("Employee Names:")
print(employees["Name"])
print("---------------")
print("Salary")
print(employees["Salary"])
print("---------------")
print("Employees salary greater than 60000")
print(employees[employees["Salary"]>60000])
print("---------------")
print("Employees belongs to IT Department and salary greater than 60000")
print(employees[(employees["Department"]=="IT") & (employees["Salary"]>60000)])
print("---------------")

# Level2:
print("Sort employees by salary (Highest first).")
print(employees.sort_values("Salary",ascending=False))

print("Sort employees by Department, Salary (Highest first inside each department)")
print(employees.sort_values(
    ["Department","Salary"],
    ascending=[True,False]
))

print("Top 3 highest-paid employees.")
print(employees.nlargest(3,"Salary"))

# Level 3:
print("Find the average salary for each department.")
print(employees.groupby("Department")["Salary"].mean())

print("Use agg() to display: Mean Salary, Maximum Salary, Minimum Salary, Total Salary,Employee Count")
print(employees.groupby("Department")["Salary"].agg(
    ["mean","max","min","sum","count"]
))

# Level4:
print("Find the average salary based on: Department,City")
group=employees.groupby(["Department","City"])["Salary"].mean()
print(group)
print("--------------------")
print(group.reset_index())
print("--------------------------")
print("Sort the departments based on average salary.Highest first.")
print(employees.groupby("Department")["Salary"].mean().sort_values(ascending=False))

# Level 5:
print("Rename Salary to MonthlySalary")
print(employees.rename(columns={"Salary":"MonthlySalary"}))
print("---------------------")
print("New Column")
employees["Bonus"]=employees["Salary"]*0.15
print(employees)
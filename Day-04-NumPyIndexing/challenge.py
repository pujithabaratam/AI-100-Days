import numpy as np

employees=np.array([
    [1,50000,26],
    [2,70000,32],
    [3,45000,24],
    [4,90000,40],
    [5,30000,22]
])

#Employees earning more than ₹50,000
print(employees[employees[:,1]>50000])

#Employees younger than 30
print(employees[employees[:,2]<30])

#Employees earning more than ₹40,000 and younger than 30
print(employees[(employees[:,1]>40000) & (employees[:,2]<30)])

#Increase everyone's salary by ₹5,000
employees[:,1]+=5000
print(employees[:,1])

#Replace salaries below ₹50,000 with ₹50,000
salary=employees[:,1]
salary[salary<50000]=50000
salary=employees[:,1]
print(salary)

salary1 = employees[:,1].copy()
#This creates an independent copy that won't affect the original array.

#Print the average salary
print("Average Salary:",np.mean(salary))
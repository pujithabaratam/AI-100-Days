import matplotlib.pyplot as plt

# Line Chart
months=["Jan","Feb","Mar","Apr","May"]
sales=[100,120,150,180,210]
profit = [30,40,50,65,89]
plt.plot(months,sales,label="Sales")
plt.plot(months,profit,label="Profit")
plt.title("Line Chart for Monthly Sales")
plt.legend()
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Bar Chart
import pandas as pd
employees = pd.DataFrame({
    "Name": ["Amit","Riya","John","Sara","David","Priya"],
    "Department": ["IT","HR","IT","HR","Finance","IT"],
    "Salary": [50000,60000,70000,65000,55000,80000],
    "Age": [25,30,28,32,27,29],
    "marks": [45, 50, 52, 60, 62, 70]
})
group=(
    employees.groupby("Department")["Name"]
    .count()
    .reset_index(name="Count")
)

plt.bar(group["Department"],group["Count"])
plt.title("Number of employees in each department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.show()

# Scatter Plot
plt.scatter(employees["Age"],employees["Salary"])
plt.title("Scatter Plot between Age and Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# Histogram
plt.hist(employees["marks"])
plt.legend(employees["Name"])
plt.show()

# Pie Chart
departments=group["Department"]
count=labels=group["Count"]
plt.pie(count,labels=departments,autopct="%1.1f%%")
plt.title("Department Distribution")
plt.show()




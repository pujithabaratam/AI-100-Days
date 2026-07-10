import pandas as pd

students=pd.DataFrame({
    "Hours":[2,4,6,8,10],
    "Attendance":[75,80,85,90,95],
    "Marks":[40,55,70,85,95]
})

print("Features:")
print(students[["Hours","Attendance"]])

print("Target:")
print(students["Marks"])
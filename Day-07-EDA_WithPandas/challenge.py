import pandas as pd
students=pd.DataFrame({
    "IDs":[1,2,3,4,5],
    "Names":["Pranay","Priya","Hari","John","Riya"],
    "Marks":[90,96,89,97,69],
    "City":["Hyderabad","Delhi","Hyderabad","Vizag","Delhi"]
})
print(students)

# Highest Marks
print(students["Marks"].max())

# Lowest Marks
print(students["Marks"].min())

# Average Marks
print(students["Marks"].mean())

# Sort Students by marks
students=students.sort_values("Marks")
print(students)

# Rename Marks to Score
students=students.rename(columns={"Marks":"Score"})
print(students)

# Students From Hyderabad
print(students[students["City"]=="Hyderabad"])

# Add Grade column
students["Grade"]=['A','A','B','A','C']
print(students)

import pandas as pd
students=pd.read_csv("dataset.csv")
print(students)
print(students.shape)
print(students.columns)
# info() provides the structure of the DataFrame, including
# the number of rows, column names, data types, and non-null values.
print(students.info())
# By using describe() we deal with statistical measurements of dataset like mean,std etc
print(students.describe())

students["Total"]=students["Math"]+students["Science"]+students["English"]
students["Average"]=students["Total"]/3

# Sort based on average
print(students.sort_values("Average",ascending=False))

#Students from Hyderabad
print(students[students["City"]=="Hyderabad"])

#Students with Average above 85
print(students[students["Average"]>85])

# Highest Average
print(students.sort_values("Average",ascending=False).head(1))

# Lowest Average
print(students.sort_values("Average").head(1))

# How many students from each city
print(students["City"].value_counts()) 

# Average Attendance
print(students["Attendance"].mean())

# Top 3 students
print(students.nlargest(3,"Average"))

# Bottom 2 students
print(students.nsmallest(2,"Average"))

# Create Result column based on Average
result=[]
for avg in students["Average"]:
    if avg>=75:
        result.append("Pass")
    else:
        result.append("Fail")
students["Result"]=result

print(students)

# Another way
temp=students[students["Average"]>85]
temp["Result"]="Pass"
students["Result"]=temp["Result"]
students["Result"].fillna("Fail")

# Find the city with the highest average marks
print(students.groupby("City")["Average"].mean().sort_values(ascending=False).nlargest(1))

# Create new Column Performance based on conditions
Perf=[]
for avg in students["Average"]:
    if avg>=90:
        Perf.append("Excellent")
    elif avg>=80:
        Perf.append("Good")
    elif avg>=70:
        Perf.append("Average")
    else:
        Perf.append("Need Improvement")
students["Performance"]=Perf
print(students)

# Find the Subject with highest average
subject_avg=students[["Math","Science","English"]].mean()
print(subject_avg.idxmax())




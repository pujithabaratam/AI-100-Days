import numpy as np
students = np.array([
    [101,85,20],
    [102,72,21],
    [103,91,19],
    [104,65,22],
    [105,55,20]
])

#Task1: Print Student IDs
print("Student Ids:",students[:,0])

#Task2: Print Student Marks
print("Marks:",students[:,1])

#Task3: Print Ages
print("Ages:",students[:,2])

#Task4: Students scoring above 80
print(students[students[:,1]>80])

#Task5: Students younger than 21
print(students[students[:,2]<21])

#Task6: Students marks>70 and Age<21
print(students[(students[:,1]>80) & (students[:,2]<21)])

#task7: Add 5 marks to everyone
students[:,1]+=5
print(students[:,1])

#Task8: Marks below 60 replace 60
students[students[:,1]<60]=60


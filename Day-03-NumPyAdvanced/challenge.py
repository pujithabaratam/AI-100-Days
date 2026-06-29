import numpy as np

marks = np.array([
    [80,75,90],
    [65,70,60],
    [95,88,92],
    [45,50,40]
])

#Average marks of each Student
print(np.mean(marks,axis=1))

#Average marks of each subject
print(np.mean(marks,axis=0))

#Highest mark in the class
print(np.max(marks))

#Lowest mark in the class
print(np.min(marks))

#Students whose average is greater than 75
avg_marks=np.mean(marks,axis=1)
above_75=avg_marks > 75
print(avg_marks[above_75])

for index,value in enumerate(avg_marks):
    if value>75:
        print("Student:",index,"Avg_Marks:",value)
    

#Add 5 grace marks to every student
new_marks=marks+5
print(new_marks)



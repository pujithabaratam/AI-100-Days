# Task1:
import numpy as np
students=np.array([
    [20,85,90],
    [21,92,95],
    [19,76,88]
])
#Number of rows and columns
print("Shape:",students.shape)
print("Number of Dimensions:",students.ndim)
print("Size:",students.size)
print("Data type:",students.dtype)

#Task2:
print(students[0]) #First row
print(students[2]) #Third row
print(students[1][1]) # Second row, Second column

#Task3:
numbers=np.array([1,2,3,4,5,6,7,8])
#convert to 2X4
matrix=numbers.reshape(2,4)
print(matrix)
matrix1=numbers.reshape(4,2)
print(matrix1)

#Task4:
print(matrix.flatten())

#Task5:
marks = np.array([
    [80,90,70],
    [60,75,85],
    [95,88,91]
])
print(np.sum(marks,axis=1)) # Sum of rows
print(np.sum(marks,axis=0)) #Sum of columns
print(np.mean(marks,axis=1)) #Average of each row
print(np.mean(marks,axis=0)) #Average of each column

#Task6:
print("Random Matrix:")
print(np.random.randint(1,100,size=(4,4)))
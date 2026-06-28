#Task1: Create Arrays
import numpy as np
marks=np.array([80,90,70,60,95]);
print(marks)

#Task2: Array Properties
print(marks.shape)
print(marks.size)
print(marks.dtype)

#Task3: Mathematical Operations
print("Sum:",np.sum(marks))
print("Average:",np.mean(marks))
print("Maximum:",np.max(marks))
print("Minimum:",np.min(marks))

#Task4: Vectorized Operations
bonus_marks=marks+5
print(bonus_marks)

#Task5: Indexing
print(marks[0])
print(marks[2])
print(marks[-1])

#Task6: Slicing
print(marks[1:4])
print(marks[:3])
print(marks[2:])

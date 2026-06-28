#Task 1:

students={
    "Rahul":85,
    "Anitha":91,
    "John":42,
    "Sara":76,
    "Mike":33
}

marks=students.values()
print(marks)
print("Sum:",sum(marks))
print("Length:",len(marks))
print("Minimum:",min(marks))
print("Maximum:",max(marks))
print("--------------")

#Iteration
for key in students:
    print(f"Key:{key}, Value:{students[key]}")
print("--------------")
for value in students.values():
    print(value,end=" ")

for key,value in students.items():
    print(f"Key:{key},Value:{value}")
print("--------------")

#Task2:

numbers = [1,2,3,4,5,6,7,8,9,10]
for num in numbers:
    print(num*num)


#Task3:
subjects = ["Math","Physics","Chemistry"]

marks = [80,92,88]
for sub,mark in zip(subjects,marks):
    print(sub,":",mark)



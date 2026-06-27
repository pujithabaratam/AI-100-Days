# Ask the user to enter 5 students' names and marks.
# Store them in a dictionary.

students={}

for i in range(1,6):
    name=input(f"Enter student{i} name :")
    marks=int(input(f"Enter student{i} marks:"))
    students[name]=marks

for key in students:
    print(f"{key}:{students[key]}")

marksList=students.values()
print("Average Marks:",sum(marksList)/len(marksList))


passed=[]
fail=[]
for key in students:
    if students[key]>35:
        passed.append(key)
    else:
        fail.append(key)
print("Passed Students")
print(passed)
print("Failed Students")
print(fail)
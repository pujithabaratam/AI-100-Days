import pandas as pd
import matplotlib.pyplot as plt

students=pd.read_csv("dataset.csv")
city_count=students["City"].value_counts()

# Bar Chart

plt.bar(city_count.index,city_count.values)
plt.title("Students by City")
plt.xlabel("City")
plt.ylabel("Students")
plt.show()

# Pie Chart

plt.pie(city_count.values,labels=city_count.index,autopct="%1.1f%%")
plt.title("Students by City")
plt.show()


# Subject-wise Average Marks

average_marks=[students["Math"].mean(),students["Science"].mean(),students["English"].mean()]
print(average_marks)
subjects=["Math","Science","English"]
plt.bar(subjects,average_marks)
plt.title("Average_marks by Subject")
plt.xlabel("Subjects")
plt.ylabel("Average_Marks")
plt.show()

# Marks Distribution

students["Total"] = (
    students["Math"] +
    students["Science"] +
    students["English"]
)

students["Average"] = students["Total"] / 3

plt.hist(students["Average"],bins=5)
plt.title("Average Marks Distribution")
plt.xlabel("Average")
plt.ylabel("Number of students")
plt.show()


# Attendance Vs Average
plt.scatter(students["Attendance"],students["Average"])
plt.title("Attendance vs Average")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()


import pandas as pd
students=pd.DataFrame({
    "Name":["Rahul","Anitha","John","Sara","David"],
    "Marks":[85,92,76,89,60],
    "Age":[20,21,19,22,20],
    "City":["Hyderabad","Vizag","Hyderabad","Delhi","Vizag"]
})


import matplotlib.pyplot as plt
# plt.bar(students["Name"],students["Marks"])
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.title("Bar Chart of Student Marks")
# plt.show()

# plt.hist(students["Marks"],bins=5)
# plt.show()


# count=students["City"].value_counts()
# plt.pie(count.values,labels=count.index,autopct="%1.1f%%")
# plt.title("Pie Chart showing students by city")
# plt.show()


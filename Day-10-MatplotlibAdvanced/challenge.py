import pandas as pd
students=pd.DataFrame({
    "Name":["Rahul","Anitha","John","Sara","David"],
    "Marks":[85,92,76,89,60],
    "Age":[20,21,19,22,20],
    "City":["Hyderabad","Vizag","Hyderabad","Delhi","Vizag"]
})

unique_cities=students["City"].value_counts()
print(unique_cities)

import matplotlib.pyplot as plt
plt.pie(unique_cities.values,labels=unique_cities.index,autopct="%1.1f%%")
plt.savefig("students_chart.png")
plt.show()

plt.figure(figsize=(8,8))
plt.subplot(5,5,1)
plt.bar(unique_cities.index,unique_cities.values)
plt.subplot(6,6,2)
plt.pie(unique_cities.values,labels=unique_cities.index,autopct="%1.1f%%")
plt.show()
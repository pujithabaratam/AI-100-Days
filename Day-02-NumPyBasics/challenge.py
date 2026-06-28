import numpy as np
marks=np.array([65,72,81,49,90,55,38])
print("Highest Marks:",np.max(marks))
print("Lowest Marks:",np.min(marks))
print("Average:",np.mean(marks))

print("median:",np.median(marks))
print("Standard Deviation:",np.std(marks))
print("Sort:",np.sort(marks))
print("Argmax:",np.argmax(marks))
print("ArgMin:",np.argmin(marks))
#Boolean mask for scoring above 60
above_60=marks>60
print("marks above 60:",marks[above_60])
#Boolean mask for scoring below 50
below_50=marks<50
print("marks below 50:",marks[below_50])
marks1=marks+5
print("Marks after 5 grace:",marks1)

#eligible_customers = customers[customers["Salary"] > 50000]


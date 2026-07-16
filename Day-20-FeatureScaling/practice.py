import pandas as pd

students = pd.DataFrame({
    "Hours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 80, 90, 100]
})

print(students)

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_scaled=scaler.fit_transform(students)
print(x_scaled)
scaled_df=pd.DataFrame(
    x_scaled,
    columns=students.columns
)
print(scaled_df.describe())

from sklearn.preprocessing import StandardScaler
standardscaler=StandardScaler()
x_scaled1=standardscaler.fit_transform(students)
print(x_scaled1)
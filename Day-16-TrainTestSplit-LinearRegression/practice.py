import pandas as pd
employees = pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [
        30000,
        38000,
        45000,
        52000,
        60000,
        68000,
        75000,
        83000,
        90000,
        100000
    ]
})

X=employees[["Experience"]]
y=employees["Salary"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42
)
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

print("Weight:",model.coef_)
print("Intercept:",model.intercept_)

predictions=model.predict(X_test)
print("Predictions:")
print(predictions)

print("Actual Values")
print(y_test)

new_employee=pd.DataFrame({
    "Experience":[6.5]
})

predict_salary=model.predict(new_employee)
print("Predicted Salary:",predict_salary[0])

import matplotlib.pyplot as plt
plt.scatter(employees["Salary"],model.predict(employees[["Experience"]]))
plt.title("Experience Vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
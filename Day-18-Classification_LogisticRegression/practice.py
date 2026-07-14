import pandas as pd
students=pd.DataFrame({
    "Hours":[1, 2, 2.5, 3, 3.5,
        4, 4.5, 5, 5.5, 6,
        6.5, 7, 7.5, 8, 8.5,
        9, 9.5, 10, 4.8, 6.8
    ],
    "Attendance":[
        50, 55, 60, 58, 65,
        68, 70, 75, 72, 80,
        78, 85, 82, 90, 88,
        92, 95, 98, 73, 84
    ],
    "Result":[
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
})
print(students)

X=students[["Hours","Attendance"]]
y=students["Result"]

print(X.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Predictions:")
print(predictions)
print("Actual:")
print(y_test)

# See the probabilitites
probabilities=model.predict_proba(X_test)[:,1]
print(probabilities)

new_student=pd.DataFrame({
    "Hours":[5.5],
    "Attendance":[78]
})
prediction=model.predict(new_student)
print("Prediction:",prediction[0])

if prediction[0]==1:
    print("Pass")
else:
    print("Fail")

print("Weights:",model.coef_)
print(model.coef_[0])
print("Bias:",model.intercept_)


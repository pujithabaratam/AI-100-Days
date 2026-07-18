import pandas as pd
students=pd.DataFrame({
    "Hours":[2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95],
    "Result":[0,0,0,1,1,1,1,1]
})
print(students)

X=students[["Hours","Attendance"]]
y=students["Result"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(random_state=42)
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print(predictions)

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

print("Accuracy:",accuracy_score(y_test,predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print("Feature Importance")
print(model.feature_importances_)

model1=DecisionTreeClassifier(max_depth=1,random_state=42)
model2=DecisionTreeClassifier(max_depth=5,random_state=42)
model1.fit(X_train,y_train)
train_predictions=model1.predict(X_train)
test_predictions=model1.predict(X_test)
print("Training Accuracy:",accuracy_score(y_train,train_predictions))
print("Testing Accuracy:",accuracy_score(y_test,test_predictions))

print("-------------------------")

model2.fit(X_train,y_train)
train_predictions1=model2.predict(X_train)
test_predictions1=model2.predict(X_test)
print("Training Accuracy:",accuracy_score(y_train,train_predictions1))
print("Testing Accuracy:",accuracy_score(y_test,test_predictions1))


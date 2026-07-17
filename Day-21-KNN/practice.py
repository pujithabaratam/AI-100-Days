import pandas as pd
students=pd.DataFrame({
    "Hours":[2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95],
    "Result":[0,0,0,1,1,1,1,1]
})
print(students)

# task 1: Split the data into training and testing sets.
X=students[["Hours","Attendance"]]
y=students["Result"]
print(X.shape)
print(y.shape)
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

# task2: Apply StandardScaler()
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
# Training - fit_transform()
X_train_scaled=scaler.fit_transform(X_train)
# Testing - transform()
X_test_scaled=scaler.transform(X_test)

# task3: Train the model
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train_scaled,y_train)

# task4: predict
predictions=model.predict(X_test_scaled)
print(predictions)

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)
print("Accuracy:",accuracy_score(y_test,predictions))
print("Confusion Matrix:")
print(confusion_matrix(y_test,predictions))
print("Classification Report:")
print(classification_report(y_test,predictions))

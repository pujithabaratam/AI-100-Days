import pandas as pd

students = pd.DataFrame({
    "Hours": [
        1, 2, 2.5, 3, 3.5,
        4, 4.5, 5, 5.5, 6,
        6.5, 7, 7.5, 8, 8.5,
        9, 9.5, 10, 4.8, 6.8
    ],

    "Attendance": [
        50, 55, 60, 58, 65,
        68, 70, 75, 72, 80,
        78, 85, 82, 90, 88,
        92, 95, 98, 73, 84
    ],

    "Result": [
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
})

X=students[["Hours","Attendance"]]
y=students["Result"]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42,stratify=y)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)

print("Actual:")
print(y_test.values)

print("Predictions:")
print(predictions)

from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    classification_report
)

cm=confusion_matrix(y_test,predictions)
print("\n Confusion Matrix")

tn,fp,fn,tp=cm.ravel()
print("\nTN:",tn)
print("FP:",fp)
print("FN:",fn)
print("TP:",tp)

accuracy=accuracy_score(y_test,predictions)
precision=precision_score(y_test,predictions)
recall=recall_score(y_test,predictions)
f1=f1_score(y_test,predictions)

print("\nAccuracy:",accuracy)
print("Precision:",precision)
print("Recall:",recall)
print("F1 Score:",f1)

print("\n Classification Report")
print(classification_report(y_test,predictions))

from sklearn.metrics import roc_curve
probabilities=model.predict_proba(X_test)[:,1]
fpr,tpr,thresholds=roc_curve(y_test,probabilities)

# import matplotlib.pyplot as plt
# plt.plot(fpr,tpr)
# plt.xlabel("False Positive Rate")
# plt.ylabel("True Posititve Rate")

# plt.title("ROC Curve")
# plt.show()

from sklearn.metrics import roc_auc_score
auc=roc_auc_score(y_test,probabilities)
print("ROC-AUC:",auc)

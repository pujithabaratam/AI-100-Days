import pandas as pd
students=pd.DataFrame({
    "Hours":[2,3,4,5,6,7,8,9],
    "Attendance":[60,65,70,75,80,85,90,95],
    "Result":[0,0,0,1,1,1,1,1]
})
X=students[["Hours","Attendance"]]
y=students["Result"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

# AdaBoost
# from sklearn.ensemble import AdaBoostClassifier
# model=AdaBoostClassifier(
#     n_estimators=50,
#     random_state=42
# )
# model.fit(X_train,y_train)
# predictions=model.predict(X_test)
# print(model.score(X_test,y_test))

# Gradient Boosting
# from sklearn.ensemble import GradientBoostingClassifier
# model=GradientBoostingClassifier(
#     n_estimators=100,
#     learning_rate=0.1,
#     random_state=42
# )
# model.fit(X_train,y_train)
# predictions=model.predict(X_test)
# print(model.score(X_test,y_test))

# XGBoost
from xgboost import XGBClassifier
model=XGBClassifier(random_state=42)
model.fit(X_train,y_train)
predictions=model.predict(X_test)

# LightGBM
from lightgbm import LGBMClassifier
model=LGBMClassifier()
model.fit(X_train,y_train)
predictions=model.predict(X_test)

# CatBoost
from catboost import CatBoostClassifier
model=CatBoostClassifier(verbose=0)
model.fit(X_train,y_train)
predictions=model.predict(X_test)


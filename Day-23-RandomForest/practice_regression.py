from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

X,y=fetch_california_housing(return_X_y=True)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestRegressor(n_estimators=100,random_state=42)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

rmse=mean_squared_error(y_test,y_pred) ** 0.5
print("RMSE:",rmse)


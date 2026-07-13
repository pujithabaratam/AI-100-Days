import pandas as pd
employees= pd.DataFrame({
    "Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "SkillScore": [50, 55, 60, 65, 70, 75, 80, 85, 90, 95],
    "Salary": [
        30000,
        38000,
        45000,
        53000,
        60000,
        68000,
        76000,
        83000,
        91000,
        100000
    ]
})

# Features
X=employees[["Experience","SkillScore"]]

# Target
y=employees["Salary"]

print(X.shape)
print(y.shape)

# Train the model
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)

print("Weights:",model.coef_)
print("Bias:",model.intercept_)

predictions=model.predict(X_test)
print("Predictions:")
print(predictions)
print("Actual values:")
print(y_test)

# Regression Evaluation Metrics
# Mean Absolute Error
from sklearn.metrics import mean_absolute_error
mae=mean_absolute_error(y_test,predictions)
print("MAE:".mae)

# Mean Squared Error
from sklearn.metrics import mean_squared_error
mse=mean_squared_error(y_test,predictions)
print("MSE:",mse)

# Root Mean Squared Error - To overcome the problem in RMSE
import numpy as np
rmse=np.sqrt(mse)
print("RMSE:",rmse)

# R2 Score
from sklearn.metrics import r2_score
r2=r2_score(y_test,predictions)
print("R2 Score:",r2)


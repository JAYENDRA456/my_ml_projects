import numpy as np
from sklearn.linear_model import LinearRegression
hours_studied= np.array([1,2,3,4,5]).reshape(-1,1)
marks=np.array([20,30,40,50,60])
model=LinearRegression()
model.fit(hours_studied,marks)
prediction=model.predict(np.array([[6]]))
print("prediction marks:",prediction[0])



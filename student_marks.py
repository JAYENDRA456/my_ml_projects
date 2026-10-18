import numpy as np
from sklearn.linear_model import LinearRegression
hours= np.array([1,2,3,4,5]).reshape(-1,1)
marks=np.array([20,30,40,50,60])
model=LinearRegression()
model.fit(hours,marks)
#feature 1
study_hours=6
prediction=model.predict([[study_hours]])
print("prediction marks:",prediction[0])
#feature 2
score=model.score(hours,marks)
print(" model R-squared score:",score)




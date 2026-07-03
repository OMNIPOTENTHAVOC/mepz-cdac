import numpy as np
import matplotlib.pyplot as plt

class LinearRegression:
    def __init__(self):
        self.coeff= None
        self.incpt= None
        
    def fit(self, x, y):
        n = len(x)
        x_b = np.c_[np.ones((n,1)), x]  
   
        self.coeff = np.linalg.inv(x_b.T.dot(x_b)).dot(x_b.T).dot(y)
        self.incpt= self.coeff[0]
        y_pred = x_b.dot(self.coeff)
        self.y_pred= y_pred
        
    def predict(self, x):
        x_b = np.c_[np.ones((len(x),1)), x]
        return x_b.dot(self.coeff)
    
    def show(self, x, y):
        print(f"Coefficients: {model.coeff}")
        print(f"Intercept: {model.incpt}")

x= np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y= np.array([2,4,5,4,5,7,8,9,10,12])
print(x, y)

model = LinearRegression()
model.fit(x, y)
res1= model.predict([7])
print("res1: ",res1, "\n")
res2= model.predict([12])
print("res2: ", res2, "\n")
model.show(x, y)

plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, model.y_pred, color='red', label='Regression Line')
plt.title("Linear Regression")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
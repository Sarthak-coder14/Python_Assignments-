import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def MarvellousPredictor():
    Border = "-" * 40
    
    print(Border)
    print("Load Dataset")
    print(Border)

    X = np.array([1,2,3,4,5]).reshape(-1,1)
    Y = np.array([20000,25000,30000,35000,40000])

    print("Values of Independent variables : X - ",X)
    print("Values of Dependent variables : Y - ",Y)

    model = LinearRegression()
    model.fit(X,Y)

    dataset_pred = model.predict(X)


    Y_pred = model.predict(np.array([[6]]))


    print("Predicted Salary for 6 Years Experience : ",Y_pred)

    plt.scatter(X, Y)          
    plt.plot(X, dataset_pred)        

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Salary vs Experience")

    plt.show()

plt.show()


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()
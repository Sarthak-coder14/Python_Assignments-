import math

def MarvellousKNeighborsClassifier():
    Border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    n = len(X) 
    new_pred = 6

    print(Border)
    print("Dataset")
    print(Border)
    print("X :",X)
    print("Y :",Y)

    print(Border)
    print("Mean Calculation")
    print(Border)

    X_mean = sum(X)/n
    
    Y_mean = sum(Y)/n

    print("Mean of X is : ",X_mean)
    print("Mean of Y is : ",Y_mean)

    print(Border)
    print("Slope calculation")
    print(Border)
    
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean)**2)

    m = numerator / denominator

    print("Slope of line ie m : ",m)

    print(Border)
    print("Intercept calculation")
    print(Border)

    intercept = Y_mean - (m * X_mean)

    print("intercept is : ",intercept)

    print(Border)
    print(" Prediction")
    print(Border)
    YP = 0

    Y_pred = m * new_pred + intercept
    print("For X =",new_pred)
    print("Predicted Y :",Y_pred)
    
def main():
    MarvellousKNeighborsClassifier()
    

if __name__ == "__main__":
    main()
import math

def MarvellousKNeighborsClassifier():
    Border = "-"*40

    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    n = len(X) 
    new_pred = 6

    print(Border)
    print("Dataset")
    print("X :",X)
    print("Y :",Y)

    print(Border)
    print("Mean Calculation")
    

    X_mean = sum(X)/n
    
    Y_mean = sum(Y)/n

    print("Mean of X is : ",X_mean)
    print("Mean of Y is : ",Y_mean)

    print(Border)
    print("Slope calculation")

    
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - X_mean) * (Y[i] - Y_mean))
        denominator = denominator + ((X[i] - X_mean)**2)

    m = numerator / denominator

    print("Slope of line ie m : ",m)

    print(Border)
    print("Intercept calculation")


    intercept = Y_mean - (m * X_mean)

    print("intercept is : ",intercept)

    print(Border)
    print(" Prediction")

    YP = 0
    
    Y_pred = []

    for i in X:
        value = m * i + intercept
        Y_pred.append(value)
    
    print("Predicted Y values : ",Y_pred)
    print(Border)
    print("Mean Squared Error Calculation")
 
    MSE = 0

    for i in range(n):
        error = (( Y_pred[i] - Y[i] )**2) 
        MSE = MSE + error
    R2 = MSE
    MSE = MSE / n

    print("MSE : ",MSE)
    print(Border)
    print("r2_score Calculation")

    num = R2
    deno = 0

    for i in range(n):
        deno = deno + (Y[i] - Y_mean)**2

    r2_score = 1 - (num / deno)

    print("r2_score is : ",r2_score)

    
def main():
    MarvellousKNeighborsClassifier()
    

if __name__ == "__main__":
    main()
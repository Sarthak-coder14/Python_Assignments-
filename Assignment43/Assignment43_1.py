import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler, LabelEncoder


def CheckAccuracy(X,Y):

    Border = "-"*40

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    for k in range(1,11):

        print(Border)
        print("Value of K :",k)

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test,Y_pred)

        print("Accuracy :",accuracy)


def main():

    Border = "-"*40

    #-------------------------------------
    # Step 1 : Load the Dataset from CSV file
    #-------------------------------------

    print(Border)
    print("Step 1 : Load the Dataset from CSV file")
    print(Border)

    df = pd.read_csv('PlayPredictor.csv')

    print(Border)
    print("Some entries from dataset")
    print(df.head())


    #-------------------------------------
    # Step 2 : Clean dataset
    #-------------------------------------

    print(Border)
    print("Step 2 : Clean dataset")
    print(Border)

    df.dropna(inplace=True)

    print("Total records :",df.shape[0])
    print("Total columns :",df.shape[1])


    #-------------------------------------
    # Step 3 : Remove unwanted columns
    #-------------------------------------

    print(Border)
    print("Step 3 : Remove unwanted columns")
    print(Border)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'],inplace=True)


    #-------------------------------------
    # Step 4 : Convert String to Numeric
    #-------------------------------------

    print(Border)
    print("Step 4 : Label Encoding")
    print(Border)

    le = LabelEncoder()

    df['Whether'] = le.fit_transform(df['Whether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    df['Play'] = le.fit_transform(df['Play'])

    print(df.head())


    #-------------------------------------
    # Step 5 : Separate input and output
    #-------------------------------------

    print(Border)
    print("Step 5 : Separate X and Y")
    print(Border)

    X = df.drop(columns=['Play'])
    Y = df['Play']

    print("Shape of X :",X.shape)
    print("Shape of Y :",Y.shape)


    #-------------------------------------
    # Step 6 : Split dataset
    #-------------------------------------

    print(Border)
    print("Step 6 : Train Test Split")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)


    #-------------------------------------
    # Step 7 : Feature Scaling
    #-------------------------------------

    print(Border)
    print("Step 7 : Feature Scaling")
    print(Border)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    #-------------------------------------
    # Step 8 : Train KNN Model
    #-------------------------------------

    print(Border)
    print("Step 8 : Train KNN Model (K=3)")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train_scaled,Y_train)

    Y_pred = model.predict(X_test_scaled)


    #-------------------------------------
    # Step 9 : Accuracy
    #-------------------------------------

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of model :",accuracy)

    print(Border)
    print("Confusion Matrix")
    print(confusion_matrix(Y_test,Y_pred))

    print(Border)
    print("Classification Report")
    print(classification_report(Y_test,Y_pred))


    #-------------------------------------
    # Step 10 : Check Accuracy for different K
    #-------------------------------------

    print(Border)
    print("Check Accuracy for different K values")
    print(Border)

    CheckAccuracy(X,Y)



if __name__ == "__main__":
    main()
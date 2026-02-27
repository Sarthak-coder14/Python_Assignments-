import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, ConfusionMatrixDisplay

Border = "-"*50

#########################################################
# Step 1 : Load the dataset
#########################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"

df = pd.read_csv(DatasetPath)

print("Dataset loaded successfully...")
print("Initial entries from dataset :")
print(df.head())


#########################################################
# Step 2 : Data Analysis (EDA)
#########################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Shape of dataset :", df.shape)
print("Column names :", list(df.columns))

print("\nMissing values per column :")
print(df.isnull().sum())

print("\nClass Distribution (Pass/Fail count)")
print(df["FinalResult"].value_counts())

print("\nStatistical report :")
print(df.describe())


#########################################################
# Step 3 : Decide Independent & Dependent variables
#########################################################

print(Border)
print("Step 3 : Independent & Dependent Variables")
print(Border)

feature_cols = [
    'StudyHours',
    'Attendance',
    'PreviousScore',
    'AssignmentsCompleted',
    'SleepHours'
]

X = df[feature_cols]
Y = df['FinalResult']

print("X shape :", X.shape)
print("Y shape :", Y.shape)


#########################################################
# Step 4 : Data Visualization
#########################################################

print(Border)
print("Step 4 : Data Visualization")
print(Border)

# Histogram
plt.figure()
plt.hist(df['StudyHours'], bins=10)
plt.title("Histogram of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure()

pass_students = df[df['FinalResult'] == 1]
fail_students = df[df['FinalResult'] == 0]

plt.scatter(pass_students['StudyHours'], pass_students['PreviousScore'], label="Pass")
plt.scatter(fail_students['StudyHours'], fail_students['PreviousScore'], label="Fail")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.title("StudyHours vs PreviousScore")
plt.legend()
plt.show()


#########################################################
# Step 5 : Split dataset into Training & Testing
#########################################################

print(Border)
print("Step 5 : Train-Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42
)

print("X_train :", X_train.shape)
print("X_test :", X_test.shape)
print("Y_train :", Y_train.shape)
print("Y_test :", Y_test.shape)


#########################################################
# Step 6 : Build the Model
#########################################################

print(Border)
print("Step 6 : Build Decision Tree Model")
print(Border)

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    random_state=42
)

print("Model created successfully :", model)


#########################################################
# Step 7 : Train the Model
#########################################################

print(Border)
print("Step 7 : Train the Model")
print(Border)

model.fit(X_train, Y_train)

print("Model training completed")


#########################################################
# Step 8 : Testing the Model
#########################################################

print(Border)
print("Step 8 : Testing the Model")
print(Border)

Y_pred = model.predict(X_test)

print("Predicted values :")
print(Y_pred[:10])


#########################################################
# Step 9 : Model Performance Evaluation
#########################################################

print(Border)
print("Step 9 : Model Performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of model :", accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)
print("\nConfusion Matrix :")
print(cm)

print("\nClassification Report :")
print(classification_report(Y_test, Y_pred))


#########################################################
# Step 10 : Plot Confusion Matrix
#########################################################

print(Border)
print("Step 10 : Plot Confusion Matrix")
print(Border)

disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix - Student Performance")
plt.show()


#########################################################
# Step 11 : Final Conclusion
#########################################################

print(Border)
print("Final Conclusion")
print(Border)

print("Decision Tree model trained and evaluated successfully.")
print("Accuracy and confusion matrix analysed.")
import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier, plot_tree

from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

Border = "-"*50

#########################################################
# Step 1 : Load the Dataset
#########################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DatasetPath = "student_performance_ml.csv"
data = pd.read_csv(DatasetPath)

print("Total Students :", len(data))
print("Dataset Shape :", data.shape)


#########################################################
# Step 2 : Basic Analysis
#########################################################

print(Border)
print("Step 2 : Basic Analysis")
print(Border)

print("Pass / Fail Count :")
print(data['FinalResult'].value_counts())


#########################################################
# Step 3 : Define Features & Target
#########################################################

print(Border)
print("Step 3 : Define Features & Target")
print(Border)

X = data[['StudyHours', 'Attendance', 'PreviousScore',
          'AssignmentsCompleted', 'SleepHours']]
y = data['FinalResult']

print("X shape :", X.shape)
print("Y shape :", y.shape)


#########################################################
# Step 4 : Train-Test Split
#########################################################

print(Border)
print("Step 4 : Train-Test Split")
print(Border)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

print("X_train :", X_train.shape)
print("X_test :", X_test.shape)
print("Y_train :", y_train.shape)
print("Y_test :", y_test.shape)


#########################################################
# Step 5 : Model Training
#########################################################

print(Border)
print("Step 5 : Model Training")
print(Border)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

print("Model Training Completed")


#########################################################
# Step 6 : Prediction & Accuracy
#########################################################

print(Border)
print("Step 6 : Prediction & Accuracy")
print(Border)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy :", accuracy*100)


#########################################################
# Step 7 : Confusion Matrix
#########################################################

print(Border)
print("Step 7 : Confusion Matrix")
print(Border)

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix :\n", cm)

ConfusionMatrixDisplay(cm).plot()
plt.show()


#########################################################
# Step 8 : Feature Importance
#########################################################

print(Border)
print("Step 8 : Feature Importance")
print(Border)

for feature, importance in zip(X.columns, model.feature_importances_):
    print(feature, ":", importance)


#########################################################
# Step 9 : Remove SleepHours Feature
#########################################################

print(Border)
print("Step 9 : Remove SleepHours")
print(Border)

X_no_sleep = data[['StudyHours', 'Attendance',
                   'PreviousScore', 'AssignmentsCompleted']]

X_train2, X_test2, y_train2, y_test2 = train_test_split(
    X_no_sleep, y, test_size=0.3, random_state=42)

model2 = DecisionTreeClassifier(random_state=42)
model2.fit(X_train2, y_train2)

acc2 = accuracy_score(y_test2, model2.predict(X_test2))
print("Accuracy without SleepHours :", acc2*100)


#########################################################
# Step 10 : Only Two Features
#########################################################

print(Border)
print("Step 10 : Only StudyHours & Attendance")
print(Border)

X_small = data[['StudyHours', 'Attendance']]

X_train3, X_test3, y_train3, y_test3 = train_test_split(
    X_small, y, test_size=0.3, random_state=42)

model3 = DecisionTreeClassifier(random_state=42)
model3.fit(X_train3, y_train3)

acc3 = accuracy_score(y_test3, model3.predict(X_test3))
print("Accuracy with 2 Features :", acc3*100)


#########################################################
# Step 11 : Manual Accuracy
#########################################################

print(Border)
print("Step 11 : Manual Accuracy")
print(Border)

correct = sum(y_test.values == y_pred)
manual_acc = correct / len(y_test)

print("Manual Accuracy :", manual_acc*100)


#########################################################
# Step 12 : Misclassified Students
#########################################################

print(Border)
print("Step 12 : Misclassified Students")
print(Border)

misclassified = X_test[y_test != y_pred]

print(misclassified)
print("Total Misclassified :", len(misclassified))


#########################################################
# Step 13 : Random State Check
#########################################################

print(Border)
print("Step 13 : Random State Check")
print(Border)

for state in [0, 10, 42]:
    temp_model = DecisionTreeClassifier(random_state=state)
    temp_model.fit(X_train, y_train)
    temp_acc = accuracy_score(y_test,
                              temp_model.predict(X_test))
    print(f"Random State {state} Accuracy :", temp_acc*100)


#########################################################
# Step 14 : Tree Visualization
#########################################################

print(Border)
print("Step 14 : Tree Visualization")
print(Border)

plt.figure(figsize=(12,8))
plot_tree(model,
          feature_names=X.columns,
          class_names=['Fail','Pass'],
          filled=True)
plt.show()


#########################################################
# Step 15 : Add New Feature (PerformanceIndex)
#########################################################

print(Border)
print("Step 15 : Add PerformanceIndex")
print(Border)

data['PerformanceIndex'] = (data['StudyHours']*2) + data['Attendance']

X_new = data[['StudyHours', 'Attendance',
              'PreviousScore', 'AssignmentsCompleted',
              'SleepHours', 'PerformanceIndex']]

X_train4, X_test4, y_train4, y_test4 = train_test_split(
    X_new, y, test_size=0.3, random_state=42)

model4 = DecisionTreeClassifier(random_state=42)
model4.fit(X_train4, y_train4)

acc4 = accuracy_score(y_test4,
                      model4.predict(X_test4))

print("Accuracy with PerformanceIndex :", acc4*100)


#########################################################
# Step 16 : Overfitting Check
#########################################################

print(Border)
print("Step 16 : Overfitting Check")
print(Border)

deep_model = DecisionTreeClassifier(
    max_depth=None, random_state=42)

deep_model.fit(X_train, y_train)

train_acc = accuracy_score(
    y_train, deep_model.predict(X_train))

test_acc = accuracy_score(
    y_test, deep_model.predict(X_test))

print("Training Accuracy :", train_acc*100)
print("Testing Accuracy :", test_acc*100)

print("\nProgram Completed Successfully.")
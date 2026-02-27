import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*40

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
print("Step 2 : Data analysis")
print(Border)

print("Shape of dataset : ", df.shape)
print("Column Names : ", list(df.columns))

print("\nMissing values (Per Column)")
print(df.isnull().sum())

print("\nPass / Fail Count")
print(df["FinalResult"].value_counts())

print("\nStatistical Report of dataset")
print(df.describe())

#########################################################
# Step 3 : Statistical Observations
#########################################################

print(Border)
print("Step 3 : Statistical Observations")
print(Border)

print("Average StudyHours :", df['StudyHours'].mean())
print("Average Attendance :", df['Attendance'].mean())
print("Maximum PreviousScore :", df['PreviousScore'].max())
print("Minimum SleepHours :", df['SleepHours'].min())

#########################################################
# Step 4 : Visualisation of dataset
#########################################################

print(Border)
print("Step 4 : Visualisation of dataset")
print(Border)

# Histogram of StudyHours
plt.figure()
plt.hist(df['StudyHours'], bins=10)
plt.title("Histogram of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot : StudyHours vs PreviousScore
plt.figure()

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    plt.scatter(temp["StudyHours"],
                temp["PreviousScore"],
                label=result)

plt.title("StudyHours vs PreviousScore")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.legend()
plt.grid(True)
plt.show()

# Boxplot for Attendance
plt.figure()
plt.boxplot(df["Attendance"])
plt.title("Boxplot of Attendance")
plt.ylabel("Attendance")
plt.show()

# AssignmentsCompleted vs FinalResult
plt.figure()
plt.scatter(df["AssignmentsCompleted"],
            df["FinalResult"])

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.grid(True)
plt.show()

# SleepHours vs FinalResult
plt.figure()
plt.scatter(df["SleepHours"],
            df["FinalResult"])

plt.title("SleepHours vs FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.grid(True)
plt.show()

#########################################################
# Step 5 : Observations
#########################################################

print(Border)
print("Step 5 : Final Observations")
print(Border)

print("Students with higher StudyHours and Attendance")
print("generally show better performance.")
print("SleepHours alone does not guarantee success.")
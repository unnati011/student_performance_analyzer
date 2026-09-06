import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STUDENT PERFORMANCE & RESULT ANALYZER
# ==========================================

print("==========================================")
print("     STUDENT PERFORMANCE ANALYZER")
print("==========================================")

# Read data from CSV file
df = pd.read_csv("student.csv")

print("\nStudent data loaded successfully!\n")
print(df)


# ==========================================
# SUBJECTS
# ==========================================

subjects = [
    "Python",
    "Data_Structures",
    "Database",
    "Operating_System",
    "Computer_Network"
]


# ==========================================
# CALCULATE TOTAL MARKS
# ==========================================

df["Total"] = df[subjects].sum(axis=1)


# ==========================================
# CALCULATE PERCENTAGE
# ==========================================

df["Percentage"] = (df["Total"] / 500) * 100


# ==========================================
# CALCULATE GRADE
# ==========================================

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


df["Grade"] = df["Percentage"].apply(calculate_grade)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n==========================================")
print("             STUDENT RESULTS")
print("==========================================")

print(
    df[["Name", "Total", "Percentage", "Grade"]]
    .to_string(index=False)
)


# ==========================================
# CLASS AVERAGE
# ==========================================

class_average = df["Percentage"].mean()

print("\nClass Average:",
      round(class_average, 2), "%")


# ==========================================
# TOP PERFORMER
# ==========================================

top_student = df.loc[df["Percentage"].idxmax()]

print("\nTop Performer:",
      top_student["Name"])

print("Top Percentage:",
      round(top_student["Percentage"], 2), "%")


# ==========================================
# LOWEST PERFORMER
# ==========================================

lowest_student = df.loc[df["Percentage"].idxmin()]

print("\nLowest Performer:",
      lowest_student["Name"])

print("Lowest Percentage:",
      round(lowest_student["Percentage"], 2), "%")


# ==========================================
# STUDENTS NEEDING IMPROVEMENT
# ==========================================

print("\n==========================================")
print("       STUDENTS NEEDING IMPROVEMENT")
print("==========================================")

improvement = df[df["Percentage"] < 60]

if improvement.empty:

    print("No students need improvement.")

else:

    print(
        improvement[["Name", "Percentage"]]
        .to_string(index=False)
    )


# ==========================================
# SUBJECT-WISE AVERAGE
# ==========================================

print("\n==========================================")
print("          SUBJECT-WISE AVERAGE")
print("==========================================")

subject_average = df[subjects].mean()

for subject, average in subject_average.items():

    print(subject, ":", round(average, 2))


# ==========================================
# SAVE RESULTS
# ==========================================

df.to_csv("student_results.csv", index=False)

print("\nResults saved successfully!")
print("File created: student_results.csv")


# ==========================================
# GRAPH 1 - STUDENT PERFORMANCE
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    df["Name"],
    df["Percentage"]
)

plt.xlabel("Students")
plt.ylabel("Percentage")

plt.title("Student Performance")

plt.ylim(0, 100)

plt.show()


# ==========================================
# GRAPH 2 - SUBJECT PERFORMANCE
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    subject_average.index,
    subject_average.values
)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")

plt.title("Subject-wise Class Performance")

plt.xticks(rotation=30)

plt.ylim(0, 100)

plt.show()


# ==========================================
# COMPLETED
# ==========================================

print("\n==========================================")
print("          ANALYSIS COMPLETED")
print("==========================================")
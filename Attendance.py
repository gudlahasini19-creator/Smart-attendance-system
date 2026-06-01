import pandas as pd
from datetime import datetime

# Read student data
data = pd.read_csv("students.csv")

# Take input from user
present_students = input(
    "Enter present student names separated by comma: "
)

# Convert input into a clean list
present_list = list(set(
    name.strip().lower()
    for name in present_students.split(",")
))

# Get all student names from CSV
student_names = data["Name"].str.lower().tolist()

# Check for invalid names
invalid_names = [
    name for name in present_list
    if name not in student_names
]

# Mark attendance
data["Attendance"] = data["Name"].apply(
    lambda x: "Present"
    if x.lower() in present_list
    else "Absent"
)

# Calculate attendance statistics
present_count = (
    data["Attendance"] == "Present"
).sum()

total_students = len(data)

attendance_percentage = (
    present_count / total_students
) * 100

# Current date and time
current_time = datetime.now()

# Display report
print("\n" + "=" * 40)
print("SMART ATTENDANCE REPORT")
print("=" * 40)

print(data)

print(f"\nDate & Time: {current_time}")

print(f"\nTotal Students: {total_students}")

print(f"Present Students: {present_count}")

print(
    f"Attendance Percentage: "
    f"{attendance_percentage:.2f}%"
)

# Show invalid names if any
if invalid_names:
    print(
        "\nInvalid Student Names:",
        ", ".join(invalid_names)
    )

# Save updated attendance file
data.to_csv(
    "updated_attendance.csv",
    index=False
)

print(
    "\nAttendance saved successfully "
    "to 'updated_attendance.csv'!"
)
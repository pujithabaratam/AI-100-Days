import pandas as pd
students=pd.read_csv("dataset.csv")
students["Total"]=(
    students["Math"]+
    students["Science"]+
    students["English"]
)
students["Average"]=students["Total"]/3
Perf=[]
for avg in students["Average"]:
    if avg>=90:
        Perf.append("Excellent")
    elif avg>=80:
        Perf.append("Good")
    elif avg>=70:
        Perf.append("Average")
    else:
        Perf.append("Need Improvement")
students["Performance"]=Perf

# Top Performer
topper = students.nlargest(1, "Average")

# Lowest Performer
lowest = students.nsmallest(1, "Average")

# Best Performing City
city_avg = students.groupby("City")["Average"].mean()

# Best Subject
subject_avg = students[["Math", "Science", "English"]].mean()

# Students by City
city_count = students["City"].value_counts()

# Performance Summary
performance_summary = students["Performance"].value_counts()

# Students Below Average Attendance
avg_attendance = students["Attendance"].mean()
below_avg = students[students["Attendance"] < avg_attendance]

with open("report.txt", "w") as file:

    file.write("=" * 50 + "\n")
    file.write("          STUDENT PERFORMANCE REPORT\n")
    file.write("=" * 50 + "\n\n")

    file.write(f"Total Students           : {len(students)}\n")
    file.write(f"Overall Average Marks    : {students['Average'].mean():.2f}\n")
    file.write(f"Average Attendance       : {avg_attendance:.2f}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Top Performer\n")
    file.write("-" * 50 + "\n")
    file.write(f"Name                     : {topper['Name'].iloc[0]}\n")
    file.write(f"Average Marks            : {topper['Average'].iloc[0]:.2f}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Lowest Performer\n")
    file.write("-" * 50 + "\n")
    file.write(f"Name                     : {lowest['Name'].iloc[0]}\n")
    file.write(f"Average Marks            : {lowest['Average'].iloc[0]:.2f}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Best Performing City\n")
    file.write("-" * 50 + "\n")
    file.write(f"{city_avg.idxmax()}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Best Subject\n")
    file.write("-" * 50 + "\n")
    file.write(f"{subject_avg.idxmax()}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Attendance Statistics\n")
    file.write("-" * 50 + "\n")
    file.write(f"Highest Attendance       : {students['Attendance'].max()}\n")
    file.write(f"Lowest Attendance        : {students['Attendance'].min()}\n")
    file.write(f"Average Attendance       : {avg_attendance:.2f}\n\n")

    file.write("-" * 50 + "\n")
    file.write("Students by City\n")
    file.write("-" * 50 + "\n")
    for city, count in city_count.items():
        file.write(f"{city:<25}: {count}\n")
    file.write("\n")

    file.write("-" * 50 + "\n")
    file.write("Performance Summary\n")
    file.write("-" * 50 + "\n")
    for category, count in performance_summary.items():
        file.write(f"{category:<25}: {count}\n")
    file.write("\n")

    file.write("-" * 50 + "\n")
    file.write("Students Below Average Attendance\n")
    file.write("-" * 50 + "\n")
    for _, row in below_avg.iterrows():
        file.write(f"{row['Name']:<25}: {row['Attendance']}\n")
    file.write("\n")

    file.write("-" * 50 + "\n")
    file.write("Key Insights\n")
    file.write("-" * 50 + "\n")
    file.write(f"• {topper['Name'].iloc[0]} is the top performer.\n")
    file.write(f"• {lowest['Name'].iloc[0]} needs improvement.\n")
    file.write(f"• {city_avg.idxmax()} has the highest average marks.\n")
    file.write(f"• {subject_avg.idxmax()} is the highest scoring subject.\n")
    file.write(f"• Average attendance is {avg_attendance:.2f}%.\n")
    file.write(f"• Most students belong to the '{performance_summary.idxmax()}' category.\n\n")

    file.write("=" * 50 + "\n")
    file.write("               END OF REPORT\n")
    file.write("=" * 50)

print("Report generated successfully!")
print("Report saved as report.txt")
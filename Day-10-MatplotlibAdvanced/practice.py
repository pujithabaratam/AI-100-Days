import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May"]
sales = [100,120,150,180,210]

# Task1: Create a Line Chart
plt.plot(months,sales)
plt.title("Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# Task2: Change color, marker, linestyle, linewidth
# Task 3: Increase Fig Size
plt.figure(figsize=(6,5))
plt.plot(
    months,
    sales,
    color="pink",
    marker="*",
    linestyle="--",
    linewidth=2,
    label="Sales"
)


# Task4: Add Title,xlabel,ylabel,grid,legend
plt.title("Enhanced Line Chart")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("Sales_chart.png")
plt.show()

# Task 6: Create Line Chart, Bar Chart using subplot()
plt.figure(figsize=(6,6))
plt.subplot(3,3,1)
plt.plot(months,sales)
plt.subplot(3,3,2)
plt.bar(months,sales)
plt.show()


# Day-10 Matplotlib Advanced
# Changing Figure Size
By default, charts have a standard size
we can customize it
plt.figure(figSize=(8,5))
8-> width
5-> Height
This is useful when you have many labels or large datasets.

# Changing colour
plt.plot(months,sales,color="red")

# LineStyle
plt.plot(months,sales,linestyle="--")
"-"   Solid
"--"  Dashed
":"   Dotted
"-."  Dash-dot

# Marker
plt.plot(months,sales,marker="o")
o   Circle
s   Square
^   Triangle
*   Star
x   Cross

# Line Width
Makes the line thicker or thinner
plt.plot(months, sales, linewidth=3)

# Combining Everything
plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linestyle="--",
    linewidth=2,
    label="Sales"
)

# Saving a chart
This saves the chart in your project folder.
Very useful for reports and dashboards.
plt.savefig("sales_chart.png")

# Subplots
Display multiple charts in one figure
subplot(rows,columns,position)

plt.subplot(1,2,1)
plt.plot(months,sales)

plt.subplot(1,2,2)
plt.bar(months,sales)

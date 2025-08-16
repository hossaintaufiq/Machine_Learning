# import matplotlib.pyplot as plt
# # %matplotlib notebook

# months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# sales= [200, 300, 250, 400, 350]

# plt.plot(months, sales ,color='blue', linestyle='--' , linewidth=2, marker='o', markersize='5', label='Sales Data')

# plt.title('Monthly Sales Data')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.show()
# plt.savefig('monthly_sales_plot.png')  # Save the plot as a PNG file
# print("Plot saved as 'monthly_sales_plot.png'")


# new version 
import matplotlib.pyplot as plt
import mplcursors

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales= [200, 300, 250, 400, 350]

plt.plot(months, sales ,color='blue', linestyle='--' , linewidth=2, marker='o', markersize='5', label='Sales Data')

plt.title('Monthly Sales Data')
plt.xlabel('Months')
plt.ylabel('Sales')

# Add hover tooltips
cursor = mplcursors.cursor(hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(
    f"{months[sel.index]}: {sales[sel.index]}"
))

plt.show()

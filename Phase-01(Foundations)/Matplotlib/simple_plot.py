# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(0, 2 * np.pi, 200)
# y = np.cos(x)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()                           # Show the figure.
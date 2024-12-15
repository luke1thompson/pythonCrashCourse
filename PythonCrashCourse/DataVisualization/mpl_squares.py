import matplotlib.pyplot as plt

inputs = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('bmh')
fig, ax = plt.subplots()
ax.plot(inputs, squares, linewidth=3)

# Lable the chart title and axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)

plt.show()
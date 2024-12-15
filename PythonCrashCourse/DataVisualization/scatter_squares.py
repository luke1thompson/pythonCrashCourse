import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.Reds, s=10)

# Lable the chart title and axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(labelsize=14)


ax.axis([0, 1100, 0, 1100000])
# ax.ticklabel_format(style='plain')

plt.savefig('./savedplots/squaresred.png', bbox_inches='tight')
# plt.show()
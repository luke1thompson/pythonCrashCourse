import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Generate a random walk
mywalk = RandomWalk(50_000)
mywalk.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(mywalk.x_values, mywalk.y_values, linewidth=1)
ax.set_aspect('equal')

# Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=150)
ax.scatter(mywalk.x_values[-1], mywalk.y_values[-1], c='red', edgecolors='none',
            s=150)

# remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
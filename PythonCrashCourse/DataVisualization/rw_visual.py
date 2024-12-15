import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    # Generate a random walk
    mywalk = RandomWalk(500)
    mywalk.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(mywalk.num_points)
    ax.scatter(mywalk.x_values, mywalk.y_values, c=point_numbers,
               cmap=plt.cm.cool, edgecolors='none', s=10)
    ax.set_aspect('equal')
    
    # Emphasize the first and last points
    ax.scatter(0, 0, c='white', s=100)
    ax.scatter(mywalk.x_values[-1], mywalk.y_values[-1], c='black',
               s=100)
    
    # remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    # break

    keep_running = input("Enter 'y' for more graphs: ")
    if keep_running != 'y':
        break
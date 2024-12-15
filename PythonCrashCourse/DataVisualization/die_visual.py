import plotly.express as px

from die import Die

die1 = Die()
die2 = Die()
size = 50_000

# Generate a list of rolls
results = [die1.roll()*die2.roll() for num in range(size)]
# results = []
# for num in range(50_000):
#     results.append(die1.roll() * die2.roll())

# Create list of possible results
minimum = 1
maximum = die1.sides * die2.sides
poss_results = range(minimum, maximum + 1)
    
# Combine the rolls and possibilities into a frequency counter
frequencies = [results.count(value) for value in poss_results]
# frequencies = []
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# Visualize results
title = f"Rolling {size} times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Additional Customizations
fig.update_layout(xaxis_dtick=1)

# fig.write_html('./savedplots/d6plusd10.html')
fig.show()
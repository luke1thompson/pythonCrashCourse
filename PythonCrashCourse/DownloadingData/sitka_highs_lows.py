from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(date)
    highs.append(int(row[4]))
    lows.append(int(row[5]))

# dates = [datetime.strptime(row[2], '%Y-%m-%d') for row in reader]
# highs = [int(row[4]) for row in reader]

# Plot the high AND low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

# Formal plot
ax.set_title("Daily Temp Range: Sitka AK - 2021", fontsize=24)
ax.set_xlabel('', fontsize=21)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
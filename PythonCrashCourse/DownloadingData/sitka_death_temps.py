from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

path2 = Path('weather_data/sitka_weather_2021_simple.csv')
lines2 = path2.read_text(encoding='utf-8').splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

dates, highs, lows = [], [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)
        
dates2, highs2, lows2 = [], [], []
for row in reader2:
    date2 = datetime.strptime(row[2], '%Y-%m-%d')
    dates2.append(date2)
    highs2.append(int(row[4]))
    lows2.append(int(row[5]))

# Plot the high AND low temperatures
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='purple', alpha=0.1)

ax.plot(dates2, highs2, color='red', alpha=0.5)
ax.plot(dates2, lows2, color='blue', alpha=0.5)
ax.fill_between(dates2, highs2, lows2, facecolor='purple', alpha=0.1)

# Formal plot
title = "Daily Temperatures, 2021\nDeath Valley, CA and Sitka, AZ"
ax.set_title(title, fontsize=24)
# ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
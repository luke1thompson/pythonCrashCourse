from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

dates, rainfall = [], []
for row in reader:
    date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        rain = float(row[5])
    except ValueError:
        print(f"Value missing on {date}")
    else:
        dates.append(date)
        rainfall.append(rain)

# Plot rainfall
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, color='red', alpha=0.5)

# Formal plot
ax.set_title("Daily Rainfall, Sitka Alaska, 2021", fontsize=24)
# ax.set_xlabel('Date', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(labelsize=12)

plt.show()
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('counts.csv')

df = pd.DataFrame(data)
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
grouped = df.groupby(['Location', 'Weekday'])
group_dict = {key: group for key, group in grouped}
capacities = {'SquashBusters - 4th Floor' : 50, 'Marino Center - Studio A' : 33, 'Marino Center - Studio B' : 33, 'Marino Center - 2nd Floor' : 105, 'Marino Center - Gymnasium' : 60, 'Marino Center - 3rd Floor Weight Room' : 65, 'Marino Center - 3rd Floor Select & Cardio' : 90}

# For each room and weekday, create a plot
# for location, df in group_dict.items():
#     print(location)
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['Time'], df['Count'], marker='o', linestyle='-', label=location)
#     plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
#     plt.title(f"Count vs Time for {location}")
#     plt.ylim(0, capacities[location[0]])  # Set y-axis from 0 to 65 (adjust as needed)
#     plt.xlabel("Time")
#     plt.ylabel("Count")
#     plt.xticks(rotation=45)
#     plt.grid(True, linestyle='--', alpha=0.7)
#     plt.tight_layout()
#     plt.show()

def graph(location, day):
    df = group_dict[(location, day)]
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Count'], marker='o', linestyle='-', label=location)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
    plt.title(f"Count vs Time for {location}")
    plt.ylim(0, capacities[location])  # Set y-axis from 0 to 65 (adjust as needed)
    plt.xlabel("Time")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

graph("Marino Center - 3rd Floor Weight Room", "Saturday")
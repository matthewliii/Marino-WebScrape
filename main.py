import requests
from bs4 import BeautifulSoup
from lxml import html
import re
import datetime
import pandas as pd

# Making a GET request
r = requests.get('https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7', headers={"User-Agent": "XY"})

# check status code for response received
# success code - 200
print(r.status_code)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
text = soup.get_text().splitlines()
clean = []
dt = datetime.datetime.now()
data = {
    'Location' : [],
    'Count' : [],
    'Time' : [],
    'Weekday' : []
}
# Cleans the data
for s in text:
    if len(s) > 30 and (s[0] == 'M' or s[0] == 'S'):
        clean.append(s)
# Puts cleaned data into a json format
for i in clean:
    splList = re.split(r'L|U', i)
    location = splList[0].split("(")[0]
    count = splList[1].split(":")[1][1:]
    time = dt.strftime('%X')
    weekday = dt.strftime('%A')
    data['Location'].append(location)
    data['Count'].append(count)
    data['Time'].append(time)
    data['Weekday'].append(weekday)

df = pd.DataFrame(data)
df.to_csv('counts.csv', mode='a', index=False, header=False)

# 48 intervals of data collection? 1 interval is 30 minutes. ex: 1st interval is 12:30 am, 2nd 1:00am ... 35th interval 5:30pm
# or just store time of request ran. Probably use this one so that it is easier to graph. Store in a CSV with Location, Count, time of request, Day of the week?

# Max Capacities of each space (Calculated using last count/ percentage from website):
# SquashBusters - 4th Floor : 50
# Marino Center - Studio A : 33
# Marino Center - Studio B : 33
# Marino Center - 2nd Floor : 105
# Marino Center - Gymnasium : 60
# Marino Center - 3rd Floor Weight Room : 65
# Marino Center - 3rd Floor Select & Cardio : 90

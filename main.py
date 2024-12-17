import requests
from bs4 import BeautifulSoup
import re
import datetime
from zoneinfo import ZoneInfo
import pandas as pd

# Constants
URL = "https://connect2concepts.com/connect2/?type=circle&key=2A2BE0D8-DF10-4A48-BEDD-B3BC0CD628E7"
HEADERS = {"User-Agent": "XY"}
EASTERN = ZoneInfo("America/New_York")
CSV_FILE = "counts.csv"

# Max Capacities of each space (calculated using last count/percentage from the website):
# SquashBusters - 4th Floor: 50
# Marino Center - Studio A: 33
# Marino Center - Studio B: 33
# Marino Center - 2nd Floor: 105
# Marino Center - Gymnasium: 60
# Marino Center - 3rd Floor Weight Room: 65
# Marino Center - 3rd Floor Select & Cardio: 90

# Function to clean and extract data from the HTML content
def clean_data(text_lines):
    """
    Cleans and extracts location and count data from raw HTML text.
    """
    cleaned_lines = []
    for line in text_lines:
        if len(line) > 30 and (line.startswith('M') or line.startswith('S')):
            cleaned_lines.append(line)
    return cleaned_lines

# Function to parse cleaned data and create a structured dictionary
def parse_cleaned_data(cleaned_lines, current_datetime):
    """
    Parses cleaned lines and formats them into structured data.
    """
    data = {
        'Location': [],
        'Count': [],
        'Time': [],
        'Weekday': []
    }
    for line in cleaned_lines:
        split_list = re.split(r'L|U', line)
        location = split_list[0].split("(")[0].strip()
        count = split_list[1].split(":")[1].strip()
        time = current_datetime.strftime('%X')
        weekday = current_datetime.strftime('%A')

        data['Location'].append(location)
        data['Count'].append(count)
        data['Time'].append(time)
        data['Weekday'].append(weekday)
    return data

def main():
    # Step 1: Make a GET request to the target URL
    response = requests.get(URL, headers=HEADERS)

    # Check the response status
    if response.status_code != 200:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
        return

    # Step 2: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    raw_text = soup.get_text().splitlines()

    # Step 3: Clean and extract relevant data
    cleaned_lines = clean_data(raw_text)

    # Step 4: Parse cleaned data into a structured format
    current_datetime = datetime.datetime.now(EASTERN)
    structured_data = parse_cleaned_data(cleaned_lines, current_datetime)

    # Step 5: Convert structured data into a DataFrame and append to CSV
    df = pd.DataFrame(structured_data)
    df.to_csv(CSV_FILE, mode='a', index=False, header=False)
    print(f"Data successfully appended to {CSV_FILE}")

if __name__ == "__main__":
    main()

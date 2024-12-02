from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io
import re
import base64

app = Flask(__name__)

# Utility function to clean location input
def clean_location(location):
    # Remove unwanted spaces and ensure consistency
    location = location.strip()

    # Replace multiple spaces with a single space
    location = re.sub(r'\s+', ' ', location)

    return location


@app.route('/generate-graph', methods=['GET'])
def generate_graph():
    raw_location = request.args.get('location', "")
    raw_day = request.args.get('day', "")
    print(raw_location)
    # Decode and clean the location
    location = clean_location(raw_location)

    # Validate the day (example: ensure it's a weekday)
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = raw_day.strip()
    if day not in valid_days:
        return jsonify({"error": "Invalid day parameter"}), 400

    # Example: match cleaned location with your expected values
    expected_locations = ["Marino Center - 3rd Floor Weight Room", "Other Location"]
    if location not in expected_locations:
        return jsonify({"error": "Invalid location parameter"}), 400

    data = pd.read_csv('counts.csv')

    df = pd.DataFrame(data)
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    grouped = df.groupby(['Location', 'Weekday'])
    group_dict = {key: group for key, group in grouped}
    capacities = {'SquashBusters - 4th Floor' : 50, 'Marino Center - Studio A' : 33, 'Marino Center - Studio B' : 33, 'Marino Center - 2nd Floor' : 105, 'Marino Center - Gymnasium' : 60, 'Marino Center - 3rd Floor Weight Room' : 65, 'Marino Center - 3rd Floor Select & Cardio' : 90}

    df = group_dict[(location, day)]
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['Count'], marker='o', linestyle='-', label=location)
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%H:%M:%S'))
    plt.title(f"Count vs Time for {location}")
    plt.ylim(0, capacities[location])
    plt.xlabel("Time")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    # Encode the image to base64
    graph_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    print("Endpoint hit successfully")

    # Return the image as a base64 string
    return jsonify({"graph": graph_base64})

if __name__ == '__main__':
    app.run(debug=True)

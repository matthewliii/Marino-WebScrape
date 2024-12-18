from flask import Flask, request, jsonify
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import io
import re
import base64
from flask_cors import CORS

# Configure Matplotlib to work without a display
matplotlib.use('Agg')

# Initialize Flask app
app = Flask(__name__, static_folder='../build', static_url_path='/')
CORS(app)

# Utility function to clean location input
def clean_location(location):
    """Cleans and standardizes the location input."""
    location = location.strip()
    return re.sub(r'\s+', ' ', location)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route('/generate-graph', methods=['GET'])
def generate_graph():
    # Get and clean input parameters
    raw_location = request.args.get('location', "")
    raw_day = request.args.get('day', "")
    location = clean_location(raw_location)
    day = raw_day.strip()

    # Validate the day parameter
    valid_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day not in valid_days:
        return jsonify({"error": "Invalid day parameter"}), 400

    # Validate the location parameter
    expected_locations = [
        "SquashBusters - 4th Floor",
        "Marino Center - Studio A",
        "Marino Center - Studio B",
        "Marino Center - 2nd Floor",
        "Marino Center - Gymnasium",
        "Marino Center - 3rd Floor Weight Room",
        "Marino Center - 3rd Floor Select & Cardio"
    ]
    if location not in expected_locations:
        return jsonify({"error": "Invalid location parameter"}), 400

    # Load data and filter based on parameters
    try:
        data = pd.read_csv('counts.csv')
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 500

    df = pd.DataFrame(data)
    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')
    grouped = df.groupby(['Location', 'Weekday'])
    group_dict = {key: group for key, group in grouped}

    if (location, day) not in group_dict:
        return jsonify({"error": "No data available for the specified location and day"}), 404

    # Filter data and calculate rolling mean
    df = group_dict[(location, day)]
    df.sort_values('Time', inplace=True)
    capacities = {
        'SquashBusters - 4th Floor': 50,
        'Marino Center - Studio A': 33,
        'Marino Center - Studio B': 33,
        'Marino Center - 2nd Floor': 105,
        'Marino Center - Gymnasium': 60,
        'Marino Center - 3rd Floor Weight Room': 65,
        'Marino Center - 3rd Floor Select & Cardio': 90
    }

    df['SMA'] = df['Count'].rolling(window=7).mean()

    # Generate the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['Time'], df['SMA'], marker='o', linestyle='-', label=location)
    plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.HourLocator(interval=1))
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%I:%M %p'))
    plt.title(f"Count vs Time for {location} on {day}")
    plt.ylim(0, capacities.get(location, 100))
    plt.xlabel("Time")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    # Encode the image to base64
    graph_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return jsonify({"graph": graph_base64})

if __name__ == '__main__':
    from os import getenv
    app.run(host="0.0.0.0", port=int(getenv("PORT", 5000)))

from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import pandas as pd
import io
import base64

app = Flask(__name__)

def graph(location, day):
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
    # plt.show()


@app.route('/generate-graph', methods=['GET'])
def generate_graph():
    location = request.args.get('location')
    day = request.args.get('day')

    if not location or not day:
        return jsonify({"error": "Please provide both location and day"}), 400
    
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

    # Return the image as a base64 string
    return jsonify({"graph": graph_base64})

if __name__ == '__main__':
    app.run(debug=True)

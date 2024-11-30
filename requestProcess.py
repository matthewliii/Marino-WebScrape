from flask import Flask, jsonify, request, send_file
import numpy as np
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    # Generate NumPy data
    x = np.linspace(0, 10, 100).tolist()
    y = np.sin(x).tolist()
    return jsonify({'x': x, 'y': y})

@app.route('/graph', methods=['GET'])
def get_graph():
    # Generate a graph with Matplotlib
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    plt.figure(figsize=(6, 4))
    plt.plot(x, y, label="Sine Wave")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()

    # Save the plot to a BytesIO object and send it
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return send_file(buf, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)

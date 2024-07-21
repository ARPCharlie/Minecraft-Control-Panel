from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS

MINECRAFT_SERVER_URL = 'http://localhost:8080'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stop', methods=['POST'])
def stop():
    response = requests.post(f"{MINECRAFT_SERVER_URL}/stop")
    if response.status_code == 200:
        return jsonify({"status": "Server stopping"}), 200
    else:
        return jsonify({"error": "Failed to stop server"}), 500

@app.route('/restart', methods=['POST'])
def restart():
    response = requests.post(f"{MINECRAFT_SERVER_URL}/restart")
    if response.status_code == 200:
        return jsonify({"status": "Server restarting"}), 200
    else:
        return jsonify({"error": "Failed to restart server"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

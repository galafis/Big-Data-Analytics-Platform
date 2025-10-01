import os
from flask import Flask, jsonify, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import json
from datetime import datetime
import subprocess

from config.config import Config

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'web'), template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'web'))
app.config.from_object(Config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'version': '1.0.0',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/process', methods=['POST'])
def process_data():
    # Placeholder for data processing logic
    data = request.json
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    # Simulate processing
    processed_data = {'status': 'success', 'received_data': data, 'processed_at': datetime.now().isoformat()}
    return jsonify(processed_data)

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    # Placeholder for analytics results
    # In a real scenario, this would trigger R scripts or fetch results from a database
    try:
        # Example: Run an R script for analytics
        analytics_script_path = os.path.join(app.config['ANALYTICS_SCRIPTS_PATH'], 'analytics.R')
        result = subprocess.run(['Rscript', analytics_script_path], capture_output=True, text=True, check=True)
        return jsonify({'status': 'success', 'analytics_output': result.stdout.splitlines()})
    except subprocess.CalledProcessError as e:
        return jsonify({'status': 'error', 'message': 'R script failed', 'details': e.stderr}), 500
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'R analytics script not found'}), 404

@app.route('/api/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'status': 'success', 'message': 'File uploaded successfully', 'filename': filename}), 200
    return jsonify({'error': 'File upload failed'}), 500

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)


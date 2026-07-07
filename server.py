from flask import Flask, request, jsonify, send_from_directory
import time

app = Flask(__name__, static_folder='.')
database = {}

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/submit_test', methods=['POST'])
def submit_test():
    data = request.get_json() or {}
    wallet = data.get('wallet', 'unknown')
    ip = request.remote_addr
    
    if ip in database and time.time() - database[ip] < 1800:
        return jsonify({'error': 'Rate limit exceeded. 30 min cooldown.'}), 429
        
    database[ip] = time.time()
    results = {'ping': '42ms', 'download_speed': '120Mbps', 'upload_speed': '45Mbps'}
    return jsonify({'status': 'success', 'results': results, 'reward_points': 10}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

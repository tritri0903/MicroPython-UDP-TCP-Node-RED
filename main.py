# main.py -- put your code here!

import machine
import network
import usocket as socket
import json
import time

# Remplacez ces valeurs par les informations de votre réseau Wi-Fi
SSID = "electroProjectWifi"
PASSWORD = "M13#MRSE"

#SSID = "WiFi-2.4-B4E5"
#PASSWORD = "185E23AC26"

wlan = network.WLAN(network.STA_IF)

def connect_to_wifi():
    # Configure la connexion Wi-Fi
    wlan.active(True)

    # Vérifie si la connexion Wi-Fi est déjà établie
    if not wlan.isconnected():
        print("Connexion au reseau Wi-Fi...")
        wlan.connect(SSID, PASSWORD)

        while not wlan.isconnected():
            pass

    print("Connexion Wi-Fi etablie, Adresse IP :", wlan.ifconfig()[0])
    
led = machine.Pin(2, machine.Pin.OUT)  # GPIO2 pour la LED intégrée

# Configuration des sockets TCP et UDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Adresse IP et port de l'ordinateur
udp_address = "192.168.1.100"  # Remplacez par l'adresse IP de votre ordinateur
udp_port = 8888  # Port UDP sur votre ordinateur

# Fonction pour envoyer les données
def send_data(data):
    try:
        # Envoi via TCP
        tcp_socket.connect((udp_address, udp_port))
        tcp_socket.send(data.encode())
        tcp_socket.close()
        print("Sent via TCP:", data)
        
        # Envoi via UDP
        udp_socket.sendto(data.encode(), (udp_address, udp_port))
        print("Sent via UDP:", data)
    except OSError as e:
        print("Error:", e)

counter = 0

while True:
    # Allume la LED pour indiquer que le dispositif est prêt
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)

    # Envoi des données avec un délai d'une seconde
    send_data(str(counter))
    counter += 1
    time.sleep(1)

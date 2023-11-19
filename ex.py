import network   #on importe la librairie network 
import usocket as socket
import ujson #on importe les librairie pour le http 
from machine import Pin #on importe Pin de la librairie machine
import time

tcp_port  = 12345;
udp_port  = 12000;
server_ip = '172.20.10.4';

led = Pin(2, Pin.OUT) #on configure la pin 16 comme sortie (la où est connecté la led)

#Connexion au  WIFI

SSID = "iPhoneXr"
PASSWORD = "1234567890"
wlan = network.WLAN(network.STA_IF) #Creer un objet WLAN et l'initialise
wlan.active(True)           #Permet d'activer la connexion

if not wlan.isconnected():  #si on est pas conneccté au wifi
    print('Connecting to Wi-Fi...')  #affiche qu'on se connecte
    wlan.connect(SSID, PASSWORD)     #se connecte au wifi en utilisant ssid et WiFi_pass
    while not wlan.isconnected():    #boucle tant qu'on est pas connecté
        pass
print('Connected to Wi-Fi:', SSID)   #affiche qu'on se connecte

#Pret à recevoir des données

led.value(0)    #Allume la led


def send_tcp_data(data):
    s = socket.socket()
    addr = socket.getaddrinfo(server_ip, tcp_port)[0][-1]
    s.connect(addr)
    s.sendall(str(data).encode())
    s.close()

def send_udp_data(data):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = socket.getaddrinfo(server_ip, udp_port)[0][-1]
    s.sendto(str(data).encode(), addr)
    s.close()

data_to_send = 0

while True:
    led.value(0)  # Allume la LED pour indiquer l'envoi de données

    # Envoi des données sur la socket TCP
    try:
        #send_tcp_data(data_to_send)
        print("tcp send")
    except Exception as e:
        print("Error sending TCP data:", e)

    # Envoi des données sur la socket UDP
    try:
        send_udp_data(data_to_send + 10)
    except Exception as e:
        print("Error sending UDP data:", e)
    led.value(1)
    time.sleep(0.1)  # Ajoutez un délai en fonction de votre fréquence d'envoi
    data_to_send += 1

    if data_to_send > 100:
        data_to_send = 0
      # Éteint la LED

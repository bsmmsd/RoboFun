import network
import socket
from machine import Pin
import time

# --- SETTINGS ---
WIFI_SSID = "YOUR_WIFI"
WIFI_PASS = "YOUR_PASSWORD"

AP_SSID = "RoboFun"
AP_PASS = "12345678"   # must be at least 8 chars

led = Pin(2, Pin.OUT)

#----------------------------------------------------
# Try to connect to WiFi Station mode
#----------------------------------------------------
def connect_sta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)

    print("Connecting to WiFi:", WIFI_SSID)
    timeout = 10
    while timeout > 0:
        if wlan.isconnected():
            print("Connected:", wlan.ifconfig())
            return True
        time.sleep(1)
        timeout -= 1

    print("WiFi NOT found.")
    return False

#----------------------------------------------------
# Create Access Point (Fallback)
#----------------------------------------------------
def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=AP_SSID, password=AP_PASS)
    print("Access Point:", AP_SSID)
    print("IP:", ap.ifconfig()[0])
    return ap

#----------------------------------------------------
# Start web server
#----------------------------------------------------
def start_web_server():

    # Load index page
    with open("index.html") as f:
        page = f.read()

    addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Web server ready on port 80")

    while True:
        cl, addr = s.accept()
        req = cl.recv(1024).decode()

        if "GET /on" in req:
            led.value(1)
        elif "GET /off" in req:
            led.value(0)

        cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        cl.send(page)
        cl.close()

#----------------------------------------------------
# MAIN
#----------------------------------------------------
if not connect_sta():
    start_ap()

start_web_server()

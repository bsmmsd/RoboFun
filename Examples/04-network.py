import network
import time

# --- SETTINGS ---
WIFI_SSID = "YOUR_WIFI"
WIFI_PASS = "YOUR_PASSWORD"

AP_SSID = "RoboFun"
AP_PASS = "12345678"

#----------------------------------------------------
# Try to connect to WiFi Station mode
#----------------------------------------------------
def connect_sta():
    if WIFI_SSID == "YOUR_WIFI":
        return False

    retry = 3
    timeout = 10
    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    attempt = 0
    while attempt < retry:
        attempt += 1
        print(f"Attempt {attempt} to connect to WiFi '{WIFI_SSID}'")
        try:
            wlan.connect(WIFI_SSID, WIFI_PASS)
            t = timeout
            while t > 0:
                if wlan.isconnected():
                    print("Connected to WiFi!")
                    print("IP address:", wlan.ifconfig())
                    return True
                print("Waiting for connection...")
                time.sleep(1)
                t -= 1

            print("Timeout, could not connect.")

        except OSError as e:
            print("WiFi Internal Error:", e)

        print("Retrying in 3 seconds...\n")
        time.sleep(3)

    print("Failed to connect after", retry, "attempts.")
    return False

#----------------------------------------------------
# Create Access Point (Fallback)
#----------------------------------------------------
def start_ap():
    try:
        ap = network.WLAN(network.AP_IF)
        ap.active(True)
        ap.config(essid=AP_SSID, password=AP_PASS)
        print("Access Point:", AP_SSID)
        print("Access Point:", AP_PASS)
        print("IP:", ap.ifconfig()[0])
        return ap
    except Exception  as e:
        print("WiFi Internal Error:", e)

#----------------------------------------------------
# MAIN
#----------------------------------------------------
if not connect_sta(): start_ap()


from machine import Pin
import time

LED_PIN = 2
led = Pin(LED_PIN, Pin.OUT)

def do_blink():
    while True:
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)


def say_hello():
    while True:
        print("Hello!")
        time.sleep(2)


say_hello()
do_blink()


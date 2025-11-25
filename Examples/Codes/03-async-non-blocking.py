import uasyncio as asyncio
from machine import Pin
import utime

LED_PIN = 2
led = Pin(LED_PIN, Pin.OUT)

async def do_blink():
    while True:
        led.on()
        await asyncio.sleep(0.5)
        led.off()
        await asyncio.sleep(0.5)

async def say_hello():
    while True:
        print("Hello!")
        await asyncio.sleep(2)

async def main():
    asyncio.create_task(say_hello())
    asyncio.create_task(do_blink())
    while True:
        await asyncio.sleep(1)

asyncio.run(main())

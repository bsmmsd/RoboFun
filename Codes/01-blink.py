from machine import Pin
import utime

LED_PIN = 2          # اگر لازم شد این عدد را به پایه‌ی مورد نظر تغییر بده
led = Pin(LED_PIN, Pin.OUT)

print("Hello!")

while True:
    led.on()         # روشن
    utime.sleep_ms(500)   # ۵۰۰ میلی‌ثانیه روشن بمونه
    led.off()        # خاموش
    utime.sleep_ms(500)   # ۵۰۰ میلی‌ثانیه خاموش بمونه

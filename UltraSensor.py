from machine import Pin
import utime
trigger = Pin(16, Pin.OUT)
echo = Pin(17, Pin.IN, Pin.PULL_DOWN)

def disincm():
    trigger.value(1)
    utime.sleep_us(10)
    trigger.value(0)

    while echo.value() == 0:
        start = utime.ticks_us()
    while echo.value() == 1:
        end = utime.ticks_us()
    distance = ((end - start) /2 ) / 29
    
    return distance

def approx(num):
    if(num - int(num) == int(num+1)-num):
        return int(num+1)
    if(num - int(num) > int(num+1)-num):
        return int(num+1)
    else:
        return int(num)

while True:
    distance = disincm()
    print("The distance in centimeter is", distance, "cm ≈", approx(distance), "cm")
    utime.sleep(1)

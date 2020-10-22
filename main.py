import board
import digitalio
import time
led=digitalio.DigitalInOut(board.13)
led.direction = difitalio.Direction.OUTPUT
while True
    led.value=True
    time.sleep(0.5)
    led.value=False
    time.sleep(0.5)
  

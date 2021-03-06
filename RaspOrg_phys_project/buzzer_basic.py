from gpiozero import Buzzer
from time import sleep

buzzer = Buzzer(19)

#while True:
    #buzzer.beep() #similar to led.blink()
while True:
   
    buzzer.on()
    sleep(0.01)
    buzzer.off()
    sleep(0.01)

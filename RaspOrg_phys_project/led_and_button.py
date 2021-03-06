# Write your code here :-)
from gpiozero import LED, Button
from time import sleep

led = LED(17)
button = Button(2)

button.wait_for_press()
print ('you pressed, blinking 7 seconds')

for i in range (0,7):
    led.on()
    sleep(i/5 + 0.2)
    led.off()
    sleep(0.5)
    
print ('now using led.toggle()')


while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.5) #if you don use this led on just when pressing button
    
    
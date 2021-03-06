# Write your code here :-)
from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)
 

led.blink(0.1,2) #(secs on, secs off)

pause() #to keep the script alive


    
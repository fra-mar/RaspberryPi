# Write your code here :-)
from gpiozero import PWMLED, Button
from signal import pause
from time import sleep

led = PWMLED(17)
button = Button(2)
 
print ('led.pulse')

led.pulse()

sleep(6)

led.off() #led.value = 0 works too

print ('LED off')

sleep (2)

print ('led.value')

led.value = 0 #off

for i in range(0,100):
    led.value = i/100
    sleep(0.1)
    
print ('led.pulse again')

led.pulse()

print ('ctrl C to break. write led.value=0 to switch off led')

pause()
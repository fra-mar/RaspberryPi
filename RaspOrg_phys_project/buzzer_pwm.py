#import the libraries used
from gpiozero import TonalBuzzer

from gpiozero.tones import Tone

from time import sleep

b = TonalBuzzer(17)

#different ways to choose note

b.play(Tone("A4")); sleep(2)

b.play(Tone(220.0)); sleep(2) # Hz

b.play(Tone(midi= 60)) ; sleep (2)# middle C in MIDI notation

b.stop() # to stop sound
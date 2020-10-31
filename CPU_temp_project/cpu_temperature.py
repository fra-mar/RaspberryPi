# Measures cpu temp during 200 sec. I use this to compare variations with /without fan

from gpiozero import CPUTemperature

from time import sleep, strftime, time

cpu = CPUTemperature()  #creates an object

count =0

fan="fan_on"   

with open("/home/pi/Documents/python/measured_temp.csv", "a") as log:  #log makes new data appends last row in file
    while True:
        
        count=count + 1
        
        if count>2400 :
            
            print ("Meausrements completed")
            break
        
        
        temp = cpu.temperature   #write cpu.temperature in the shell just to understand
        
        log.write("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"), fan, temp ))
        
        print (temp)
        print ("{0},{1},{2}\n".format(strftime("%Y-%m-%d %H:%M:%S"), fan, temp ))
        
        sleep(1)
# Measures cpu temp during 2400 sec. I use this to compare variations with /without fan

from gpiozero import CPUTemperature

from time import sleep

cpu = CPUTemperature()  #creates an object

count =0

fan="fan_off"

def file_len(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

length= file_len ("measured_temp.csv")

with open("/home/pi/Documents/python/measured_temp.csv", "r") as fan_on:  
    
    temp_on_off= open ('temp_on_off.csv', 'w')
    
  
    
    count=1
    
    for line in fan_on:
        
        line_on= line
    
        line_splitted = line_on.split(',')
    
        t_on=line_splitted[-1]
        t_on=t_on.strip()  #old file the temperature was followed by \n. with strip we get rid of \n
        
        t_off = cpu.temperature   #write cpu.temperature in the shell just to understand
        
        temp_on_off.write ("{0},{1},{2}\n".format( str(count), str(t_on) , str(t_off) ))
        print ("{0},{1},{2}\n".format(count, t_on , t_off ))
        
        count= count +1
        
        
        sleep(1)
        
    temp_on_off.close()

# read csv, put data in numpy array and finally plot it

import numpy as np

from matplotlib import pyplot as plt

loader = np.zeros ( (1,3))
data = np.zeros ( (1,3) )


with open("/home/pi/Documents/python/temp_on_off.csv", "r")  as ff:
    for line in ff:
        
        #line = ff.readline()  #if you write this then reads two lines
                            #one with line in previous line and the
                            #other with readline. Ie counts 2,4,6...
        
        line_splitted = line.split (',')
        
        line_splitted[2] = line_splitted[2][0:-2] #removes \n in last temp
        
        for i in range (0,3):
            
            loader[0,i]= float(line_splitted[i])
        
        
        #data = np.concatenate ( (data, loader), axis=0) #This two options
        data = np.append (data, loader, axis=0)           #work well
        
#plotting
        
data = np.delete (data, 0, axis =0) #delete first row with just 000


my_fig=plt.figure('Fan on vs off RaspberryPi',figsize=(8,4),facecolor=('0.9'),edgecolor='black')

my_ax=my_fig.add_subplot(1,1,1)

my_ax.plot(data[:,1], label = "Fan_on")

my_ax.plot(data[:,2], label = "Fan_off")

marks_number=[]; marks_number = [x for x in range (0,len(data),500)]

marks = data [:,0][marks_number] -1

my_ax.set_xticks(marks_number)

#marks=[]
#for i in range (0, len(data), 200):
    #marks.append(int(data[i,0])-1 )

my_ax.set_xticklabels(marks,rotation=0)

my_ax.legend(loc=5)

my_ax.yaxis.grid(ls=':',c=('0.9'),lw=2, alpha=0.5)

my_ax.set_xlabel('Time after "cold" start (s)')
my_ax.set_ylabel('Temperature (C)')
my_ax.set_title('Raspberry Pi. CPU temp: fan on vs off')

plt.show()
        
        
        
        
        
import os

def get_cpu_speed():
    #“Returns the current CPU speed”
    f = os.popen('/opt/vc/bin/vcgencmd get_config arm_freq')
    cpu = f.read()
    return cpu
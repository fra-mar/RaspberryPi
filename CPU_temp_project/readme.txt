Project intended to get used to RaspberryPi.

cpu.load doesn't work. Intended to return the CPU speed in that moment

cpu_temperature.py measures cpu temp when fan on (if it´s connected) and saves the data in a temperature.csv

cpu_temp_on_off.py takes those data from temperature.csv, measures temp with fan off (if fan is disconnected) and saves them in another csv (temp_on_off)

read_plot_temp_results.py plot the data.
